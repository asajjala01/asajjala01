# Python Projects

A collection of security-focused Python scripts and tools built alongside my cybersecurity learning path. Everything in this folder was built with a purpose — each script exists because it solves a real security problem, reinforces a concept I was studying, or gave me hands-on experience with something I'd only read about.

---

## The Approach

I have a background in Python going back to college coursework and more recently the 100 Days of Code bootcamp, so the language itself isn't new to me. What is new is applying it specifically to security work — and that reframing has been one of the most valuable parts of this journey.

Rather than uploading generic course projects, I made a decision early on to only document Python work here that has a meaningful security angle. Every file in this folder came from asking the question — does this actually help me understand something about how attackers think, how defenders work, or how security tools operate under the hood? If the answer was no, it didn't make the cut.

Each script includes a header that explains what it does, why I built it, what I learned, and what resources I used. The code is the output — the header is the story behind it.

---

## Projects

### Network & Scanning
| Script | Description | Concepts |
|---|---|---|
| [port-scanner.py](./port-scanner.py) | Scan a target host for open TCP ports | Sockets, threading, error handling |

### Log Analysis & Parsing
| Script | Description | Concepts |
|---|---|---|
| [log-parser.py](./log-parser.py) | Parse and filter authentication log files | File I/O, regex, string parsing |

### Password & Credential Security
| Script | Description | Concepts |
|---|---|---|
| [password-checker.py](./password-checker.py) | Evaluate password strength against common criteria | Regex, string operations |
| [hash-identifier.py](./hash-identifier.py) | Identify common hash types by pattern | Pattern matching, conditionals |

---

## Running Any Script

Open your terminal and navigate to this folder:

```bash
cd python-projects
python3 script-name.py
```

All scripts are built using the Python standard library unless stated otherwise in the file header. No installs needed to get started.

---

## What's Coming

This folder will keep growing as I work through TryHackMe rooms, CTF challenges, and the SOC analyst path. Any time a concept clicks better by building it than by reading about it — it ends up here.
