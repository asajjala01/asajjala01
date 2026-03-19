```
┌──(abhi㉿security)-[~/certifications/google-cybersecurity]
└─$ cat course-02-manage-risks.md
```

# Course 2: Play It Safe — Manage Security Risks

**Course:** Google Cybersecurity Certificate — Course 2 of 8  
**Status:** ✅ Completed

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)]()
[![Course](https://img.shields.io/badge/Course-2%20of%208-grey?style=flat)]()

---

## Security Frameworks and Controls

Frameworks give organizations a structured way to manage risk. Controls are the specific actions taken to reduce risk.

### NIST CSF (Cybersecurity Framework)

| Function | What It Means | Example Activity |
|---|---|---|
| Identify | Know your assets and risks | Asset inventory, risk assessments |
| Protect | Put safeguards in place | Firewalls, access controls, training |
| Detect | Monitor for threats | SIEM alerts, IDS/IPS |
| Respond | Handle incidents | Incident response playbooks |
| Recover | Restore operations | Backups, disaster recovery plans |

### NIST RMF (Risk Management Framework)
7-step process used heavily in government and regulated industries:
1. Prepare
2. Categorize
3. Select (controls)
4. Implement
5. Assess
6. Authorize
7. Monitor

---

## Security Controls

| Type | Purpose | Examples |
|---|---|---|
| **Administrative** | Policies and procedures | Acceptable use policy, training, hiring practices |
| **Technical** | Technology-based | Firewalls, encryption, MFA, IDS |
| **Physical** | Physical access | Locks, CCTV, badge readers, security guards |

---

## Security Audits

A security audit evaluates whether an organization's controls are working and whether they meet compliance requirements.

### Common Compliance Frameworks
| Framework | Industry |
|---|---|
| HIPAA | Healthcare |
| PCI-DSS | Payment card data |
| SOC 2 | Service organizations (cloud, SaaS) |
| GDPR | Any org handling EU citizen data |
| NIST 800-53 | US federal agencies |

---

## SIEM (Security Information and Event Management)

A SIEM tool collects and analyzes log data from across an organization to detect threats in real time.

### What SIEMs Do
- Aggregate logs from servers, firewalls, endpoints, apps
- Correlate events across multiple sources
- Generate alerts when suspicious patterns are detected
- Provide dashboards for security analysts

### Tools Introduced
- **Splunk** — industry-leading SIEM, powerful search language (SPL)
- **Chronicle** — Google's cloud-native SIEM

### Basic SIEM Use Case
```
Scenario: Multiple failed login attempts from the same IP

Log source: Authentication server
SIEM rule: Alert if >5 failed logins from one IP within 10 minutes
Action: Analyst reviews → confirms brute force → blocks IP
```

---

## Risk Management Vocabulary

| Term | Definition |
|---|---|
| Risk | Likelihood × Impact of a negative event |
| Threat | Something that could cause harm |
| Vulnerability | A weakness that could be exploited |
| Residual risk | Risk that remains after controls are applied |
| Risk appetite | How much risk an org is willing to accept |
| Mitigation | Reducing the likelihood or impact of a risk |
| Transference | Shifting risk to another party (e.g. cyber insurance) |
| Acceptance | Acknowledging a risk and choosing not to act |
| Avoidance | Eliminating the activity that creates the risk |

---

## What I Had to Do

The portfolio activity for this course was conducting a **security audit**. They walked through how to scope an audit, what controls to evaluate, and how to document findings against compliance frameworks. It was a structured exercise — given a fictional organization, assess what controls were in place, identify gaps, and write up the results. Coming from a sales background where process documentation was part of the job, the structure of it made sense to me even if the security-specific terminology was still new.

The course also covered **incident response playbooks** — essentially pre-written step-by-step procedures for handling specific types of incidents. The concept immediately made sense to me. A playbook in security is not that different from a sales process — you define the steps ahead of time so that when something happens you're not improvising under pressure.

---

## My Take

This course went deeper into CISSP than Course 1 did and honestly it was still a lot to process at that stage. Being brand new to the field, the eight domains across all those different areas of security — each one its own discipline — took time to sit with. I used multiple resources, rewatched sections, and had to let some of it marinate before it fully made sense. It's one of those things that gets clearer the more of the field you understand, so revisiting it after completing the certificate felt different than the first time through.

NIST, OWASP, common threats, risks, and vulnerabilities — that content was more accessible. Building on what Course 1 introduced, it started clicking into a coherent picture. The risk appetite concept was one that genuinely stuck with me — the idea that organizations make conscious decisions about how much risk they're willing to live with was something I hadn't really considered before.

SIEM being introduced here was a highlight. The moment Splunk showed up I knew it was going to be important and worth going deep on. Seeing how logs from across an entire environment get aggregated and correlated in real time — that's the work. That's what a SOC analyst is actually doing and this course gave me the first real look at it.
