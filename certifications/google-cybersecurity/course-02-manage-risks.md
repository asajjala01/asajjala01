# Course 2: Play It Safe — Manage Security Risks

**Course:** Google Cybersecurity Certificate — Course 2 of 8  
**Status:** ✅ Completed

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

Three categories:

| Type | Purpose | Examples |
|---|---|---|
| **Administrative** | Policies and procedures | Acceptable use policy, training, hiring practices |
| **Technical** | Technology-based | Firewalls, encryption, MFA, IDS |
| **Physical** | Physical access | Locks, CCTV, badge readers, security guards |

---

## Security Audits

A security audit evaluates whether an organization's controls are working and whether they meet compliance requirements.

### Audit Scope
- What systems / departments are included
- What regulations apply (HIPAA, PCI-DSS, SOC2, etc.)

### Audit Goals
- Identify gaps in security posture
- Ensure compliance
- Improve security controls

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

### Basic SIEM Use Case Example
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

## My Take

This course is where things started feeling more real to me. Course 1 was about understanding the landscape — this one was about understanding how organizations actually respond to risk, and that shift in perspective was interesting. Like, you start realizing that security isn't just about blocking attacks, it's about making calculated decisions about what risks to accept, what to mitigate, and what to transfer. That risk appetite concept hit different — I hadn't thought about the fact that companies consciously decide how much risk they're willing to live with.

The framework vs. control distinction tripped me up at first too. I kept mixing them up until it clicked — a framework is the strategy, controls are the actual actions you take inside that strategy. Once that landed everything else made more sense.

SIEM was introduced here and honestly I got excited about it immediately. The idea that you can aggregate logs from across an entire environment and run correlation rules against all of it in real time — that's exactly the kind of work I wanted to be doing. Splunk showed up here and I knew right away it was something worth going deep on. The compliance piece was also good context — understanding that compliance sets the floor, not the ceiling, is something a lot of people outside security don't realize.
