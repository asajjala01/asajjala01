```
┌──(abhi㉿security)-[~/certifications/tryhackme-soc-level-1]
└─$ cat blue-team-introduction.md
```

# Blue Team Introduction

**Path:** TryHackMe — SOC Level 1  
**Module:** Blue Team Introduction  
**Status:** ✅ Completed

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)]()
[![Module](https://img.shields.io/badge/Module-Blue%20Team%20Introduction-212C42?style=flat&logo=tryhackme&logoColor=white)]()

---

## What This Module Covers

The opening module of SOC Level 1 — sets the stage for everything that follows. Before diving into tools and techniques, this module answers the fundamental question of what the blue team actually is, who's on it, and what they're defending against. The two core threat surfaces covered were humans as attack vectors and systems as attack vectors — which together make up the vast majority of how real attacks actually happen.

---

## Roles on the Blue Team

The blue team isn't just one job — it's a collection of roles that each focus on a different part of detection and defense. Understanding the landscape of who does what helped me see exactly where a SOC analyst sits and what the path forward looks like from there.

| Role | Responsibility |
|---|---|
| SOC Analyst (L1) | First line of defense — triage alerts, investigate, escalate |
| SOC Analyst (L2) | Deeper investigation, threat hunting, mentoring L1 |
| SOC Analyst (L3) | Advanced threat hunting, red team collaboration, incident lead |
| Incident Responder | Active breach response, containment, forensics |
| Threat Intelligence Analyst | Research threat actors, TTPs, and emerging threats |
| Digital Forensics Analyst | Evidence collection and analysis post-incident |
| Malware Analyst | Reverse engineer malicious code to understand behavior |
| Security Engineer | Build and maintain the tools and infrastructure the team uses |

The L1 → L2 → L3 → IR progression is the path I'm focused on. Each level builds on the last — you can't effectively triage what you don't understand, and you can't investigate deeply without first learning to triage well.

---

## Humans as Attack Vectors

One of the two main threat surfaces covered. The core message — technical controls only go so far. People are often the easiest way in.

**Why humans are targeted:**
- Can be manipulated through trust, urgency, and authority
- Often have legitimate access to exactly what attackers want
- Security awareness varies widely across an organization
- One click on a phishing email can bypass millions of dollars of technical controls

**Common human-focused attack techniques:**
- **Phishing** — fraudulent emails designed to steal credentials or deliver malware
- **Spear phishing** — targeted phishing using personal or company-specific details
- **Vishing** — voice-based social engineering over the phone
- **Pretexting** — building a fabricated scenario to manipulate someone into giving up information
- **Insider threat** — malicious or negligent actions by someone with legitimate access

**Blue team response:**
- Security awareness training programs
- Phishing simulations to test and educate staff
- Email filtering and sandboxing
- Monitoring for unusual user behavior (UEBA)
- Clear reporting procedures when something suspicious occurs

---

## Systems as Attack Vectors

The second major threat surface — the technical side. Where humans are the softer target, systems are the ones with exploitable vulnerabilities that attackers probe constantly.

**Common system-focused attack techniques:**
- **Unpatched vulnerabilities** — software with known CVEs that haven't been patched
- **Misconfigured services** — default credentials, open ports, overly permissive firewall rules
- **Weak authentication** — no MFA, reused passwords, weak password policies
- **Exposed attack surface** — unnecessary services running, public-facing systems without adequate protection
- **Supply chain attacks** — compromising a trusted vendor or software update to reach the real target

**Blue team response:**
- Vulnerability scanning and patch management
- Asset inventory — you can't protect what you don't know you have
- Hardening configurations and closing unnecessary attack surface
- Network segmentation to limit lateral movement
- Continuous monitoring of systems for anomalous behavior

---

## The Labs

This module included introductory labs that gave a first look at some of the scenarios a SOC analyst encounters. Nothing deeply technical at this stage — more about building the right mental model before the heavier tool-focused modules. The labs walked through identifying attack vectors in given scenarios, understanding how an attacker might approach a target, and thinking through what the defensive response should look like.

It was a good warm-up. Enough to get your head in the right place before the real work starts in the modules that follow.

---

## My Take

This was a solid opening module and exactly the right way to start a SOC-focused path. By the time I got here I already had context on most of the concepts — phishing, social engineering, CVEs, misconfiguration — from the Google cert and TryHackMe Pre-Security. But having it all framed specifically around blue team roles and responsibilities made it land differently.

The roles breakdown was particularly useful. I'd heard terms like threat intelligence analyst and malware analyst before but seeing them mapped out as distinct roles within the same team — with clear responsibilities and a natural progression between them — gave me a much clearer picture of the field I'm stepping into. It also reinforced why I'm starting at L1 rather than jumping ahead. The foundation matters.

The humans vs systems framing is something I'll carry through the rest of this path. Every alert, every investigation, every incident ultimately traces back to one of those two surfaces. Keeping that mental model in place makes it easier to think through how an attack unfolded and where the gaps were.
