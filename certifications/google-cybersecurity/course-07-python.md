# Course 7: Automate Cybersecurity Tasks with Python

**Course:** Google Cybersecurity Certificate — Course 7 of 8  
**Status:** ✅ Completed

---

## Why Python for Security

- Fast to write, easy to read
- Huge library ecosystem for security tasks (`socket`, `os`, `re`, `hashlib`, `requests`, `scapy`)
- Used in automation, tooling, log parsing, scripting exploits, and building detections
- Expected skill for SOC analysts and security engineers

---

## Core Python Review (Security Context)

### Working with Files (Log Parsing)
```python
# Read a log file line by line
with open("/var/log/auth.log", "r") as f:
    for line in f:
        if "Failed password" in line:
            print(line.strip())
```

### Regular Expressions for Log Analysis
```python
import re

log_line = "Jan 15 03:22:01 server sshd[1234]: Failed password for root from 192.168.1.50 port 54321"

# Extract IP address
ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log_line)
if ip:
    print(ip.group())   # 192.168.1.50

# Extract username attempted
user = re.search(r'Failed password for (\w+)', log_line)
if user:
    print(user.group(1))  # root
```

### String Methods for Parsing
```python
line = "2026-01-15 03:22:01 FAILED LOGIN admin 192.168.1.50"

parts = line.split()
timestamp = parts[0] + " " + parts[1]
status    = parts[2]
username  = parts[4]
ip        = parts[5]
```

---

## Security Automation Examples

### Automated Failed Login Counter
```python
import re
from collections import Counter

failed_ips = []

with open("auth.log", "r") as f:
    for line in f:
        if "Failed password" in line:
            match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                failed_ips.append(match.group(1))

counts = Counter(failed_ips)
print("Top offenders:")
for ip, count in counts.most_common(10):
    print(f"  {ip}: {count} attempts")
```

### IP Allowlist Checker
```python
def check_access(ip_address, allowlist):
    """Check if an IP is in the approved allowlist."""
    if ip_address in allowlist:
        return f"ACCESS GRANTED: {ip_address}"
    else:
        return f"ACCESS DENIED: {ip_address} — not in allowlist"

allowlist = ["10.0.0.1", "10.0.0.2", "192.168.1.100"]

print(check_access("10.0.0.1", allowlist))       # granted
print(check_access("203.0.113.45", allowlist))   # denied
```

### File Integrity Checker (Hashing)
```python
import hashlib

def hash_file(filepath):
    """Generate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

# Store baseline
baseline = hash_file("critical_config.conf")
print(f"Baseline hash: {baseline}")

# Later — verify integrity
current = hash_file("critical_config.conf")
if current == baseline:
    print("File integrity verified.")
else:
    print("ALERT: File has been modified!")
```

---

## Python Standard Library Modules for Security

| Module | Use Case |
|---|---|
| `os` | File system operations, running system commands |
| `re` | Regular expressions for log parsing |
| `socket` | Network connections, port scanning |
| `hashlib` | Hashing (MD5, SHA-256, etc.) |
| `hmac` | Message authentication codes |
| `ssl` | SSL/TLS connections |
| `subprocess` | Run system commands from Python |
| `json` | Parse API responses and config files |
| `csv` | Parse CSV-formatted logs |
| `datetime` | Timestamp handling and comparison |
| `collections` | Counter, defaultdict for data aggregation |

---

## Error Handling in Security Scripts
```python
import socket

def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.gaierror:
        print(f"Error: Could not resolve {host}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
```

---

## My Take

Python was a comfortable one for me going in and I'll be upfront about why — I've actually studied it twice before this. First back in college where it was part of my Computer Information Systems coursework, and more recently I completed the 100 Days of Python course on Coursera which was a much deeper dive. By the time this course came around Python wasn't new territory, it was more like revisiting a place I already knew but through a completely different lens.

That security lens is what made it interesting. I'd used Python for general projects and automation before but applying it specifically to log parsing, writing detection scripts, building port scanners — that reframing changed how I thought about the language. Suddenly every tool I'd built before had a security equivalent and I started seeing Python less as a coding language and more as a force multiplier for analyst work.

The regex stuff was the one area that gave me a little friction even with prior experience — it always does. But for anyone coming into this course with zero Python background I'd say take your time with it and lean on the 100 Days of Python course as a companion. The foundation it builds makes everything in this course land a lot harder.
