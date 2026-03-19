# Course 5: Assets, Threats, and Vulnerabilities

**Course:** Google Cybersecurity Certificate — Course 5 of 8  
**Status:** ✅ Completed

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

Each state requires different protections.

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
- **CVE** (Common Vulnerabilities and Exposures) — a unique ID for each known vulnerability (e.g. CVE-2021-44228 = Log4Shell)
- **CVSS** (Common Vulnerability Scoring System) — score 0–10 rating severity

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

A structured way to identify what could go wrong before it does.

### PASTA Framework (Process for Attack Simulation and Threat Analysis)
1. Define objectives
2. Define technical scope
3. Decompose the application
4. Analyze threats
5. Identify vulnerabilities
6. Enumerate attacks
7. Perform risk/impact analysis

### Attack Surface
Everything exposed to a potential attacker:
- Web applications
- APIs
- Open ports and services
- Employee email accounts (phishing targets)
- Third-party vendors and integrations
- Physical access points

> **Principle of least privilege** reduces attack surface — users should only have access to exactly what they need.

---

## Social Engineering

Manipulating people rather than systems — often the easiest attack vector.

| Technique | Description |
|---|---|
| Phishing | Fraudulent emails to steal credentials or deploy malware |
| Spear phishing | Targeted phishing using personal info |
| Vishing | Voice phishing (phone calls) |
| Smishing | SMS phishing |
| Pretexting | Creating a fabricated scenario to extract info |
| Baiting | Leaving infected USB drives in public areas |
| Tailgating | Following someone through a secured door |
| Watering hole | Compromising a site the target is known to visit |

### Why Social Engineering Works
- Creates urgency or fear ("your account will be suspended")
- Exploits trust (impersonates IT, manager, or vendor)
- Leverages authority
- Takes advantage of helpfulness

---

## Encryption and Hashing Basics

### Encryption
Converts plaintext to ciphertext — reversible with a key.
- **Symmetric** — same key encrypts and decrypts (AES)
- **Asymmetric** — public key encrypts, private key decrypts (RSA, ECC)

### Hashing
One-way transformation — cannot be reversed.
- Used to store passwords safely
- Common algorithms: MD5 (weak), SHA-1 (weak), SHA-256, SHA-3, bcrypt

```
plaintext: "password123"
MD5 hash:  482c811da5d5b4bc6d497ffa98491e38  ← easily cracked
bcrypt:    $2b$12$...                         ← much stronger
```

> If you see MD5 or SHA-1 hashed passwords in an investigation — that's a finding.

---

## My Take

This course had more reading than any other in the certificate and some of it took me longer to absorb than I expected. Most of the content was manageable — asset classification, threat actors, social engineering — that stuff made intuitive sense pretty quickly. But there were two areas where I genuinely had to slow down and put in extra time.

The frameworks were the first one. PASTA, threat modeling methodology, understanding how to actually apply a framework to a real scenario rather than just memorizing what the letters stand for — that required more passes than I expected. The second was hashing. Encryption I got fairly quickly, but hashing — the one-way nature of it, why you can't reverse it, how it's used for password storage and integrity verification — took me a while to fully internalize. Once it clicked it made complete sense, but it wasn't instant.

Everything else in this course was solid and easier to work through. And looking back it's one of the more foundational courses for SOC work — understanding CVE scores, how to classify assets by sensitivity, why social engineering is often the scariest attack vector — all of that shapes how you think when you're actually investigating something. The hard parts were worth pushing through.
