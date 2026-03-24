# Log File Analyzer

A Python based log file analyzer built as part of my cybersecurity learning journey.
This project was developed block by block with the help of Claude (Anthropic) as a
learning tool — breaking down each function line by line to understand the logic,
security implications, and real world relevance behind every decision. Through building
this project I learned how the basis of a SIEM (Security Information and Event
Management) system works — ingesting raw log data, parsing it into structured fields,
running detection rules against it, and generating alerts for a security analyst to
act on. Tools like Splunk, Microsoft Sentinel, and IBM QRadar do this exact workflow
at enterprise scale. The code was stress tested using test_analyzer.py with 30
aggressive inputs designed to break it, and reviewed to find additional edge cases
and potential breaking points.

## What it does

This tool reads a web server log file, parses each line into structured fields, runs
three detection rules against the parsed data, and generates a formatted SOC analyst
alert report. It detects brute force login attempts, unauthorized access probing, and
path traversal attacks — three of the most common attack patterns seen in real SOC
environments.

The analyzer is built across five functional blocks. Block 1 loads the regex, system,
collections, and datetime libraries that power the tool. Block 2 defines a
create_alert() helper function that standardizes the alert structure across all
detectors, and a parse_log_line() function that uses regular expressions to extract
six fields from each log line — IP address, timestamp, HTTP method, endpoint, status
code, and response size. Block 3 contains three detection functions — detect_brute_force()
which flags IPs with too many 401 failures, detect_admin_probe() which flags IPs
repeatedly hitting forbidden endpoints, and detect_path_traversal() which flags
requests containing suspicious patterns like ../  /etc/passwd and cmd.exe. Block 4
contains generate_report() which takes all collected alerts and prints a formatted
SOC analyst report with a header, per-alert detail, and a summary count. Block 5
contains main() which handles the command line argument, reads the log file, runs
all three detectors, and passes the results to the report generator.

## How the SIEM concept applies

A real SIEM like Splunk or Microsoft Sentinel follows the exact same pipeline we
built here. Raw log data comes in from servers, firewalls, and endpoints. The SIEM
parses each log line into structured fields. Detection rules run against those fields
looking for known attack patterns. Alerts fire when rules are triggered. Analysts
review and respond to those alerts. Our tool is a miniature version of that pipeline
built from scratch in Python, which means understanding this code gives you a direct
mental model of how enterprise security tooling works under the hood.

## Usage

Run the analyzer against any log file:
```bash
python analyzer.py sample.log
```

The tool will parse the log, run all three detectors, and print a full alert report.

## Sample output
```
[*] Parsed 21 log entries from sample.log

============================================================
       SOC ANALYST ALERT REPORT
============================================================
Log file analyzed: sample.log
Report generated:  2026-03-24 19:30:30
Total alerts:      5
============================================================

[!] ALERT — BRUTE FORCE
    IP Address : 10.0.0.5
    Detail     : 5 failed login attempts detected
    Timestamp  : 2026-03-24 19:30:30
------------------------------------------------------------

[!] ALERT — ADMIN PROBE
    IP Address : 192.168.1.3
    Detail     : 3 attempts to access restricted endpoints
    Timestamp  : 2026-03-24 19:30:30
------------------------------------------------------------

[!] ALERT — PATH TRAVERSAL
    IP Address : 10.0.0.9
    Detail     : Suspicious pattern '/etc/passwd' in endpoint /etc/passwd
    Timestamp  : 2026-03-24 19:30:30
------------------------------------------------------------

[*] Report complete. 5 alert(s) generated.
```

## Detection rules

The three detection rules mirror real SOC alert logic used in enterprise environments.

Brute force detection monitors for repeated 401 Unauthorized responses from the same
IP address. The default threshold is 5 failures before an alert fires. This threshold
is tunable — a bank might set it to 3, a low security internal tool might set it to 10.
Repeated authentication failures followed by a success is one of the clearest
indicators of a successful brute force attack.

Admin probe detection monitors for repeated 403 Forbidden responses from the same IP.
The default threshold is 3. A user accidentally hitting a restricted page once is
normal. Hitting it three or more times suggests deliberate probing for an admin panel
or restricted resource.

Path traversal detection fires on the first occurrence of any suspicious pattern in
the requested endpoint with no threshold needed. Patterns monitored include ../ and
..\ for directory traversal, /etc/passwd and /etc/shadow for Unix credential file
access, and cmd.exe for Windows command execution attempts. There is no legitimate
reason for a normal user to request any of these patterns so one occurrence is
enough to alert.

## What I learned

On the technical side I learned how regular expressions work to extract structured
data from unstructured text, how defaultdict makes counting operations cleaner than
regular dictionaries, how to build a standardized alert schema using a helper
function so all detection rules produce consistent output, and how the parse then
detect then report pipeline maps directly to how real SIEM tools are architected.

On the security side I learned that log analysis is one of the core daily
responsibilities of a tier 1 SOC analyst and that detection rules are just
conditional logic applied to structured log fields at scale. I learned the
difference between threshold based detection used for brute force and admin
probing versus signature based detection used for path traversal, and why each
approach suits different attack patterns. I also learned that log tampering is a
real anti-forensics technique and that a high number of unparseable log lines
could itself be a signal worth investigating.

## Known limitations

URL encoded traversal patterns like %2e%2e%2f which is the encoded form of ../
are not currently detected. A sophisticated attacker would encode their path
traversal attempt to bypass signature based detection. Extremely long endpoints
are accepted without a length limit which could cause memory issues at massive
scale. Null bytes in endpoints are stored rather than stripped which could affect
downstream processing. These are documented improvement areas for future versions.

## Testing

A separate test_analyzer.py file was written to stress test every function with
30 aggressive inputs designed to break the analyzer. Tests covered None and empty
string inputs to parse_log_line, malformed timestamps, SQL injection strings in
endpoints, extremely long endpoints, null bytes and unicode characters, None passed
to detection functions, zero and negative thresholds, string thresholds, boolean
thresholds, entries with missing keys and wrong data types, Windows style path
traversal, URL encoded traversal attempts, 1000 identical 401s from the same IP,
and 1000 alerts passed to the report generator simultaneously. Bugs found and
fixed during testing included a TypeError crash when None was passed to
parse_log_line fixed by adding isinstance string validation, a TypeError crash
when None was passed to detection functions fixed by adding isinstance list
validation, invalid thresholds including zero negative and boolean values being
accepted fixed by adding threshold validation, and entries with missing or None
keys crashing detection loops fixed by wrapping entry access in try except blocks.

## Development approach

This project was built with the assistance of Claude (Anthropic) as a learning
tool. Rather than copying and running the code, every block was broken down line
by line to understand the logic, the security implications, and the real world
relevance behind each decision. The most valuable insight from this project was
understanding how the basis of a SIEM works — the same parse, detect, and alert
pipeline we built here from scratch in Python is what enterprise tools like Splunk
and Microsoft Sentinel run at billions of events per day. Building it from the
ground up gave a direct mental model of what those tools are doing under the hood
and why each architectural decision was made the way it was.
