# Port Scanner

A TCP port scanner built in Python as part of my cybersecurity learning journey.
This project was developed block by block with the help of Claude as a
learning tool — breaking down each function line by line to understand the logic,
security implications, and real world relevance behind every decision. The code was
then stress tested using test_scanner.py, and reviewed by peers to find additional
edge cases and potential breaking points. The goal was not just to have a working
port scanner, but to deeply understand how TCP connections work, how attackers use
tools, and how defenders can detect and mitigate scanning activity.

## What it does

This tool attempts TCP connections across a range of ports on a target IP address
or hostname and reports which ports are open. It optionally grabs service banners
from open ports to identify software names and versions running on the target —
a technique used in real penetration testing called version fingerprinting.

The scanner is built across five functional blocks. Block 1 loads the socket,
threading, argument parsing, and datetime libraries that power the tool. Block 2
creates a TCP socket, attempts a connection to a single port, and returns the port
number if open or None if closed or filtered. Block 3 connects to an open port,
sends an HTTP HEAD request, and reads the server response to identify what software
is listening. Block 4 manages a thread pool of up to 100 concurrent workers that
call scan_port() simultaneously across the full port range, making the scan fast
enough to cover 1024 ports in under a second. Block 5 handles command line
arguments, resolves hostnames to IP addresses, orchestrates the scan, and prints
a timestamped summary.

## Usage

Basic scan across ports 1 to 1024:
```bash
python scanner.py scanme.nmap.org
```

Custom port range:
```bash
python scanner.py scanme.nmap.org -s 1 -e 500
```

Enable banner grabbing:
```bash
python scanner.py scanme.nmap.org -b
```

Full scan with all options:
```bash
python scanner.py scanme.nmap.org -s 1 -e 65535 -t 200 -b
```

| Flag | Long form | Description | Default |
|------|-----------|-------------|---------|
| | target | Target IP address or hostname | required |
| -s | --start | Start port | 1 |
| -e | --end | End port | 1024 |
| -t | --threads | Number of concurrent threads | 100 |
| -b | --banner | Enable banner grabbing | off |

## Sample output
```
[*] Scanning 45.33.32.156 — ports 1 to 1024
[*] Started at: 2026-03-23 20:45:44
--------------------------------------------------
  [+] Port 22 OPEN
  [+] Port 80 OPEN
[*] Grabbing banners...
  Port 22: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
  Port 80: HTTP/1.1 200 OK Date: Mon, 23 Mar 2026 20:48:20 GMT Server: Apache/2.4.7
[*] Scan complete. 2 open port(s) found.
[*] Finished at: 2026-03-23 20:45:44
```

## Port states

| State | Behavior | Security relevance |
|-------|----------|--------------------|
| Open | Completes TCP handshake | A service is actively listening — primary attack surface |
| Closed | Returns a TCP RST packet | Host is alive but nothing listening on that port |
| Filtered | No response, times out | Firewall is dropping packets — reveals less information |

## What I learned

On the technical side I learned how TCP sockets work at the OS level using
Python's socket library, the difference between connect() and connect_ex() and
why error codes are cleaner than exceptions in network scanning loops, how
threading with ThreadPoolExecutor dramatically reduces scan time by running
hundreds of connection attempts simultaneously, how service banners expose
software versions that can be cross referenced against CVE databases for
vulnerability assessment, and how argparse builds professional CLI interfaces
with built in help menus.

On the security side I learned that port scanning is one of the first steps in
real penetration testing and understanding it from both sides is fundamental to
SOC analyst work. A filtered port is more secure than a closed port because
silence reveals less information to an attacker than a TCP RST response. Banner
grabbing exposes version information that directly maps to known vulnerabilities
and disabling banners is a basic hardening step. Timestamps in scan output are
critical for forensic timeline analysis and incident response documentation.
Low and slow scanning mimics normal traffic to evade IDS detection and
understanding attacker evasion techniques helps defenders write better detection
rules.

## Testing

A separate test_scanner.py file was written to stress test every function with
20 different inputs including edge cases designed to break the scanner. Tests
included None and empty string as target, negative port numbers and ports above
65535, wrong data types as arguments such as floats lists and integers, SQL
injection strings as target input, zero threads and float thread counts, and
internal network ranges and localhost. Bugs found and fixed during testing
included a TypeError crash when passing None as target fixed by expanding the
except block, an OverflowError on negative ports fixed with port range
validation, a ValueError crash on 0 threads fixed with thread count validation,
and sloppy output when None was passed to run_scan fixed with an early return.
