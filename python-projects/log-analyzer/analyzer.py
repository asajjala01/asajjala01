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

