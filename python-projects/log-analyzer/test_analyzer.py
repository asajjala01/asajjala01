from analyzer import parse_log_line

print("=" * 50)
print("TEST 1 — valid log line")
print("=" * 50)
result = parse_log_line('10.0.0.5 - - [23/Mar/2026:10:00:04] "POST /login HTTP/1.1" 401 512')
print(result)

print("\n" + "=" * 50)
print("TEST 2 — empty line")
print("=" * 50)
result = parse_log_line("")
print(result)

print("\n" + "=" * 50)
print("TEST 3 — random string")
print("=" * 50)
result = parse_log_line("this is not a log line")
print(result)

print("\n" + "=" * 50)
print("TEST 4 — valid line with 200 status")
print("=" * 50)
result = parse_log_line('192.168.1.1 - - [23/Mar/2026:10:00:01] "GET /index.html HTTP/1.1" 200 1024')
print(result)

print("\n" + "=" * 50)
print("TEST 5 — path traversal line")
print("=" * 50)
result = parse_log_line('10.0.0.9 - - [23/Mar/2026:10:00:21] "GET /../../../etc/passwd HTTP/1.1" 400 128')
print(result)