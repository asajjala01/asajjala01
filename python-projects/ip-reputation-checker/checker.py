import requests
import json
import os
import sys
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY")
API_URL = "https://api.abuseipdb.com/api/v2/check"

if not API_KEY:
    print("[!] Error: ABUSEIPDB_API_KEY not found in .env file")
    exit(1)

def check_ip(ip):
    """
    Sends a single IP address to AbuseIPDB and returns reputation data.
    """
    if not isinstance(ip, str) or not ip.strip():
        return None

    ip = ip.strip()

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(API_URL, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            result = data["data"]

            return {
                "ip": result["ipAddress"],
                "score": result["abuseConfidenceScore"],
                "country": result["countryCode"] or "Unknown",
                "isp": result["isp"] or "Unknown",
                "total_reports": result["totalReports"],
                "last_reported": result.get("lastReportedAt", "Never")
            }

        elif response.status_code == 429:
            print(f"[!] Rate limit hit — too many requests")
            return None

        else:
            print(f"[!] API error for {ip} — status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"[!] Connection error for {ip}: {e}")
        return None

def check_multiple_ips(ip_list, threshold=50):
    """
    Takes a list of IPs, checks each one, and categorizes by risk level.
    """
    if not isinstance(ip_list, list):
        print("[!] Error: ip_list must be a list")
        return {"clean": [], "suspicious": [], "malicious": []}

    if not isinstance(threshold, int) or isinstance(threshold, bool) or threshold < 1:
        print("[!] Error: threshold must be a positive integer")
        return {"clean": [], "suspicious": [], "malicious": []}

    results = {
        "clean": [],
        "suspicious": [],
        "malicious": []
    }

    total = len(ip_list)

    for i, ip in enumerate(ip_list):
        if ip is None:
            continue

        ip = str(ip).strip()

        if not ip:
            continue

        print(f"[*] Checking {ip} ({i+1}/{total})")
        result = check_ip(ip)

        if result is None:
            continue

        if result["score"] == 0:
            results["clean"].append(result)
        elif result["score"] < threshold:
            results["suspicious"].append(result)
        else:
            results["malicious"].append(result)

    return results

def generate_report(results):
    """
    Takes the categorized results and prints a formatted triage report.
    """
    if not isinstance(results, dict):
        print("[!] Error: results must be a dictionary")
        return

    total = len(results["clean"]) + len(results["suspicious"]) + len(results["malicious"])

    print("\n" + "=" * 60)
    print("       IP REPUTATION TRIAGE REPORT")
    print("=" * 60)
    print(f"Report generated:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total IPs checked: {total}")
    print(f"Clean:             {len(results['clean'])}")
    print(f"Suspicious:        {len(results['suspicious'])}")
    print(f"Malicious:         {len(results['malicious'])}")
    print("=" * 60)

    if results["malicious"]:
        print("\n[!!!] MALICIOUS IPs")
        print("-" * 60)
        for r in results["malicious"]:
            print(f"  IP           : {r['ip']}")
            print(f"  Abuse Score  : {r['score']}/100")
            print(f"  Country      : {r['country']}")
            print(f"  ISP          : {r['isp']}")
            print(f"  Total Reports: {r['total_reports']}")
            print(f"  Last Reported: {r['last_reported']}")
            print("-" * 60)

    if results["suspicious"]:
        print("\n[!] SUSPICIOUS IPs")
        print("-" * 60)
        for r in results["suspicious"]:
            print(f"  IP           : {r['ip']}")
            print(f"  Abuse Score  : {r['score']}/100")
            print(f"  Country      : {r['country']}")
            print(f"  ISP          : {r['isp']}")
            print(f"  Total Reports: {r['total_reports']}")
            print(f"  Last Reported: {r['last_reported']}")
            print("-" * 60)

    if results["clean"]:
        print("\n[*] CLEAN IPs")
        print("-" * 60)
        for r in results["clean"]:
            print(f"  IP           : {r['ip']}")
            print(f"  Abuse Score  : {r['score']}/100")
            print(f"  Country      : {r['country']}")
            print(f"  ISP          : {r['isp']}")
            print("-" * 60)

    print(f"\n[*] Triage complete. {len(results['malicious'])} malicious, {len(results['suspicious'])} suspicious, {len(results['clean'])} clean.")    
   
def main():
    if len(sys.argv) < 2:
        print("Usage: python checker.py <ip_file_or_ip>")
        print("Example: python checker.py ips.txt")
        print("Example: python checker.py 8.8.8.8")
        sys.exit(1)

    target = sys.argv[1]
    ip_list = []

    if os.path.isfile(target):
        print(f"[*] Reading IPs from file: {target}")
        with open(target, "r") as f:
            ip_list = f.readlines()
    else:
        print(f"[*] Checking single IP: {target}")
        ip_list = [target]

    if not ip_list:
        print("[!] No IPs found to check")
        sys.exit(1)

    results = check_multiple_ips(ip_list)
    generate_report(results)


if __name__ == "__main__":
    main()