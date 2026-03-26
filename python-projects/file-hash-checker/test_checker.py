from checker import generate_hashes, check_hash, analyze_file, generate_report
import os

# ============================================================
# SECTION 1 — generate_hashes edge cases
# ============================================================

print("=" * 50)
print("TEST 1 — valid file")
print("=" * 50)
print(generate_hashes("test_file.txt"))

print("\n" + "=" * 50)
print("TEST 2 — file that doesn't exist")
print("=" * 50)
print(generate_hashes("nonexistent.txt"))

print("\n" + "=" * 50)
print("TEST 3 — None as filepath")
print("=" * 50)
print(generate_hashes(None))

print("\n" + "=" * 50)
print("TEST 4 — empty string as filepath")
print("=" * 50)
print(generate_hashes(""))

print("\n" + "=" * 50)
print("TEST 5 — integer as filepath")
print("=" * 50)
print(generate_hashes(12345))

print("\n" + "=" * 50)
print("TEST 6 — directory as filepath")
print("=" * 50)
print(generate_hashes("test_folder"))

print("\n" + "=" * 50)
print("TEST 7 — whitespace as filepath")
print("=" * 50)
print(generate_hashes("   "))

print("\n" + "=" * 50)
print("TEST 8 — path traversal as filepath")
print("=" * 50)
print(generate_hashes("../../etc/passwd"))

print("\n" + "=" * 50)
print("TEST 9 — empty file")
print("=" * 50)
open("empty_file.txt", "w").close()
print(generate_hashes("empty_file.txt"))

print("\n" + "=" * 50)
print("TEST 10 — file with special characters in name")
print("=" * 50)
with open("test file with spaces.txt", "w") as f:
    f.write("spaces in filename")
print(generate_hashes("test file with spaces.txt"))

# ============================================================
# SECTION 2 — check_hash edge cases
# ============================================================

print("\n" + "=" * 50)
print("TEST 11 — valid known malicious hash EICAR")
print("=" * 50)
print(check_hash("131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267"))

print("\n" + "=" * 50)
print("TEST 12 — unknown hash not in VirusTotal")
print("=" * 50)
print(check_hash("0" * 64))

print("\n" + "=" * 50)
print("TEST 13 — None as hash")
print("=" * 50)
print(check_hash(None))

print("\n" + "=" * 50)
print("TEST 14 — empty string as hash")
print("=" * 50)
print(check_hash(""))

print("\n" + "=" * 50)
print("TEST 15 — integer as hash")
print("=" * 50)
print(check_hash(12345))

print("\n" + "=" * 50)
print("TEST 16 — SQL injection as hash")
print("=" * 50)
print(check_hash("' OR '1'='1"))

print("\n" + "=" * 50)
print("TEST 17 — short invalid hash")
print("=" * 50)
print(check_hash("abc123"))

print("\n" + "=" * 50)
print("TEST 18 — MD5 hash instead of SHA256")
print("=" * 50)
print(check_hash("69630e4574ec6798239b091cda43dca0"))

print("\n" + "=" * 50)
print("TEST 19 — XSS attempt as hash")
print("=" * 50)
print(check_hash("<script>alert(1)</script>"))

print("\n" + "=" * 50)
print("TEST 20 — path traversal as hash")
print("=" * 50)
print(check_hash("../../etc/passwd"))

# ============================================================
# SECTION 3 — analyze_file edge cases
# ============================================================

print("\n" + "=" * 50)
print("TEST 21 — valid file")
print("=" * 50)
print(analyze_file("test_file.txt"))

print("\n" + "=" * 50)
print("TEST 22 — EICAR malicious file")
print("=" * 50)
print(analyze_file("eicar.txt"))

print("\n" + "=" * 50)
print("TEST 23 — None as filepath")
print("=" * 50)
print(analyze_file(None))

print("\n" + "=" * 50)
print("TEST 24 — nonexistent file")
print("=" * 50)
print(analyze_file("nonexistent.txt"))

print("\n" + "=" * 50)
print("TEST 25 — negative threshold")
print("=" * 50)
print(analyze_file("test_file.txt", threshold=-1))

print("\n" + "=" * 50)
print("TEST 26 — threshold of 0")
print("=" * 50)
print(analyze_file("test_file.txt", threshold=0))

print("\n" + "=" * 50)
print("TEST 27 — threshold of 1 on EICAR")
print("=" * 50)
print(analyze_file("eicar.txt", threshold=1))

print("\n" + "=" * 50)
print("TEST 28 — threshold of 9999 on EICAR")
print("=" * 50)
print(analyze_file("eicar.txt", threshold=9999))

print("\n" + "=" * 50)
print("TEST 29 — empty file")
print("=" * 50)
print(analyze_file("empty_file.txt"))

print("\n" + "=" * 50)
print("TEST 30 — boolean as threshold")
print("=" * 50)
print(analyze_file("test_file.txt", threshold=True))

# ============================================================
# SECTION 4 — generate_report edge cases
# ============================================================

print("\n" + "=" * 50)
print("TEST 31 — None as results")
print("=" * 50)
generate_report(None)

print("\n" + "=" * 50)
print("TEST 32 — empty results list")
print("=" * 50)
generate_report([])

print("\n" + "=" * 50)
print("TEST 33 — results with missing keys")
print("=" * 50)
generate_report([{"verdict": "MALICIOUS"}])

print("\n" + "=" * 50)
print("TEST 34 — full directory scan through main logic")
print("=" * 50)
results = []
for filename in os.listdir("test_folder"):
    filepath = os.path.join("test_folder", filename)
    if os.path.isfile(filepath):
        result = analyze_file(filepath)
        if result:
            results.append(result)
generate_report(results)

print("\n" + "=" * 50)
print("TEST 35 — cleanup temp files")
print("=" * 50)
os.remove("empty_file.txt")
os.remove("test file with spaces.txt")
print("Temp files cleaned up")