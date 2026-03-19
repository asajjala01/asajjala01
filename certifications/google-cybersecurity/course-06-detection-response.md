# Course 6: Sound the Alarm — Detection and Response

**Course:** Google Cybersecurity Certificate — Course 6 of 8  
**Status:** ✅ Completed

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

Not every alert is an incident. Triage determines priority.

### Severity Levels (Common Framework)
| Level | Description | Response Time |
|---|---|---|
| P1 – Critical | Active breach, data exfiltration, system down | Immediate |
| P2 – High | Likely compromise, spread possible | Within 1 hour |
| P3 – Medium | Suspicious activity, limited scope | Within 4 hours |
| P4 – Low | Policy violation, minor anomaly | Within 24 hours |

### False Positive vs True Positive
- **True Positive** — real attack, alert is correct
- **False Positive** — not an attack, alert is wrong (adjust detection rules)
- **True Negative** — no attack, no alert (good)
- **False Negative** — real attack, no alert fired (dangerous — tune detection)

---

## Log Analysis

Logs are the primary evidence source in incident response.

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
# Find all failed SSH logins
grep "Failed password" /var/log/auth.log

# Count failures per IP
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn

# Find successful logins after multiple failures (potential brute force success)
grep "Accepted password" /var/log/auth.log
```

---

## SIEM Deep Dive

### How a SIEM Works
```
Log Sources → Collection → Normalization → Correlation Rules → Alerts → Analyst
```

1. Logs are collected from across the environment
2. Normalized into a common format
3. Correlation rules run against combined data
4. Alerts fire when patterns match
5. Analyst investigates and responds

### Splunk Basics
```
Search Processing Language (SPL) examples:

index=auth_logs "failed login"
| stats count by src_ip
| where count > 20
| sort -count

index=web_logs status=404
| timechart count span=1h
| where count > 100
```

### Alert Types
- **Threshold** — alert when a count exceeds a number (>10 failed logins)
- **Anomaly** — alert when behavior deviates from baseline
- **Signature** — alert when known attack pattern is detected

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

### Why Playbooks Matter
- Ensure consistent response regardless of who's on shift
- Reduce response time — no need to improvise
- Required for compliance in many regulated industries

---

## Chain of Custody

In incident response, maintaining evidence integrity is critical — especially if legal action follows.

- Document every piece of evidence collected
- Note who collected it, when, and how
- Store evidence in a secure, tamper-evident way
- Use hashing to verify evidence hasn't been modified

---

## My Take

This was the course that changed everything for me. I absolutely loved it. The moment SIEM tools got introduced and I started actually looking at log files, correlating events, understanding what Splunk and Chronicle were doing under the hood — I felt it. That's the only way I can describe it. Something just locked in and I knew this was the direction I wanted to go.

There's something genuinely satisfying about looking at a sea of log data and being able to spot the thing that doesn't belong. The way SIEM tools surface patterns across thousands of events, the way a well-written detection rule can catch a brute force attempt in real time — I found that fascinating in a way that I didn't expect going in. The tools introduced here made the whole field feel tangible for the first time.

This was also right around the time I discovered TryHackMe. I was doing research on how to go deeper with SIEM and log analysis and kept seeing it come up — and when I saw that they had actual interactive lab environments where you could get hands-on with real tools, I was sold. That honestly lit a fire under me to finish the rest of the Google certificate as fast as I could so I could get over there and start doing the work in a more hands-on way. Best decision I made in this whole journey.
