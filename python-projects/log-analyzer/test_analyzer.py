from analyzer import parse_log_line, detect_brute_force, detect_admin_probe, detect_path_traversal, create_alert

# First parse all lines from sample.log
entries = []
with open("sample.log", "r") as f:
    for line in f:
        entry = parse_log_line(line.strip())
        if entry:
            entries.append(entry)

print(f"[*] Parsed {len(entries)} log entries")

print("\n" + "=" * 50)
print("TEST 1 — brute force detection")
print("=" * 50)
alerts = detect_brute_force(entries)
for alert in alerts:
    print(alert)

print("\n" + "=" * 50)
print("TEST 2 — admin probe detection")
print("=" * 50)
alerts = detect_admin_probe(entries)
for alert in alerts:
    print(alert)

print("\n" + "=" * 50)
print("TEST 3 — path traversal detection")
print("=" * 50)
alerts = detect_path_traversal(entries)
for alert in alerts:
    print(alert)

print("\n" + "=" * 50)
print("TEST 4 — create_alert structure check")
print("=" * 50)
alert = create_alert("TEST", "1.2.3.4", "this is a test alert")
print(alert)