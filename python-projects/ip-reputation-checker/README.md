# IP Reputation Checker

A Python based IP reputation checker built as part of my cybersecurity learning
journey. This project was developed block by block with the help of Claude
(Anthropic) as a learning tool — breaking down each function line by line to
understand the logic, security implications, and real world relevance behind every
decision. This project introduced me to API integration for the first time, which
came with its own set of challenges and learning moments. The code was stress tested
using test_checker.py with 26 aggressive inputs designed to break it, and iterated
on multiple times to fix bugs found during testing.

## What it does

This tool takes a list of IP addresses, checks each one against the AbuseIPDB
threat intelligence API, and generates a formatted triage report categorizing each
IP as clean, suspicious, or malicious based on its abuse confidence score. It is
designed to replicate the IP triage workflow a SOC analyst performs during alert
investigation — instead of manually looking up each IP, the tool automates the
entire process in seconds.

## How it works

The checker is built across six functional blocks. Block 1 loads the requests,
json, os, sys, dotenv, and datetime libraries. Block 2 loads the API key securely
from a .env file using python-dotenv and defines the AbuseIPDB API endpoint URL.
Block 3 contains check_ip() which sends a single IP to the AbuseIPDB API, receives
a JSON response, and extracts six fields — IP address, abuse confidence score,
country, ISP, total reports, and last reported date — into a clean dictionary.
Block 4 contains check_multiple_ips() which loops through a list of IPs,
deduplicates them to avoid wasting API requests, calls check_ip() on each one, and
sorts results into three risk buckets — clean, suspicious, and malicious — based on
a tunable threshold. Block 5 contains generate_report() which takes the categorized
results and prints a formatted triage report with malicious IPs first, suspicious
second, and clean last — priority based ordering so the most critical information
is always at the top. Block 6 contains main() which handles command line input,
supports both single IP lookup and batch file mode, and orchestrates the full
pipeline from input to report.

## API integration

This was my first time integrating a third party API into a Python project. The
AbuseIPDB API requires an API key for authentication which is passed in the request
headers alongside an Accept header telling the server to respond in JSON format.
The actual IP being checked is passed as a query parameter. The API responds with
a JSON object containing reputation data for the requested IP including an abuse
confidence score from 0 to 100, where 0 means clean and 100 means the IP has been
repeatedly reported as malicious by multiple organizations.

API keys are sensitive credentials and should never be committed to GitHub. This
project uses a .env file to store the API key locally and a .gitignore file to
prevent it from ever being pushed to the repository. The python-dotenv library
loads the key into the environment at runtime so the script can access it securely
without ever hardcoding it in the source code.

## Usage

Check a single IP:
```bash
python checker.py 8.8.8.8
```

Check a list of IPs from a file:
```bash
python checker.py ips.txt
```

The IP file should contain one IP address per line. The tool supports both IPv4
and IPv6 addresses.

## Sample output
```
[*] Reading IPs from file: ips.txt
[*] Checking 8.8.8.8 (1/5)
[*] Checking 185.220.101.45 (2/5)
[*] Checking 89.248.167.131 (3/5)

============================================================
       IP REPUTATION TRIAGE REPORT
============================================================
Report generated:  2026-03-25 04:34:21
Total IPs checked: 5
Clean:             3
Suspicious:        0
Malicious:         2
============================================================

[!!!] MALICIOUS IPs
------------------------------------------------------------
  IP           : 185.220.101.45
  Abuse Score  : 100/100
  Country      : DE
  ISP          : Network for Tor-Exit traffic.
  Total Reports: 96
  Last Reported: 2026-03-25T00:40:16+00:00
------------------------------------------------------------
  IP           : 89.248.167.131
  Abuse Score  : 100/100
  Country      : NL
  ISP          : FiberXpress BV
  Total Reports: 7535
  Last Reported: 2026-03-25T04:27:30+00:00
------------------------------------------------------------

[*] CLEAN IPs
------------------------------------------------------------
  IP           : 8.8.8.8
  Abuse Score  : 0/100
  Country      : US
  ISP          : Google LLC
------------------------------------------------------------

[*] Triage complete. 2 malicious, 0 suspicious, 3 clean.
```

## Risk categorization

The tool sorts IPs into three tiers which map directly to how SOC teams prioritize
their work. Clean means a score of 0 and requires no action. Suspicious means a
score between 1 and the threshold and requires further investigation and potential
escalation. Malicious means a score at or above the threshold and requires immediate
action — block the IP at the firewall, open an incident ticket, and notify the team.

The default threshold is 50 but it is tunable based on the organization's risk
tolerance. A high security environment might lower it to 25 to catch more borderline
cases. A more relaxed environment might raise it to 75. This threshold concept maps
directly to severity scoring in enterprise SIEM tools.

## Mistakes and learning moments

This project had more trial and error than the previous two and that was part of
the learning.

The first major issue was the API key not loading from the .env file after a
Codespace session reset. When a GitHub Codespace restarts it wipes installed
packages and environment variables. The fix was creating a requirements.txt file
so dependencies can be reinstalled with one command, and recreating the .env file
after each session reset. This taught me why production environments use secrets
managers and persistent environment configuration rather than local .env files.

The second issue was a missing sys import. The main function used sys.argv to read
command line arguments but sys was never added to the imports at the top of the
file. The script crashed immediately on startup with a NameError. A simple fix but
a good reminder to always verify every import is present before running.

The third issue was None and invalid inputs reaching the API and burning request
quota with 422 errors. The initial code sent everything directly to AbuseIPDB
without validating inputs first. After testing we added isinstance string validation
to check_ip() so None, integers, empty strings, and whitespace are rejected before
touching the API. This saved wasted requests and made error messages cleaner.

The fourth issue was duplicate IPs in the input list each burning a separate API
request. If a log file contained the same suspicious IP fifty times the tool would
check it fifty times and consume fifty requests from the daily limit. The fix was
adding a deduplication step using a set to track seen IPs before the main loop.

The fifth issue was private and special purpose IPs returning None for country and
ISP fields because AbuseIPDB has no geographic data for RFC 1918 private ranges,
localhost, and broadcast addresses. The report was printing None which looked
unprofessional. The fix was using Python's or operator to substitute Unknown as
a default value when the API returns None for those fields.

## Testing

A separate test_checker.py file was written to stress test every function with
26 aggressive inputs. Tests covered known clean IPs like Google DNS and Cloudflare,
known malicious IPs with scores of 100, private network ranges, localhost, broadcast
addresses, all zeros, IPv6 addresses, invalid IPs like 999.999.999.999 and
256.256.256.256, non-IP strings, SQL injection attempts, XSS payloads, path
traversal strings, JavaScript injection, the string NULL, None as input, empty
strings, integers, whitespace only strings, duplicate IPs, None as the ip_list,
empty lists, lists containing None values, mixed valid and invalid inputs, negative
thresholds, threshold of zero, threshold above the maximum possible score of 100,
and a full run against the complete aggressive test file.

Bugs found and fixed during testing included a TypeError crash when None was passed
to check_multiple_ips fixed by adding isinstance list validation, invalid inputs
reaching the API and returning 422 errors fixed by adding string validation to
check_ip before the request is made, duplicate IPs burning multiple API requests
fixed by deduplicating the list before scanning, and None country and ISP values
displaying in the report fixed by substituting Unknown as a default value.

## Known limitations

Invalid IP formats like 999.999.999.999 and non-IP strings still reach the API
and return 422 errors rather than being caught locally first. A regex based IP
format validator added before the API call would eliminate these wasted requests
entirely. The daily free tier limit of 1000 requests resets every 24 hours — large
IP lists should be run in batches to avoid hitting the limit. A threshold above 100
causes all IPs to be categorized as suspicious since the maximum possible score is
100 and nothing can reach the malicious bucket.

## What I learned

On the technical side I learned how to authenticate with a third party API using
request headers, how to pass query parameters with the requests library, how JSON
responses are structured and how to parse them into Python dictionaries, how to
protect sensitive credentials using .env files and .gitignore, how to handle
multiple HTTP status codes including 200 success, 422 unprocessable entity, and
429 rate limit, and how deduplication using a set prevents redundant API calls.

On the security side I learned that IP reputation checking is one of the first
triage steps a SOC analyst performs after an alert fires, that threat intelligence
APIs like AbuseIPDB aggregate reports from thousands of organizations to build a
constantly updated picture of malicious infrastructure, that a three tier
categorization system of clean suspicious and malicious maps directly to how SOC
teams prioritize their workload and avoid alert fatigue, and that protecting API
keys from version control is a fundamental security practice because exposed keys
can be scraped from GitHub and abused within minutes of being published.

## Development approach

This project was built with the assistance of Claude (Anthropic) as a learning
tool. It was my first time working with APIs in Python and it came with real
challenges — session resets wiping my environment, missing imports causing crashes
on startup, invalid inputs burning API quota, and duplicate IPs wasting requests.
Each bug was found through aggressive testing with 26 different inputs designed to
break the tool, and each fix was understood before being applied rather than just
copied in. The most valuable insight from this project was understanding how threat
intelligence APIs work and how automating IP lookups replicates the manual triage
workflow SOC analysts perform dozens of times per shift.
