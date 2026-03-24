from checker import check_ip, check_multiple_ips, generate_report
import sys

print("=" * 50)
print("TEST 1 — known clean IP Google DNS")
print("=" * 50)
print(check_ip("8.8.8.8"))

print("\n" + "=" * 50)
print("TEST 2 — known malicious IP")
print("=" * 50)
print(check_ip("89.248.167.131"))

print("\n" + "=" * 50)
print("TEST 3 — private network IP")
print("=" * 50)
print(check_ip("192.168.1.1"))

print("\n" + "=" * 50)
print("TEST 4 — localhost")
print("=" * 50)
print(check_ip("127.0.0.1"))

print("\n" + "=" * 50)
print("TEST 5 — invalid IP 999.999.999.999")
print("=" * 50)
print(check_ip("999.999.999.999"))

print("\n" + "=" * 50)
print("TEST 6 — None as input")
print("=" * 50)
print(check_ip(None))

print("\n" + "=" * 50)
print("TEST 7 — empty string")
print("=" * 50)
print(check_ip(""))

print("\n" + "=" * 50)
print("TEST 8 — integer as input")
print("=" * 50)
print(check_ip(12345))

print("\n" + "=" * 50)
print("TEST 9 — SQL injection as input")
print("=" * 50)
print(check_ip("' OR '1'='1"))

print("\n" + "=" * 50)
print("TEST 10 — XSS attempt as input")
print("=" * 50)
print(check_ip("<script>alert(1)</script>"))

print("\n" + "=" * 50)
print("TEST 11 — path traversal as input")
print("=" * 50)
print(check_ip("../../etc/passwd"))

print("\n" + "=" * 50)
print("TEST 12 — IPv6 address")
print("=" * 50)
print(check_ip("2001:db8::1"))

print("\n" + "=" * 50)
print("TEST 13 — broadcast address")
print("=" * 50)
print(check_ip("255.255.255.255"))

print("\n" + "=" * 50)
print("TEST 14 — all zeros")
print("=" * 50)
print(check_ip("0.0.0.0"))

print("\n" + "=" * 50)
print("TEST 15 — whitespace only")
print("=" * 50)
print(check_ip("   "))

print("\n" + "=" * 50)
print("TEST 16 — check_multiple_ips with None")
print("=" * 50)
print(check_multiple_ips(None))

print("\n" + "=" * 50)
print("TEST 17 — check_multiple_ips with empty list")
print("=" * 50)
print(check_multiple_ips([]))

print("\n" + "=" * 50)
print("TEST 18 — check_multiple_ips with None inside list")
print("=" * 50)
print(check_multiple_ips([None, None]))

print("\n" + "=" * 50)
print("TEST 19 — check_multiple_ips with mixed valid and invalid")
print("=" * 50)
results = check_multiple_ips(["8.8.8.8", "999.999.999.999", None, "", "89.248.167.131"])
generate_report(results)

print("\n" + "=" * 50)
print("TEST 20 — generate_report with None")
print("=" * 50)
generate_report(None)

print("\n" + "=" * 50)
print("TEST 21 — generate_report with empty results")
print("=" * 50)
generate_report({"clean": [], "suspicious": [], "malicious": []})

print("\n" + "=" * 50)
print("TEST 22 — duplicate IPs in list")
print("=" * 50)
results = check_multiple_ips(["8.8.8.8", "8.8.8.8", "8.8.8.8"])
generate_report(results)

print("\n" + "=" * 50)
print("TEST 23 — negative threshold")
print("=" * 50)
print(check_multiple_ips(["8.8.8.8"], threshold=-1))

print("\n" + "=" * 50)
print("TEST 24 — threshold of 0")
print("=" * 50)
print(check_multiple_ips(["8.8.8.8"], threshold=0))

print("\n" + "=" * 50)
print("TEST 25 — threshold of 101 above maximum score")
print("=" * 50)
results = check_multiple_ips(["89.248.167.131"], threshold=101)
generate_report(results)

print("\n" + "=" * 50)
print("TEST 26 — run against full test_ips.txt file")
print("=" * 50)
with open("test_ips.txt", "r") as f:
    ip_list = f.readlines()
results = check_multiple_ips(ip_list)
generate_report(results)