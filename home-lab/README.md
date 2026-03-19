```
┌──(abhi㉿security)-[~/home-lab]
└─$ cat README.md
```

# Home Lab

**Status:** In Planning — build starts once TryHackMe SOC path and Security+ prep are further along.

[![Status](https://img.shields.io/badge/Status-In%20Planning-yellow?style=flat)]()
[![Hypervisor](https://img.shields.io/badge/Hypervisor-VirtualBox-183A61?style=flat&logo=virtualbox&logoColor=white)]()
[![Attacker](https://img.shields.io/badge/Attacker%20VM-Kali%20Linux-557C94?style=flat&logo=kali-linux&logoColor=white)]()
[![Target](https://img.shields.io/badge/Target%20VM-Metasploitable%202-red?style=flat)]()

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

![Nmap](https://img.shields.io/badge/Nmap-grey?style=flat)
![Metasploit](https://img.shields.io/badge/Metasploit-grey?style=flat)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat&logo=wireshark&logoColor=white)
![Burp Suite](https://img.shields.io/badge/Burp%20Suite-FF6633?style=flat&logo=burpsuite&logoColor=white)
![Hydra](https://img.shields.io/badge/Hydra-grey?style=flat)
![John the Ripper](https://img.shields.io/badge/John%20the%20Ripper-grey?style=flat)
![Gobuster](https://img.shields.io/badge/Gobuster-grey?style=flat)
![Nikto](https://img.shields.io/badge/Nikto-grey?style=flat)

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

> *"You don't really understand something until you've broken it yourself."*
