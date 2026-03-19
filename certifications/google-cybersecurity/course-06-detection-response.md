```
┌──(abhi㉿security)-[~/certifications/google-cybersecurity]
└─$ cat course-06-detection-response.md
```

# Course 6: Sound the Alarm — Detection and Response

**Course:** Google Cybersecurity Certificate — Course 6 of 8  
**Status:** ✅ Completed

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)]()
[![Course](https://img.shields.io/badge/Course-6%20of%208-grey?style=flat)]()
[![Tools](https://img.shields.io/badge/Tools-Splunk%20%7C%20Chronicle%20%7C%20Wazuh-grey?style=flat)]()

---

## The Incident Response Lifecycle

Based on NIST SP 800-61:

```
1. Preparation
        ↓
2. Detection & Analysis
        ↓
3. Containment, Eradication & Recovery
        ↓
4. Post-Incident Activity
        ↑___________________________|
```

### 1. Preparation
- Build and train the incident response team
- Establish playbooks and communication procedures
- Harden systems and deploy detection tools

### 2. Detection & Analysis
- Monitor alerts from SIEM, IDS/IPS, endpoints
- Triage: is this a real incident or a false positive?
- Determine scope — what systems are affected?
- Document everything from the start

### 3. Containment, Eradication & Recovery
- **Containment** — isolate affected systems to stop spread
- **Eradication** — remove malware, close entry points, patch vulnerabilities
- **Recovery** — restore systems from clean backups, monitor closely

### 4. Post-Incident Activity
- Write a post-incident report
- Root cause analysis — how did this happen?
- Update playbooks and defenses
- Share lessons learned with the team

---

## Incident Triage

### Severity Levels
| Level | Description | Response Time |
|---|---|---|
| P1 – Critical | Active breach, data exfiltration, system down | Immediate |
| P2 – High | Likely compromise, spread possible | Within 1 hour |
| P3 – Medium | Suspicious activity, limited scope | Within 4 hours |
| P4 – Low | Policy violation, minor anomaly | Within 24 hours |

### True vs False Positives
- **True Positive** — real attack, alert is correct
- **False Positive** — not an attack, alert is wrong
- **True Negative** — no attack, no alert
- **False Negative** — real attack, no alert fired — the dangerous one

---

## Log Analysis

### Common Log Sources
| Source | What It Captures |
|---|---|
| Authentication logs | Login attempts, successes, failures |
| Firewall logs | Traffic allowed and denied |
| DNS logs | Domain lookups — can reveal malware C2 |
| Web server logs | HTTP requests, status codes, user agents |
| Endpoint logs | Process execution, file changes |
| Network flow logs | Who talked to who, when, how much data |

### What to Look For
```
Failed logins           → brute force attempt
Login at 3am            → unusual access time
Login from new country  → account compromise
DNS to unknown domain   → possible malware C2
Large outbound transfer → data exfiltration
New admin account       → persistence mechanism
```

### Log Analysis with grep
```bash
grep "Failed password" /var/log/auth.log
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn
grep "Accepted password" /var/log/auth.log
```

---

## SIEM

### How a SIEM Works
```
Log Sources → Collection → Normalization → Correlation Rules → Alerts → Analyst
```

### Splunk Basics
```
index=auth_logs "failed login"
| stats count by src_ip
| where count > 20
| sort -count

index=web_logs status=404
| timechart count span=1h
| where count > 100
```

### Tools Introduced
- **Splunk** — industry-leading SIEM with SPL (Search Processing Language)
- **Chronicle** — Google's cloud-native SIEM
- **Wazuh** — open-source SIEM and XDR platform

---

## Playbooks

A playbook is a documented, step-by-step procedure for handling a specific type of incident.

### Phishing Playbook (Example)
1. Analyst receives phishing alert from email gateway
2. Examine sender, subject, links, and attachments
3. Check if any users clicked the link
4. Isolate any affected endpoints
5. Reset credentials for affected users
6. Block the sender domain and malicious URL
7. Notify affected users
8. Document the incident and update filters

---

## Chain of Custody

- Document every piece of evidence collected
- Note who collected it, when, and how
- Store evidence in a secure, tamper-evident way
- Use hashing to verify evidence hasn't been modified

---

## What I Had to Do

This course had the richest set of activities in the entire certificate — a mix of technical hands-on work, investigation scenarios, and the most substantial portfolio deliverable so far.

**Activities:**

1. **Analyze my first packet** — opened a packet capture file and analyzed the traffic inside. First real exposure to looking at raw network data and understanding what the packets were actually saying — source, destination, protocol, payload.

2. **Research protocol analyzers** — explored the landscape of tools used for packet analysis, understanding when and why you'd use different analyzers depending on the scenario.

3. **Investigate a suspicious file hash** — given a file hash, use threat intelligence tools to look it up and determine whether it's associated with known malware. This is a core day-one SOC analyst skill — you get a hash, you look it up, you make a call.

4. **Use a playbook to respond to a phishing incident** — given a phishing alert scenario, follow the documented playbook step by step. Triage the alert, investigate the email, check for affected users, contain, document. This was the first time the playbook concept became real rather than theoretical.

5. **Review a final report** — given a completed incident report, analyze the findings, assess whether the response was handled correctly, and identify anything that should have been done differently.

6. **Perform a query with Wazuh** — hands-on with Wazuh, an open-source SIEM. Write queries to search through log data, filter for specific events, and identify anomalies. This was the first time I touched a real SIEM interface rather than just reading about how they work.

**Portfolio:**

1. **Document an incident with an incident handler's journal** — throughout the course, maintain a running journal documenting incidents as they came up in the scenarios. Each entry covers what happened, what actions were taken, what evidence was collected, and the outcome.

2. **Finalize the incident handler's journal** — at the end of the course, polish and complete the journal as a full deliverable. This was the portfolio piece that felt most like real SOC work — maintaining ongoing documentation across multiple incidents, written in a way that another analyst could pick up and understand exactly what happened.

---

## My Take

This was the course that changed everything for me. I absolutely loved it. The moment SIEM tools got introduced and I started actually looking at log files, correlating events, understanding what Splunk and Chronicle were doing under the hood — I felt it. That's the only way I can describe it. Something just locked in and I knew this was the direction I wanted to go.

There's something genuinely satisfying about looking at a sea of log data and being able to spot the thing that doesn't belong. The way SIEM tools surface patterns across thousands of events, the way a well-written detection rule can catch a brute force attempt in real time — I found that fascinating in a way I didn't expect going in. The Wazuh activity especially stood out — actually running queries in a live SIEM interface rather than just reading about it made the whole concept land differently.

The phishing playbook activity and the incident handler's journal were also highlights. Using a playbook to respond to an actual scenario step by step showed me how much of incident response is about process discipline — following the documented procedure calmly and completely rather than improvising. That's something my sales background actually prepared me for well.

This was also right around the time I discovered TryHackMe. I was doing research on how to go deeper with SIEM and log analysis and kept seeing it come up — and when I saw they had actual interactive lab environments where you could get hands-on with real tools, I was sold. That honestly lit a fire under me to finish the rest of the Google certificate as fast as I could so I could get over there and start doing the work in a more hands-on way. Best decision I made in this whole journey.
