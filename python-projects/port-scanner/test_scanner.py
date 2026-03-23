from scanner import scan_port, grab_banner, run_scan
import socket

print("=" * 50)
print("TEST 1 — empty string as target")
print("=" * 50)
print(scan_port("", 80))

print("\n" + "=" * 50)
print("TEST 2 — None as target")
print("=" * 50)
print(scan_port(None, 80))

print("\n" + "=" * 50)
print("TEST 3 — integer as target instead of string")
print("=" * 50)
print(scan_port(12345, 80))

print("\n" + "=" * 50)
print("TEST 4 — list as target")
print("=" * 50)
print(scan_port(["scanme.nmap.org"], 80))

print("\n" + "=" * 50)
print("TEST 5 — negative port")
print("=" * 50)
print(scan_port("scanme.nmap.org", -1))

print("\n" + "=" * 50)
print("TEST 6 — port above 65535")
print("=" * 50)
print(scan_port("scanme.nmap.org", 99999))

print("\n" + "=" * 50)
print("TEST 7 — float as port")
print("=" * 50)
print(scan_port("scanme.nmap.org", 80.5))

print("\n" + "=" * 50)
print("TEST 8 — None as port")
print("=" * 50)
print(scan_port("scanme.nmap.org", None))

print("\n" + "=" * 50)
print("TEST 9 — both target and port are None")
print("=" * 50)
print(scan_port(None, None))

print("\n" + "=" * 50)
print("TEST 10 — very long string as target")
print("=" * 50)
print(scan_port("A" * 10000, 80))

print("\n" + "=" * 50)
print("TEST 11 — special characters as target")
print("=" * 50)
print(scan_port("!@#$%^&*()", 80))

print("\n" + "=" * 50)
print("TEST 12 — SQL injection attempt as target")
print("=" * 50)
print(scan_port("' OR '1'='1", 80))

print("\n" + "=" * 50)
print("TEST 13 — localhost loopback")
print("=" * 50)
print(scan_port("127.0.0.1", 80))

print("\n" + "=" * 50)
print("TEST 14 — internal network range")
print("=" * 50)
print(scan_port("192.168.1.1", 80))

print("\n" + "=" * 50)
print("TEST 15 — run_scan with None as target")
print("=" * 50)
print(run_scan(None, 1, 10, threads=5))

print("\n" + "=" * 50)
print("TEST 16 — run_scan with negative start port")
print("=" * 50)
print(run_scan("scanme.nmap.org", -5, 10, threads=5))

print("\n" + "=" * 50)
print("TEST 17 — run_scan with 0 threads")
print("=" * 50)
print(run_scan("scanme.nmap.org", 79, 82, threads=0))

print("\n" + "=" * 50)
print("TEST 18 — run_scan with float as thread count")
print("=" * 50)
print(run_scan("scanme.nmap.org", 79, 82, threads=10.5))

print("\n" + "=" * 50)
print("TEST 19 — banner grab with None port")
print("=" * 50)
print(grab_banner("scanme.nmap.org", None))

print("\n" + "=" * 50)
print("TEST 20 — banner grab with list as target")
print("=" * 50)
print(grab_banner(["scanme.nmap.org"], 80))

