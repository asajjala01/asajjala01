```
┌──(abhi㉿security)-[~/certifications/google-cybersecurity]
└─$ cat course-01-foundations.md
```

# Course 1: Foundations of Cybersecurity

**Course:** Google Cybersecurity Certificate — Course 1 of 8  
**Status:** ✅ Completed

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)]()
[![Course](https://img.shields.io/badge/Course-1%20of%208-grey?style=flat)]()

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

## Common Attack Types

- **Phishing** — deceptive emails/messages to steal credentials or install malware
- **Malware** — malicious software (virus, worm, ransomware, spyware, trojan)
- **Social Engineering** — manipulating people rather than systems
- **Password Attack** — brute force, dictionary, credential stuffing
- **Physical Attack** — USB drops, tailgating, hardware theft
- **Supply Chain Attack** — compromising a vendor to reach the real target (e.g. SolarWinds)

---

## Security Frameworks

### NIST Cybersecurity Framework (CSF)
Five core functions:
1. **Identify** — understand your assets and risks
2. **Protect** — implement safeguards
3. **Detect** — identify when something goes wrong
4. **Respond** — take action on a detected incident
5. **Recover** — restore normal operations

### OWASP Principles
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

## What I Had to Do

The only portfolio activity in this course was drafting a **professional statement** — a short written piece that captures who you are, why you're entering cybersecurity, and what you bring to the field. At that point in the course it was more of a starting point than a finished product, something to revisit and refine as the program went on and my direction became clearer. It was a useful exercise though because it forced me to actually put into words why I was doing this, which isn't always easy when you're just getting started.

---

## My Take

Most of this course was relatively straightforward as an intro — the concepts weren't deeply technical and were designed to be accessible to someone with zero background, which I appreciated coming in cold. The CIA Triad, threat actors, attack types, NIST framework — all of it made intuitive sense pretty quickly and gave me a solid mental model to build on.

The one area where I had to slow down and put in extra time was the CISSP 8 domains. Not because any individual domain is complicated, but because there are eight of them covering completely different areas of security and understanding how they relate to each other took some work. I went through multiple resources — rewatching sections, looking things up separately, talking it through — before it really clicked as a cohesive picture rather than just a list to memorize. Once it did though it became a genuinely useful map for thinking about where different security roles and responsibilities fit.

Everything else in this course set the tone well. The threat actor motivation breakdown was one of the more interesting parts — understanding that a nation-state and a ransomware gang are operating with completely different goals changes how you think about attribution and intent when analyzing a threat.
