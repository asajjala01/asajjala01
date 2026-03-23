import re
import sys
from collections import defaultdict
from datetime import datetime

def create_alert(alert_type, ip, detail):
    """
    Creates a standardized alert dictionary.
    All detection functions use this to ensure consistent alert structure.
    """
    return {
        "type": alert_type,
        "ip": ip,
        "detail": detail,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def parse_log_line(line):
    """
    Parses a single log line and extracts key fields.
    Returns a dictionary of extracted values or None if line doesn't match.
    """
    pattern = r'(\d+\.\d+\.\d+\.\d+).*\[(.+?)\].*"(\w+)\s+(\S+)\s+HTTP/\d+\.\d+"\s+(\d+)\s+(\d+)'
    
    match = re.match(pattern, line)
    
    if not match:
        return None
    
    return {
        "ip": match.group(1),
        "timestamp": match.group(2),
        "method": match.group(3),
        "endpoint": match.group(4),
        "status": int(match.group(5)),
        "size": int(match.group(6))
    }

def detect_brute_force(entries, threshold=5):
    """
    Detects brute force login attempts.
    Flags IPs that fail authentication more than threshold times.
    """
    failed_logins = defaultdict(int)
    alerts = []

    for entry in entries:
        if entry["status"] == 401:
            failed_logins[entry["ip"]] += 1

    for ip, count in failed_logins.items():
        if count >= threshold:
            alerts.append(create_alert("BRUTE FORCE", ip, f"{count} failed login attempts detected"))
    return alerts

def detect_admin_probe(entries, threshold=3):
    """
    Detects repeated attempts to access restricted endpoints.
    Flags IPs hitting forbidden resources more than threshold times.
    """
    forbidden_hits = defaultdict(int)
    alerts = []

    for entry in entries:
        if entry["status"] == 403:
            forbidden_hits[entry["ip"]] += 1

    for ip, count in forbidden_hits.items():
        if count >= threshold:
            alerts.append(create_alert("ADMIN PROBE", ip, f"{count} attempts to access restricted endpoints"))

    return alerts

def detect_path_traversal(entries):
    """
    Detects path traversal attempts in requested endpoints.
    Flags any request containing directory traversal patterns.
    """
    alerts = []
    suspicious_patterns = ["../", "..\\", "/etc/passwd", "/etc/shadow", "cmd.exe"]

    for entry in entries:
        for pattern in suspicious_patterns:
            if pattern in entry["endpoint"]:
                alerts.append(create_alert("PATH TRAVERSAL", entry["ip"], f"Suspicious pattern '{pattern}' in endpoint {entry['endpoint']}"))
                break

    return alerts

def generate_report(alerts, log_file):
    """
    Takes a list of alerts and prints a formatted SOC analyst report.
    """
    print("\n" + "=" * 60)
    print("       SOC ANALYST ALERT REPORT")
    print("=" * 60)
    print(f"Log file analyzed: {log_file}")
    print(f"Report generated:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total alerts:      {len(alerts)}")
    print("=" * 60)

    if not alerts:
        print("\n[*] No suspicious activity detected.")
        return

    for alert in alerts:
        print(f"\n[!] ALERT — {alert['type']}")
        print(f"    IP Address : {alert['ip']}")
        print(f"    Detail     : {alert['detail']}")
        print(f"    Timestamp  : {alert['timestamp']}")
        print("-" * 60)

    print(f"\n[*] Report complete. {len(alerts)} alert(s) generated.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <logfile>")
        print("Example: python analyzer.py sample.log")
        sys.exit(1)

    log_file = sys.argv[1]

    try:
        with open(log_file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"[!] Error: log file '{log_file}' not found")
        sys.exit(1)

    entries = []
    for line in lines:
        entry = parse_log_line(line.strip())
        if entry:
            entries.append(entry)

    print(f"[*] Parsed {len(entries)} log entries from {log_file}")

    all_alerts = []
    all_alerts.extend(detect_brute_force(entries))
    all_alerts.extend(detect_admin_probe(entries))
    all_alerts.extend(detect_path_traversal(entries))

    generate_report(all_alerts, log_file)

if __name__ == "__main__":
    main()