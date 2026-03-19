```
┌──(abhi㉿security)-[~/certifications/google-cybersecurity]
└─$ cat course-05-assets-threats.md
```

# Course 5: Assets, Threats, and Vulnerabilities

**Course:** Google Cybersecurity Certificate — Course 5 of 8  
**Status:** ✅ Completed

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)]()
[![Course](https://img.shields.io/badge/Course-5%20of%208-grey?style=flat)]()

---

## Asset Management

Assets are anything of value to an organization that needs protecting — hardware, software, data, people, reputation.

### Asset Classification
| Level | Description | Examples |
|---|---|---|
| Restricted | Most sensitive — severe damage if exposed | PII, credentials, medical records |
| Confidential | Significant damage if exposed | Financial records, IP, internal strategies |
| Internal-only | Minor damage if exposed | Internal processes, org charts |
| Public | No damage if exposed | Marketing material, public website |

### Data States
- **Data at rest** — stored on disk, database, USB
- **Data in transit** — moving across a network
- **Data in use** — actively being processed in memory

---

## Vulnerability Management

### Vulnerability vs. Threat vs. Risk
```
Vulnerability = the weakness (unlocked door)
Threat        = the potential danger (burglar)
Risk          = likelihood × impact (how likely is the burglar, how bad is the outcome)
```

### Common Vulnerability Types
| Type | Description |
|---|---|
| Unpatched software | Known vulnerabilities that haven't been fixed |
| Misconfiguration | Default credentials, open ports, weak permissions |
| Injection flaws | SQL injection, command injection, XSS |
| Broken authentication | Weak passwords, no MFA, session issues |
| Insider threat | Trusted user misusing access |
| Zero-day | Unknown vulnerability with no patch |

### CVE and CVSS
- **CVE** — unique ID for each known vulnerability (e.g. CVE-2021-44228 = Log4Shell)
- **CVSS** — score 0–10 rating severity

| CVSS Score | Severity |
|---|---|
| 0.0 | None |
| 0.1–3.9 | Low |
| 4.0–6.9 | Medium |
| 7.0–8.9 | High |
| 9.0–10.0 | Critical |

> Always prioritize patching Critical and High CVEs first.

---

## Threat Modeling

### PASTA Framework
1. Define objectives
2. Define technical scope
3. Decompose the application
4. Analyze threats
5. Identify vulnerabilities
6. Enumerate attacks
7. Perform risk/impact analysis

### Attack Surface
- Web applications, APIs, open ports
- Employee email accounts (phishing targets)
- Third-party vendors and integrations
- Physical access points
- USB drives and removable media

---

## Social Engineering

| Technique | Description |
|---|---|
| Phishing | Fraudulent emails to steal credentials or deploy malware |
| Spear phishing | Targeted phishing using personal info |
| Vishing | Voice phishing (phone calls) |
| Smishing | SMS phishing |
| Pretexting | Fabricated scenario to extract info |
| Baiting | Infected USB drives left in public areas |
| Tailgating | Following someone through a secured door |
| Watering hole | Compromising a site the target is known to visit |

---

## Encryption and Hashing

### Encryption
Converts plaintext to ciphertext — reversible with a key.
- **Symmetric** — same key encrypts and decrypts (AES)
- **Asymmetric** — public key encrypts, private key decrypts (RSA, ECC)

### Hashing
One-way transformation — cannot be reversed.

```
plaintext: "password123"
MD5 hash:  482c811da5d5b4bc6d497ffa98491e38  ← easily cracked
bcrypt:    $2b$12$...                         ← much stronger
```

> MD5 and SHA-1 are considered weak — if you see these in an investigation, that's a finding.

---

## What I Had to Do

This course had the most hands-on activities of the certificate so far — eight in total plus a portfolio piece.

**Activities:**

1. **Classify assets connected to a home network** — given a home network scenario, identify every connected device and classify each asset by sensitivity level. A straightforward exercise but it reinforced how quickly an attack surface grows even in a simple environment.

2. **Score risks based on likelihood and severity** — given a set of vulnerabilities, assign risk scores using likelihood × impact. This is the practical application of the risk formula from earlier courses — putting numbers to actual scenarios.

3. **Determine data handling practices** — given an organization's data types, identify what handling procedures should apply to each based on classification — who can access it, how it should be stored, how it should be transmitted.

4. **Decrypt an encrypted message** — hands-on with symmetric encryption. Given an encrypted message and the key, decrypt it and document the process. This was where encryption stopped being abstract.

5. **Create hash values** — generate hashes for files and strings, compare them, and verify integrity. Understanding why hashes are used for integrity checking rather than encryption clicked during this activity.

6. **Improve AAA (Authentication, Authorization, Accounting) for a small business** — given a fictional small business with weak access controls, identify gaps and recommend improvements across all three AAA functions.

7. **Identify attack vectors of a USB drive** — analyze how a physical USB device can be used as an attack vector, identify the threat scenarios (baiting, HID attacks, data exfiltration), and recommend mitigations.

8. **Apply the PASTA threat model** — walk through all seven stages of PASTA against a given application scenario. This was the most involved activity in the course and the one that made the framework actually make sense — reading about PASTA is one thing, applying it step by step to a real scenario is another.

**Portfolio — Analyze a vulnerable system for a small business** — given a small business environment with documented assets and infrastructure, perform a vulnerability analysis. Identify what's exposed, classify the risk level of each finding, and produce a written report with recommendations. This was the most complete deliverable of the course — it pulled together asset classification, CVE/CVSS scoring, threat modeling, and written communication all in one.

---

## My Take

This course had more reading than any other in the certificate and some of it took me longer to absorb than I expected. Most of the content was manageable — asset classification, threat actors, social engineering — that stuff made intuitive sense pretty quickly. But there were two areas where I genuinely had to slow down and put in extra time.

The frameworks were the first one. PASTA especially — threat modeling methodology, understanding how to actually apply a framework to a real scenario rather than just memorizing what the letters stand for — that required more passes than I expected. The second was hashing. Encryption I got fairly quickly, but hashing — the one-way nature of it, why you can't reverse it, how it's used for password storage and integrity verification — took me a while to fully internalize. The activity where I had to actually create and compare hash values was what finally made it click. Once it did it made complete sense, but it wasn't instant.

Everything else in this course was solid and easier to work through. The USB attack vector activity was one I didn't expect to find interesting but actually did — it's easy to overlook physical attack surfaces when you're focused on network security, but a USB drive left in a parking lot is one of the oldest and most effective social engineering techniques out there. Good reminder that the human element is always part of the equation.
