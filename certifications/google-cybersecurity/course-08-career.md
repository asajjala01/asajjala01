```
┌──(abhi㉿security)-[~/certifications/google-cybersecurity]
└─$ cat course-08-career.md
```

# Course 8: Put It to Work — Prepare for Cybersecurity Jobs

**Course:** Google Cybersecurity Certificate — Course 8 of 8  
**Status:** ✅ Completed

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)]()
[![Course](https://img.shields.io/badge/Course-8%20of%208-grey?style=flat)]()
[![Tools](https://img.shields.io/badge/Tools-NotebookLM%20%7C%20AI%20Job%20Tools-grey?style=flat)]()

---

## Entry-Level Cybersecurity Roles

| Role | Focus | Key Skills |
|---|---|---|
| SOC Analyst (L1/L2) | Monitor alerts, triage incidents | SIEM, log analysis, playbooks |
| Security Analyst | Broader security posture work | Risk assessment, vulnerability mgmt |
| IT Security Specialist | Org-wide security implementation | Policies, tools, user support |
| Incident Responder | Handle active breaches | Forensics, containment, root cause |
| Penetration Tester | Find vulnerabilities before attackers | Kali Linux, Metasploit, report writing |

> **My target:** SOC Analyst (L1) as the entry point, building toward L2 and eventually IR.

---

## Communicating with Stakeholders

Security isn't just technical — it's about translating risk into business language.

| Technical Finding | Stakeholder Language |
|---|---|
| "Unpatched CVE-9.8 on web server" | "Critical vulnerability — attackers could take full control of the public website. Patch within 24 hours." |
| "No MFA on admin accounts" | "If an admin password is stolen, there's nothing stopping full system access. MFA would prevent this." |
| "Logs show lateral movement" | "An attacker appears to be moving through our network looking for high-value systems. We need to isolate and investigate immediately." |

---

## Incident Escalation

Knowing when to escalate is a key L1 SOC skill.

**Escalate when:**
- The incident is outside your documented playbook
- Systems are actively being compromised
- You suspect data exfiltration has occurred
- The scope is expanding rapidly
- Legal or regulatory implications are present

**Don't escalate every alert** — triage first. False positives waste senior analyst time.

---

## Security Mindset

- **Think like an attacker** — understand how systems get compromised to defend them better
- **Defense in depth** — no single control is enough; layer your defenses
- **Assume breach** — operate as if attackers are already inside; focus on detection and response
- **Document everything** — if it isn't documented, it didn't happen
- **Continuous learning** — the threat landscape changes constantly; staying current is part of the job

---

## Interview Prep (SOC Analyst)

### Common Technical Questions
- Walk me through what happens when you get a phishing alert
- What's the difference between IDS and IPS?
- How would you investigate a brute force attack in your SIEM?
- What is the CIA Triad?
- What's the difference between a vulnerability and an exploit?
- How do you prioritize which alerts to investigate first?

### Behavioral Questions (STAR Format)
- Tell me about a time you had to communicate complex information simply *(sales background = great answer)*
- Describe a time you had to stay calm under pressure
- Tell me about a time you had to learn something new quickly

### Questions to Ask Interviewers
- What does a typical day look like for an L1 analyst here?
- How mature is the SOC? Is there a formal escalation process?
- What SIEM are you using?
- What does the mentorship and growth path look like from L1 to L2?

---

## Transferable Skills from Sales

| Sales Skill | Security Application |
|---|---|
| Building rapport and trust | Stakeholder communication, user awareness training |
| Pattern recognition in pipeline data | Log analysis, anomaly detection |
| Working to strict SLAs | Incident response time targets |
| Handling objections calmly | Escalation conversations, communicating bad news |
| CRM data hygiene | Security data management and documentation |
| Training new reps | Security awareness program delivery |

---

## What I Had to Do

This course was less about technical labs and more about pulling everything together — professional development, real-world application, and job readiness.

**Activities:**

1. **Analyze event logs with NotebookLM** — used Google's NotebookLM to analyze and query event log data. This was a practical introduction to using AI tools specifically for security investigation work — uploading log data, asking questions about it, and getting structured insights back. A preview of where AI-assisted analysis is heading in real SOC environments.

2. **Escalation** — worked through escalation scenarios. Given different incident types and severity levels, practice making the call on when to handle something yourself versus when to escalate to senior staff. The judgment around escalation is one of the most important soft skills for an L1 analyst and something you can only really develop through scenario practice.

3. **Exploring cybersecurity organizations** — researched professional organizations, communities, and resources in the cybersecurity space. Understanding where the industry gathers, where threat intelligence is shared, and where continuing education lives — ISACA, ISC2, SANS, local security groups, CTF communities.

**Bonus Module — Accelerate Your Job Search with AI:**

Google added a dedicated AI module at the end of the course focused entirely on using AI tools to get hired faster. This wasn't theoretical — it was practical and immediately applicable. Covered using AI to strengthen your resume and surface transferable skills, optimize your LinkedIn profile and close keyword gaps recruiters search for, prep for interviews through mock sessions and feedback, write personalized cover letters and cold outreach, and build a study plan tailored to your specific target role. Coming from sales I already knew how to communicate — but this module helped me frame that experience in language that actually resonates with technical hiring managers. Genuinely one of the most useful things in the entire certificate.

---

## My Take

A fitting way to end the certificate. By the time I got here I already had a pretty clear picture of where I wanted to go — SOC analyst, blue team, detection and response — so this course felt like it was putting a bow on everything that came before it.

What I appreciated most was that it didn't just say "here's how to get a job" and leave it at that. It actually made me think seriously about how to tell my story as someone coming from a non-traditional background. The sales-to-security transition isn't obvious on paper and this course pushed me to connect those dots deliberately — not just list what I did before but articulate why it's actually relevant. That work ended up shaping how I wrote my resume, how I talk about myself in interviews, and honestly how I built out this entire GitHub profile.

The NotebookLM activity stood out to me because it felt forward-looking. Using AI to actually query and analyze log data isn't a novelty — it's where SOC work is heading and getting exposure to that workflow early feels like an advantage.

This was also right around the time I fully committed to TryHackMe. I'd discovered it during Course 6 but finishing the certificate gave me the green light to dive in properly. TryHackMe was the missing piece — it took everything I'd learned across these 8 courses and gave me a place to actually apply it in a hands-on environment. The Google certificate gave me the foundation and TryHackMe gave me the practice floor. Between the two I finally felt like I wasn't just studying security — I was doing it.
