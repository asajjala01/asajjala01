from scanner import scan_port, grab_banner, run_scan
import socket
import threading

print("=" * 50)
print("TEST 1 — unicode string as target")
print("=" * 50)
print(scan_port("scanme.nmap.örg", 80))

print("\n" + "=" * 50)
print("TEST 2 — whitespace as target")
print("=" * 50)
print(scan_port("   ", 80))

print("\n" + "=" * 50)
print("TEST 3 — newline character as target")
print("=" * 50)
print(scan_port("\n", 80))

print("\n" + "=" * 50)
print("TEST 4 — tab character as target")
print("=" * 50)
print(scan_port("\t", 80))

print("\n" + "=" * 50)
print("TEST 5 — IP with letters mixed in")
print("=" * 50)
print(scan_port("192.168.1.abc", 80))

print("\n" + "=" * 50)
print("TEST 6 — IP with 5 octets instead of 4")
print("=" * 50)
print(scan_port("192.168.1.1.1", 80))

print("\n" + "=" * 50)
print("TEST 7 — IP with octets out of range")
print("=" * 50)
print(scan_port("256.256.256.256", 80))

print("\n" + "=" * 50)
print("TEST 8 — boolean True as target")
print("=" * 50)
print(scan_port(True, 80))

print("\n" + "=" * 50)
print("TEST 9 — boolean False as port")
print("=" * 50)
print(scan_port("scanme.nmap.org", False))

print("\n" + "=" * 50)
print("TEST 10 — dictionary as target")
print("=" * 50)
print(scan_port({"target": "scanme.nmap.org"}, 80))

print("\n" + "=" * 50)
print("TEST 11 — extremely large integer as port")
print("=" * 50)
print(scan_port("scanme.nmap.org", 99999999999999))

print("\n" + "=" * 50)
print("TEST 12 — port as float that looks like integer")
print("=" * 50)
print(scan_port("scanme.nmap.org", 80.0))

print("\n" + "=" * 50)
print("TEST 13 — binary string as target")
print("=" * 50)
print(scan_port(b"scanme.nmap.org", 80))

print("\n" + "=" * 50)
print("TEST 14 — null byte in target string")
print("=" * 50)
print(scan_port("scanme.nmap.org\x00", 80))

print("\n" + "=" * 50)
print("TEST 15 — port as string number")
print("=" * 50)
print(scan_port("scanme.nmap.org", "80"))

print("\n" + "=" * 50)
print("TEST 16 — run_scan with both ports as 0")
print("=" * 50)
print(run_scan("scanme.nmap.org", 0, 0, threads=5))

print("\n" + "=" * 50)
print("TEST 17 — run_scan with string as thread count")
print("=" * 50)
print(run_scan("scanme.nmap.org", 79, 82, threads="100"))

print("\n" + "=" * 50)
print("TEST 18 — run_scan with negative thread count")
print("=" * 50)
print(run_scan("scanme.nmap.org", 79, 82, threads=-1))

print("\n" + "=" * 50)
print("TEST 19 — run_scan with boolean as thread count")
print("=" * 50)
print(run_scan("scanme.nmap.org", 79, 82, threads=True))

print("\n" + "=" * 50)
print("TEST 20 — run_scan where start equals end on open port")
print("=" * 50)
print(run_scan("scanme.nmap.org", 80, 80, threads=5))

print("\n" + "=" * 50)
print("TEST 21 — run_scan with empty string as target")
print("=" * 50)
print(run_scan("", 1, 100, threads=5))

print("\n" + "=" * 50)
print("TEST 22 — banner grab on port 443 HTTPS")
print("=" * 50)
print(grab_banner("scanme.nmap.org", 443))

print("\n" + "=" * 50)
print("TEST 23 — banner grab with empty string target")
print("=" * 50)
print(grab_banner("", 80))

print("\n" + "=" * 50)
print("TEST 24 — banner grab with negative port")
print("=" * 50)
print(grab_banner("scanme.nmap.org", -1))

print("\n" + "=" * 50)
print("TEST 25 — banner grab with port 65535")
print("=" * 50)
print(grab_banner("scanme.nmap.org", 65535))

print("\n" + "=" * 50)
print("TEST 26 — scan port 0 specifically")
print("=" * 50)
print(scan_port("scanme.nmap.org", 0))

print("\n" + "=" * 50)
print("TEST 27 — run_scan with massive thread count")
print("=" * 50)
print(run_scan("scanme.nmap.org", 79, 82, threads=99999))

print("\n" + "=" * 50)
print("TEST 28 — target with path appended like a URL")
print("=" * 50)
print(scan_port("scanme.nmap.org/admin", 80))

print("\n" + "=" * 50)
print("TEST 29 — target with port appended in string")
print("=" * 50)
print(scan_port("scanme.nmap.org:80", 80))

print("\n" + "=" * 50)
print("TEST 30 — concurrent run_scan calls at the same time")
print("=" * 50)
results = []
def run_concurrent(results):
    result = run_scan("scanme.nmap.org", 79, 82, threads=5)
    results.append(result)

threads = [threading.Thread(target=run_concurrent, args=(results,)) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Concurrent results: {results}")