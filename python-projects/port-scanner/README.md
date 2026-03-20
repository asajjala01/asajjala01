# Port Scanner

A Python-based TCP port scanner built for educational purposes and cybersecurity portfolio development.

## What it does

This tool attempts TCP connections across a range of ports on a target IP address
and reports which ports are open, closed, or filtered. It is intended for use on
networks and systems you own or have explicit written permission to scan.

---

## Block 1 — Imports
```python
import socket
import concurrent.futures
import argparse
import sys
from datetime import datetime
```

### What each import does

- `socket` — core of the project. Provides direct access to the OS-level networking
  stack. Used to create TCP connections and probe ports.

- `concurrent.futures` — enables multi-threaded scanning. Without this, scanning
  65,535 ports sequentially at 1 second timeout each would take over 18 hours.
  Threading brings that down to seconds.

- `argparse` — handles command line arguments. Lets the user pass a target IP,
  port range, and options without modifying the source code.

- `sys` — used for clean program exits when something goes wrong, like an
  unresolvable hostname.

- `datetime` — timestamps the start and end of each scan. Critical for forensic
  documentation and audit trails in a professional security context.

---

## Block 2 — Core Scan Function
```python
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            return port
        return None

    except socket.error:
        return None
```

### Line by line

- `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` — creates a TCP socket
  using IPv4 addressing. AF_INET specifies the address family, SOCK_STREAM
  specifies TCP as the protocol.

- `sock.settimeout(1)` — limits the connection attempt to 1 second. Prevents
  threads from hanging indefinitely on filtered ports that return no response.

- `sock.connect_ex((target, port))` — attempts the TCP connection. Returns 0
  if the port is open, a non-zero error code if closed or filtered.

- `sock.close()` — releases the socket and its associated OS resources. Essential
  at scan scale to prevent file descriptor exhaustion.

- `if result == 0: return port` — returns the port number if open so the thread
  pool can collect and report it. Returns None otherwise.

- `try/except socket.error` — wraps the entire function so any network-level
  failure is caught cleanly without crashing the thread.

### Port states

| State    | Behavior                          | What it tells an attacker         |
|----------|-----------------------------------|-----------------------------------|
| Open     | Completes TCP handshake           | A service is listening here       |
| Closed   | Returns a TCP RST packet          | Host is alive, nothing listening  |
| Filtered | No response, times out            | A firewall is dropping packets    |

### Security notes

- This performs a full TCP connect scan. It completes the three-way handshake
  and will appear in connection logs on a monitored network.
- A SYN scan (half-open) is stealthier but requires raw socket privileges.
- Only use against systems you own or have written authorization to test.
