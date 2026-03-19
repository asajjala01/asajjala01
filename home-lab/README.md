# Home Lab

**Status:** 🔄 In Planning  
**Goal:** Build a personal cybersecurity lab environment for hands-on practice outside of guided platforms like TryHackMe.

---

## Why I'm Building This

TryHackMe has been an incredible resource — the guided labs, the VMs they provide, the structured learning paths. But there's a next level to hands-on practice and that's building your own environment from scratch. No guardrails, no hints, no pre-configured scenarios. Just you, your machines, and a problem to solve.

A home lab is where you take everything you've learned across certifications and guided platforms and start applying it on your own terms. You control the network, you choose what to attack, you decide what to defend. It forces a deeper level of understanding because when something breaks you have to figure out why — there's no support ticket to open.

This is the next milestone on my learning path and I'll be documenting the entire build process here as I go — from the initial setup all the way through to running my first practice scenarios.

---

## Planned Setup

### Hypervisor
| Tool | Purpose |
|---|---|
| VirtualBox | Free, cross-platform VM manager — will use this to run all lab machines |

### Virtual Machines
| Machine | Role | OS |
|---|---|---|
| Kali Linux | Attacker machine — primary pentesting toolkit | Kali Linux (latest) |
| Metasploitable 2 | Intentionally vulnerable target for practice | Linux |
| Windows 10 (vulnerable) | Windows-based attack practice | Windows 10 |

### Network Configuration
- **Host-only adapter** — all VMs isolated from the real internet, can only talk to each other and the host machine
- No traffic leaves the lab environment

### Tools to Install and Practice
`Nmap` `Metasploit` `Wireshark` `Burp Suite` `Hydra` `John the Ripper` `Gobuster` `Nikto`

---

## How I'll Be Building This

One thing I've learned throughout this journey is that the best way to learn is to use every resource available to you — and I plan to do exactly that with the home lab.

**AI** is going to be a big part of the build process. Whether it's troubleshooting a VM configuration that isn't behaving, debugging a tool that won't run, understanding why a scan is returning unexpected results, or just breaking down a concept that isn't clicking — AI has been a constant companion throughout my learning and this lab will be no different. I find it especially useful for getting quick explanations when I'm deep in a problem and need clarity fast without losing momentum.

**My network of friends** who come from programming and tech backgrounds will also be part of this. I've leaned on them throughout the Google cert and TryHackMe when things got complex, and having people you can actually sit down with and talk through a problem is something I don't take for granted. Debugging lab environments, sanity checking configurations, bouncing ideas — that kind of collaboration makes the learning process faster and a lot more fun.

The combination of structured learning, hands-on labs, AI tools, and real people to learn alongside is what's gotten me this far. The home lab is just the next chapter of the same approach.

---

## Planned Documentation

Once the lab is built each section below will be filled in:

- [ ] **Setup Guide** — step-by-step walkthrough of building the lab from scratch
- [ ] **Network Topology** — diagram of how the machines connect
- [ ] **Tools Reference** — what each tool does and how I'm using it
- [ ] **Practice Scenarios** — documented attack/defense exercises I've run
- [ ] **Lessons Learned** — what broke, what I fixed, what I learned

---

## Timeline

Currently working through the TryHackMe SOC Analyst path and Security+ prep. Home lab build is the next major project on the roadmap once those are further along. Will update this folder as soon as the build begins.

> *"You don't really understand something until you've broken it yourself."*
