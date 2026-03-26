# File Hash Checker

A Python based file hash checker built as part of my cybersecurity learning journey.
This project was developed block by block with the help of Claude (Anthropic) as a
learning tool — breaking down each function line by line to understand the logic,
security implications, and real world relevance behind every decision. This was my
second project using API integration and introduced me to a completely different
area of SOC work — static file analysis. Rather than analyzing network traffic or
log files, this tool analyzes files themselves by generating cryptographic
fingerprints and checking them against a global threat intelligence database. The
code was stress tested using test_checker.py with 35 aggressive inputs designed to
break it, and iterated on multiple times to fix bugs found during testing.

## What it does

This tool takes one or more files, generates MD5 SHA1 and SHA256 hashes for each
one, submits those hashes to the VirusTotal API, and generates a formatted triage
report showing which files are clean, suspicious, or malicious based on how many
antivirus engines flagged them. It supports both single file analysis and full
directory scanning — meaning you can point it at an entire folder and it will
automatically analyze every file inside it. This directly replicates the static
analysis workflow a SOC analyst performs when a suspicious file appears on a
quarantined endpoint.

## How it works

The checker is built across seven functional blocks. Block 1 loads the hashlib,
requests, os, sys, dotenv, and datetime libraries. Block 2 loads the VirusTotal
API key securely from a .env file and defines the API endpoint URL. Block 3
contains generate_hashes() which reads a file in chunks of 8192 bytes and feeds
each chunk through three hashing algorithms simultaneously to produce MD5 SHA1
and SHA256 fingerprints. Block 4 contains check_hash() which validates the hash
format locally then submits it to VirusTotal and returns detection results from
up to 76 antivirus engines. Block 5 contains analyze_file() which ties hashing
and lookup together into a single function and assigns a verdict of clean
suspicious or malicious based on a tunable detection threshold. Block 6 contains
generate_report() which takes all results and prints a priority based triage
report with malicious files first. Block 7 contains main() which handles command
line input, supports both single file and directory mode, and orchestrates the
full pipeline.

## Understanding file hashes

A hash is a fixed length fingerprint generated from a file's contents. No matter
how large the file is, running it through a hashing algorithm always produces a
short fixed length string. The same file always produces the same hash, and even
a single character change produces a completely different hash. This makes hashes
perfect identifiers for files without needing to store or transmit the file itself.

In cybersecurity this property is used for malware identification. Security
researchers maintain databases of known malicious file hashes. When a suspicious
file appears on a system, instead of executing it and seeing what it does — which
could infect the machine — analysts hash it and look up that hash in the database.
If it matches a known malware sample the answer is immediate without ever running
the file. This is called static analysis.

We generate three hash types per file because different threat intelligence
databases index by different algorithms. Older systems use MD5, newer ones prefer
SHA256. Generating all three maximizes the chance of finding a match in any
database queried. SHA256 is sent to VirusTotal specifically because it is the most
collision resistant — meaning two different files are extremely unlikely to produce
the same SHA256 hash, making it the most reliable identifier.

## Reading files in chunks

One of the key technical concepts learned in this project was why files are read
in chunks of 8192 bytes at a time rather than all at once. If a file is read
entirely into memory with a single read() call, a large file like a 10GB malware
sample would consume 10GB of RAM immediately. With chunked reading the memory
usage stays flat at 8KB regardless of file size because only one chunk is in
memory at any given time.

The analogy that made this click was thinking about how network packets work —
data is never sent all at once across a network, it gets broken into small pieces
and reassembled at the destination. Chunked file reading follows the same principle.
The 8192 byte chunk size aligns with how most operating systems handle disk reads
at the block level, making it efficient without being so small that it requires
too many read operations.

The three hash objects — md5, sha1, and sha256 — all run simultaneously on the
same chunks. Each call to update() feeds the next piece of the file into the
running hash calculation. By the time the loop finishes, all three hashers have
processed the entire file and hexdigest() finalizes each one into a readable
hex string.

## What is VirusTotal

VirusTotal is a free threat intelligence service owned by Google that scans file
hashes against over 70 antivirus engines simultaneously. Submitting a hash returns
detection results from all engines showing how many flagged it as malicious, what
malware family it belongs to, and when it was first seen in the wild. It is one
of the most widely used tools in SOC and malware analysis work. The free tier
allows 500 lookups per day which resets every 24 hours.

## The EICAR test file

During testing we used the EICAR standard antivirus test file — a special string
recognized by every major antivirus engine as a test signature. It is not real
malware but produces a consistent result of 63 out of 76 engines flagging it as
malicious on VirusTotal. This was used to verify the full pipeline was working
correctly — from hash generation through API lookup to malicious verdict — without
using actual malware samples.

## Usage

Analyze a single file:
```bash
python checker.py suspicious.exe
```

Analyze an entire directory:
```bash
python checker.py /path/to/folder
```

## Sample output
```
[*] Found 1 file(s) to analyze
[*] Analyzing: eicar.txt
    MD5:    69630e4574ec6798239b091cda43dca0
    SHA1:   cf8bd9dfddff007f75adf4c2be48005cea317c62
    SHA256: 131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267
[*] Checking VirusTotal...

============================================================
       FILE HASH TRIAGE REPORT
============================================================
Report generated:  2026-03-25 23:11:12
Total files:       1
Malicious:         1
Suspicious:        0
Clean:             0
============================================================

[!!!] MALICIOUS FILES
------------------------------------------------------------
  File           : eicar.txt
  Name           : eicar.txt
  MD5            : 69630e4574ec6798239b091cda43dca0
  SHA1           : cf8bd9dfddff007f75adf4c2be48005cea317c62
  SHA256         : 131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267
  Malicious      : 63/76 engines
  Suspicious     : 0/76 engines
------------------------------------------------------------

[*] Analysis complete. 1 malicious, 0 suspicious, 0 clean.
```

## Mistakes and learning moments

The first issue was hash validation — invalid inputs like SQL injection strings,
XSS payloads, path traversal attempts, and short strings were all being sent
directly to VirusTotal which accepted them as requests and returned 404 not found.
This was burning API quota on invalid inputs. The fix was adding local hash format
validation before any API call — valid hashes must be hex strings of exactly 32
characters for MD5, 40 for SHA1, or 64 for SHA256. Anything else gets rejected
locally without touching the API.

The second issue was analyze_file() printing the filepath before validating it.
Passing None as a filepath would print [*] Analyzing: None before the validation
caught it. The fix was moving the validation check above the print statement so
invalid inputs are rejected silently before any output is produced.

The third issue was generate_report() crashing with a KeyError when results had
missing fields. A result dictionary with only a verdict key and no filepath, name,
or hash fields would crash the entire report. The fix was replacing direct bracket
access with .get() which returns a default value of Unknown instead of crashing
when a key is missing.

## Testing

A separate test_checker.py file was written to stress test every function with
35 aggressive inputs across four sections. Section 1 tested generate_hashes() with
a valid file, nonexistent file, None, empty string, integer, directory passed as
filepath, whitespace, path traversal attempt, empty file, and file with spaces in
the name. Section 2 tested check_hash() with a known malicious EICAR hash, unknown
hash, None, empty string, integer, SQL injection, short invalid hash, MD5 hash
instead of SHA256, XSS payload, and path traversal string. Section 3 tested
analyze_file() with valid files, the EICAR malicious file, None filepath,
nonexistent file, negative threshold, zero threshold, threshold of 1, threshold
of 9999, empty file, and boolean as threshold. Section 4 tested generate_report()
with None, empty list, results with missing keys, and a full directory scan.

Bugs found and fixed during testing included invalid hashes reaching the API and
burning quota fixed by adding hex format and length validation locally, None
filepath printing before validation fixed by reordering the validation check,
and KeyError crashes on missing result fields fixed by replacing bracket access
with .get() and default values throughout generate_report().

## Known limitations

A threshold above the maximum number of engines — currently 76 on VirusTotal —
means nothing can ever reach the malicious verdict since the detection count can
never exceed the number of engines. Files not previously submitted to VirusTotal
return not found with zero engines checked, which means brand new malware that
has never been analyzed would appear clean. This is a fundamental limitation of
hash based detection and is why behavioral analysis exists as a complementary
technique. The free tier limit of 500 lookups per day resets every 24 hours.

## What I learned

On the technical side I learned how cryptographic hashing works and why the same
file always produces the same hash regardless of its name or location, why three
hash types are generated simultaneously to maximize database coverage, how chunked
file reading keeps memory usage flat regardless of file size using the same
principle as network packet fragmentation, how VirusTotal's API differs from
AbuseIPDB in authentication method and URL structure using path based routing
instead of query parameters, and how hash format validation locally before API
calls prevents wasted quota and improves tool reliability.

On the security side I learned that static analysis through hash lookup is one of
the fastest and safest ways to triage a suspicious file without executing it, that
VirusTotal's 70 plus engine coverage gives analysts immediate consensus from the
global security community rather than relying on a single vendor, that a file not
found result does not mean clean — it means unknown, which is itself a signal worth
investigating, and that directory scanning capability matters in incident response
because analysts often need to triage entire quarantined folders rather than
individual files.

## Development approach

This project was built with the assistance of Claude (Anthropic) as a learning
tool. Every block was broken down to understand the logic and security relevance
behind each decision. The chunked file reading concept was the most technically
interesting part of this project — understanding why files are processed in 8192
byte pieces rather than all at once came from drawing the parallel to how network
packets work, which made the concept immediately intuitive. The 35 test aggressive
suite found three real bugs that were fixed before the final version, and each fix
was understood before being applied.