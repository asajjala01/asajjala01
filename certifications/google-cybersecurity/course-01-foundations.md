# Course 1: Foundations of Cybersecurity

**Course:** Google Cybersecurity Certificate — Course 1 of 8  
**Status:** ✅ Completed

---

## The CIA Triad

The three core principles that guide all of security:

| Principle | Definition | Example Threat |
|---|---|---|
| **Confidentiality** | Only authorized people can access information | Data breach, credential theft |
| **Integrity** | Data is accurate and hasn't been tampered with | Man-in-the-middle attack, file corruption |
| **Availability** | Systems and data are accessible when needed | DDoS attack, ransomware |

> Every security decision maps back to protecting one or more of these three things.

---

## Security Domains (CISSP 8 Domains)

1. **Security and Risk Management** — policies, compliance, ethics
2. **Asset Security** — protecting data throughout its lifecycle
3. **Security Architecture and Engineering** — secure system design
4. **Communication and Network Security** — securing networks and transmissions
5. **Identity and Access Management (IAM)** — who can access what
6. **Security Assessment and Testing** — audits, pen testing, vulnerability scans
7. **Security Operations** — incident response, monitoring, forensics
8. **Software Development Security** — secure coding practices

---

## Types of Threat Actors

| Type | Motivation | Example |
|---|---|---|
| Nation-state | Espionage, disruption | APT groups |
| Criminal | Financial gain | Ransomware gangs |
| Hacktivist | Political / ideological | Anonymous-style groups |
| Insider threat | Revenge, financial, careless | Disgruntled employee |
| Script kiddie | Recognition, curiosity | Uses prebuilt tools |

---

## Common Attack Types (Intro Level)

- **Phishing** — deceptive emails/messages to steal credentials or install malware
- **Malware** — malicious software (virus, worm, ransomware, spyware, trojan)
- **Social Engineering** — manipulating people rather than systems
- **Password Attack** — brute force, dictionary, credential stuffing
- **Physical Attack** — USB drops, tailgating, hardware theft
- **Supply Chain Attack** — compromising a vendor to reach the real target (e.g. SolarWinds)

---

## Security Frameworks (Intro)

### NIST Cybersecurity Framework (CSF)
Five core functions:
1. **Identify** — understand your assets and risks
2. **Protect** — implement safeguards
3. **Detect** — identify when something goes wrong
4. **Respond** — take action on a detected incident
5. **Recover** — restore normal operations

### OWASP Principles (Intro)
- Minimize attack surface
- Least privilege
- Defense in depth
- Fail securely
- Separation of duties

---

## Key Vocabulary

| Term | Definition |
|---|---|
| Threat | Potential cause of harm to a system |
| Vulnerability | Weakness that a threat can exploit |
| Risk | Likelihood × Impact of a threat exploiting a vulnerability |
| Asset | Anything of value that needs protecting |
| Exploit | Code or technique that takes advantage of a vulnerability |
| Payload | The malicious part of an attack that executes on the target |
| Zero-day | A vulnerability with no patch yet available |
| IOC | Indicator of Compromise — evidence that an attack occurred |

---

## My Take

This was the course that set the tone for everything. Coming in with no background, I didn't really know what cybersecurity even looked like day to day — this gave me the first real framework to think about it. The CIA Triad sounds simple but it genuinely changes how you look at every security situation once it clicks. You stop thinking about threats as random and start asking "what are they actually after — confidentiality, integrity, or availability?"

What I found interesting here was the threat actor breakdown. I hadn't really thought about the fact that not everyone attacking a system has the same motivation — a nation-state is playing a completely different game than a ransomware gang. That context made the field feel a lot more real and a lot less abstract. The NIST framework was also a good early anchor — even if you don't fully understand every piece yet, having that Identify → Protect → Detect → Respond → Recover mental model makes everything else make more sense as you go.
