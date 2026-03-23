from analyzer import parse_log_line, detect_brute_force, detect_admin_probe, detect_path_traversal, create_alert, generate_report

# ============================================================
# SECTION 1 — parse_log_line edge cases
# ============================================================

print("=" * 50)
print("TEST 1 — valid log line")
print("=" * 50)
print(parse_log_line('10.0.0.5 - - [23/Mar/2026:10:00:04] "POST /login HTTP/1.1" 401 512'))

print("\n" + "=" * 50)
print("TEST 2 — empty string")
print("=" * 50)
print(parse_log_line(""))

print("\n" + "=" * 50)
print("TEST 3 — None as input")
print("=" * 50)
print(parse_log_line(None))

print("\n" + "=" * 50)
print("TEST 4 — integer as input")
print("=" * 50)
print(parse_log_line(12345))

print("\n" + "=" * 50)
print("TEST 5 — missing IP address")
print("=" * 50)
print(parse_log_line('- - [23/Mar/2026:10:00:04] "POST /login HTTP/1.1" 401 512'))

print("\n" + "=" * 50)
print("TEST 6 — missing status code")
print("=" * 50)
print(parse_log_line('10.0.0.5 - - [23/Mar/2026:10:00:04] "POST /login HTTP/1.1"'))

print("\n" + "=" * 50)
print("TEST 7 — malformed timestamp")
print("=" * 50)
print(parse_log_line('10.0.0.5 - - [BADTIMESTAMP] "POST /login HTTP/1.1" 401 512'))

print("\n" + "=" * 50)
print("TEST 8 — extra whitespace throughout")
print("=" * 50)
print(parse_log_line('10.0.0.5  -  -  [23/Mar/2026:10:00:04]  "POST /login HTTP/1.1"  401  512'))

print("\n" + "=" * 50)
print("TEST 9 — SQL injection in endpoint")
print("=" * 50)
print(parse_log_line('10.0.0.5 - - [23/Mar/2026:10:00:04] "GET /login?id=1 OR 1=1 HTTP/1.1" 200 512'))

print("\n" + "=" * 50)
print("TEST 10 — extremely long endpoint")
print("=" * 50)
print(parse_log_line(f'10.0.0.5 - - [23/Mar/2026:10:00:04] "GET /{"A" * 10000} HTTP/1.1" 200 512'))

print("\n" + "=" * 50)
print("TEST 11 — null byte in log line")
print("=" * 50)
print(parse_log_line('10.0.0.5 - - [23/Mar/2026:10:00:04] "GET /index\x00.html HTTP/1.1" 200 512'))

print("\n" + "=" * 50)
print("TEST 12 — unicode characters in endpoint")
print("=" * 50)
print(parse_log_line('10.0.0.5 - - [23/Mar/2026:10:00:04] "GET /pàge.html HTTP/1.1" 200 512'))

# ============================================================
# SECTION 2 — detection function edge cases
# ============================================================

print("\n" + "=" * 50)
print("TEST 13 — empty entries list")
print("=" * 50)
print(detect_brute_force([]))
print(detect_admin_probe([]))
print(detect_path_traversal([]))

print("\n" + "=" * 50)
print("TEST 14 — None as entries")
print("=" * 50)
print(detect_brute_force(None))

print("\n" + "=" * 50)
print("TEST 15 — threshold of 0")
print("=" * 50)
entries = []
with open("sample.log", "r") as f:
    for line in f:
        entry = parse_log_line(line.strip())
        if entry:
            entries.append(entry)
print(detect_brute_force(entries, threshold=0))

print("\n" + "=" * 50)
print("TEST 16 — threshold of 1")
print("=" * 50)
print(detect_brute_force(entries, threshold=1))

print("\n" + "=" * 50)
print("TEST 17 — threshold of 99999")
print("=" * 50)
print(detect_brute_force(entries, threshold=99999))

print("\n" + "=" * 50)
print("TEST 18 — negative threshold")
print("=" * 50)
print(detect_brute_force(entries, threshold=-1))

print("\n" + "=" * 50)
print("TEST 19 — string as threshold")
print("=" * 50)
print(detect_brute_force(entries, threshold="five"))

print("\n" + "=" * 50)
print("TEST 20 — entries list with None inside it")
print("=" * 50)
print(detect_brute_force([None, None, None]))

print("\n" + "=" * 50)
print("TEST 21 — entries with missing keys")
print("=" * 50)
print(detect_brute_force([{"ip": "1.2.3.4"}]))

print("\n" + "=" * 50)
print("TEST 22 — entries with wrong data types in fields")
print("=" * 50)
print(detect_brute_force([{"ip": None, "status": "401", "endpoint": 123}]))

print("\n" + "=" * 50)
print("TEST 23 — path traversal with windows style path")
print("=" * 50)
print(detect_path_traversal([{"ip": "1.2.3.4", "status": 200, "endpoint": "..\\..\\windows\\system32"}]))

print("\n" + "=" * 50)
print("TEST 24 — path traversal with encoded traversal attempt")
print("=" * 50)
print(detect_path_traversal([{"ip": "1.2.3.4", "status": 200, "endpoint": "%2e%2e%2f%2e%2e%2f"}]))

print("\n" + "=" * 50)
print("TEST 25 — 1000 identical 401s from same IP")
print("=" * 50)
flood_entries = [{"ip": "9.9.9.9", "status": 401, "endpoint": "/login", "method": "POST", "size": 512, "timestamp": "23/Mar/2026:10:00:00"} for _ in range(1000)]
print(detect_brute_force(flood_entries))

# ============================================================
# SECTION 3 — report generator edge cases
# ============================================================

print("\n" + "=" * 50)
print("TEST 26 — empty alerts list")
print("=" * 50)
generate_report([], "sample.log")

print("\n" + "=" * 50)
print("TEST 27 — None as alerts")
print("=" * 50)
generate_report(None, "sample.log")

print("\n" + "=" * 50)
print("TEST 28 — None as log file name")
print("=" * 50)
generate_report([], None)

print("\n" + "=" * 50)
print("TEST 29 — alert with missing keys")
print("=" * 50)
generate_report([{"type": "TEST"}], "sample.log")

print("\n" + "=" * 50)
print("TEST 30 — 1000 alerts at once")
print("=" * 50)
big_alerts = [create_alert("FLOOD TEST", "9.9.9.9", f"alert number {i}") for i in range(1000)]
generate_report(big_alerts, "sample.log")