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
