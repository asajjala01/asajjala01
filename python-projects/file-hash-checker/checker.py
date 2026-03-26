import hashlib
import requests
import os
import sys
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
API_URL = "https://www.virustotal.com/api/v3/files/"

if not API_KEY:
    print("[!] Error: VIRUSTOTAL_API_KEY not found in .env file")
    sys.exit(1)

def generate_hashes(filepath):
    """
    Generates MD5, SHA1, and SHA256 hashes for a given file.
    Returns a dictionary of hashes or None if file cannot be read.
    """
    if not isinstance(filepath, str) or not filepath.strip():
        return None

    if not os.path.isfile(filepath):
        print(f"[!] Error: file not found — {filepath}")
        return None

    try:
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()

        with open(filepath, "rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                md5.update(chunk)
                sha1.update(chunk)
                sha256.update(chunk)

        return {
            "filepath": filepath,
            "md5": md5.hexdigest(),
            "sha1": sha1.hexdigest(),
            "sha256": sha256.hexdigest()
        }

    except (IOError, OSError) as e:
        print(f"[!] Error reading file {filepath}: {e}")
        return None

def check_hash(hash_value):
    if not isinstance(hash_value, str) or not hash_value.strip():
        return None

    hash_value = hash_value.strip()
    
    # Valid hashes are hex strings of specific lengths
    # MD5=32, SHA1=40, SHA256=64
    valid_lengths = [32, 40, 64]
    if len(hash_value) not in valid_lengths:
        print(f"[!] Invalid hash format: {hash_value[:20]}...")
        return None
    
    if not all(c in "0123456789abcdefABCDEF" for c in hash_value):
        print(f"[!] Invalid hash format — non-hex characters detected")
        return None

    headers = {
        "x-apikey": API_KEY
    }

    try:
        response = requests.get(API_URL + hash_value, headers=headers)

        if response.status_code == 200:
            data = response.json()
            stats = data["data"]["attributes"]["last_analysis_stats"]
            name = data["data"]["attributes"].get("meaningful_name", "Unknown")

            return {
                "hash": hash_value,
                "malicious": stats["malicious"],
                "suspicious": stats["suspicious"],
                "undetected": stats["undetected"],
                "harmless": stats["harmless"],
                "name": name,
                "total_engines": sum(stats.values())
            }

        elif response.status_code == 404:
            return {
                "hash": hash_value,
                "malicious": 0,
                "suspicious": 0,
                "undetected": 0,
                "harmless": 0,
                "name": "Not found in VirusTotal database",
                "total_engines": 0
            }

        elif response.status_code == 429:
            print("[!] Rate limit hit — too many requests")
            return None

        else:
            print(f"[!] API error — status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"[!] Connection error: {e}")
        return None
    
def analyze_file(filepath, threshold=5):
    if not isinstance(threshold, int) or isinstance(threshold, bool) or threshold < 1:
        print("[!] Error: threshold must be a positive integer")
        return None

    # Validate filepath before printing
    if not isinstance(filepath, str) or not filepath.strip():
        return None

    print(f"[*] Analyzing: {filepath}")

    hashes = generate_hashes(filepath)
    if hashes is None:
        return None

    print(f"    MD5:    {hashes['md5']}")
    print(f"    SHA1:   {hashes['sha1']}")
    print(f"    SHA256: {hashes['sha256']}")

    print(f"[*] Checking VirusTotal...")
    vt_result = check_hash(hashes["sha256"])

    if vt_result is None:
        return None

    return {
        "filepath": filepath,
        "md5": hashes["md5"],
        "sha1": hashes["sha1"],
        "sha256": hashes["sha256"],
        "malicious": vt_result["malicious"],
        "suspicious": vt_result["suspicious"],
        "undetected": vt_result["undetected"],
        "harmless": vt_result["harmless"],
        "name": vt_result["name"],
        "total_engines": vt_result["total_engines"],
        "verdict": "MALICIOUS" if vt_result["malicious"] >= threshold else
                   "SUSPICIOUS" if vt_result["suspicious"] >= threshold else
                   "CLEAN"
    }

def generate_report(results):
    """
    Takes a list of file analysis results and prints a formatted report.
    """
    if not isinstance(results, list):
        print("[!] Error: results must be a list")
        return

    total = len(results)
    malicious = [r for r in results if r["verdict"] == "MALICIOUS"]
    suspicious = [r for r in results if r["verdict"] == "SUSPICIOUS"]
    clean = [r for r in results if r["verdict"] == "CLEAN"]

    print("\n" + "=" * 60)
    print("       FILE HASH TRIAGE REPORT")
    print("=" * 60)
    print(f"Report generated:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total files:       {total}")
    print(f"Malicious:         {len(malicious)}")
    print(f"Suspicious:        {len(suspicious)}")
    print(f"Clean:             {len(clean)}")
    print("=" * 60)

    if malicious:
        print("\n[!!!] MALICIOUS FILES")
        print("-" * 60)
        for r in malicious:
            try:
                print(f"  File           : {r.get('filepath', 'Unknown')}")
                print(f"  Name           : {r.get('name', 'Unknown')}")
                print(f"  MD5            : {r.get('md5', 'Unknown')}")
                print(f"  SHA1           : {r.get('sha1', 'Unknown')}")
                print(f"  SHA256         : {r.get('sha256', 'Unknown')}")
                print(f"  Malicious      : {r.get('malicious', 0)}/{r.get('total_engines', 0)} engines")
                print(f"  Suspicious     : {r.get('suspicious', 0)}/{r.get('total_engines', 0)} engines")
                print("-" * 60)
            except (KeyError, TypeError):
                print("  [!] Malformed result entry")
                print("-" * 60)

    if suspicious:
        print("\n[!] SUSPICIOUS FILES")
        print("-" * 60)
        for r in suspicious:
            print(f"  File           : {r['filepath']}")
            print(f"  Name           : {r['name']}")
            print(f"  MD5            : {r['md5']}")
            print(f"  SHA1           : {r['sha1']}")
            print(f"  SHA256         : {r['sha256']}")
            print(f"  Malicious      : {r['malicious']}/{r['total_engines']} engines")
            print(f"  Suspicious     : {r['suspicious']}/{r['total_engines']} engines")
            print("-" * 60)

    if clean:
        print("\n[*] CLEAN FILES")
        print("-" * 60)
        for r in clean:
            print(f"  File           : {r['filepath']}")
            print(f"  Name           : {r['name']}")
            print(f"  SHA256         : {r['sha256']}")
            print(f"  Engines        : {r['total_engines']} checked")
            print("-" * 60)

    print(f"\n[*] Analysis complete. {len(malicious)} malicious, {len(suspicious)} suspicious, {len(clean)} clean.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python checker.py <file_or_directory>")
        print("Example: python checker.py suspicious.exe")
        print("Example: python checker.py /path/to/folder")
        sys.exit(1)

    target = sys.argv[1]
    files_to_check = []

    if os.path.isfile(target):
        files_to_check.append(target)

    elif os.path.isdir(target):
        print(f"[*] Scanning directory: {target}")
        for filename in os.listdir(target):
            filepath = os.path.join(target, filename)
            if os.path.isfile(filepath):
                files_to_check.append(filepath)

    else:
        print(f"[!] Error: {target} is not a valid file or directory")
        sys.exit(1)

    if not files_to_check:
        print("[!] No files found to analyze")
        sys.exit(1)

    print(f"[*] Found {len(files_to_check)} file(s) to analyze")

    results = []
    for filepath in files_to_check:
        result = analyze_file(filepath)
        if result is not None:
            results.append(result)

    if not results:
        print("[!] No results to report")
        sys.exit(1)

    generate_report(results)


if __name__ == "__main__":
    main()