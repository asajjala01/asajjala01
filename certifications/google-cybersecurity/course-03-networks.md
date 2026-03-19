# Course 3: Connect and Protect — Networks and Network Security

**Course:** Google Cybersecurity Certificate — Course 3 of 8  
**Status:** ✅ Completed

---

## Network Architecture Basics

### Types of Networks
| Type | Description |
|---|---|
| LAN | Local Area Network — single building or campus |
| WAN | Wide Area Network — across cities/countries (internet is the largest WAN) |
| VLAN | Virtual LAN — logically segmented network within a physical network |
| VPN | Virtual Private Network — encrypted tunnel over a public network |

### Network Devices
| Device | Role |
|---|---|
| Router | Directs traffic between different networks |
| Switch | Connects devices within the same network |
| Firewall | Filters traffic based on rules |
| Hub | Broadcasts traffic to all devices (outdated, replaced by switches) |
| IDS/IPS | Intrusion Detection / Prevention System |
| Proxy | Acts as intermediary between client and internet |

---

## The OSI Model

| Layer | Name | Protocol Examples | Data Unit |
|---|---|---|---|
| 7 | Application | HTTP, HTTPS, DNS, FTP, SMTP | Data |
| 6 | Presentation | SSL/TLS, JPEG, ASCII | Data |
| 5 | Session | NetBIOS, RPC | Data |
| 4 | Transport | TCP, UDP | Segment |
| 3 | Network | IP, ICMP, OSPF | Packet |
| 2 | Data Link | Ethernet, ARP, MAC | Frame |
| 1 | Physical | Cables, radio, fiber | Bits |

> **Memory trick:** "All People Seem To Need Data Processing" (top-down: 7→1)

---

## TCP/IP Model

The practical model used in the real world (4 layers):

| TCP/IP Layer | Maps to OSI | Protocols |
|---|---|---|
| Application | 5, 6, 7 | HTTP, DNS, FTP, SMTP |
| Transport | 4 | TCP, UDP |
| Internet | 3 | IP, ICMP |
| Network Access | 1, 2 | Ethernet, ARP |

---

## Key Protocols

| Protocol | Port | Purpose |
|---|---|---|
| HTTP | 80 | Web traffic (unencrypted) |
| HTTPS | 443 | Web traffic (encrypted) |
| FTP | 21 | File transfer |
| SSH | 22 | Secure remote access |
| Telnet | 23 | Remote access (unencrypted — avoid) |
| SMTP | 25 | Sending email |
| DNS | 53 | Resolves domain names to IPs |
| DHCP | 67/68 | Assigns IP addresses automatically |
| RDP | 3389 | Remote Desktop Protocol |
| SMB | 445 | File sharing (Windows) |

> Memorize these ports — they come up constantly in CTFs and real SOC work.

---

## IP Addressing

### IPv4
- Format: `192.168.1.100`
- 32-bit address space

### Private IP Ranges (RFC 1918)
```
10.0.0.0    – 10.255.255.255    /8   (Class A)
172.16.0.0  – 172.31.255.255   /12  (Class B)
192.168.0.0 – 192.168.255.255  /16  (Class C)
```

### Subnet Masks
```
/24 = 255.255.255.0   → 254 usable hosts
/16 = 255.255.0.0     → 65,534 usable hosts
/8  = 255.0.0.0       → 16,777,214 usable hosts
```

---

## Firewalls

### Types
| Type | How It Works |
|---|---|
| Packet filtering | Inspects packet headers (IP, port) — no state tracking |
| Stateful | Tracks connection state — more intelligent |
| NGFW (Next-Gen) | Deep packet inspection, app awareness, IDS/IPS built-in |

### Firewall Rules Logic
```
Allow TCP from 192.168.1.0/24 to any port 443    ← HTTPS outbound allowed
Deny TCP from any to any port 23                 ← block Telnet
Allow TCP from any to 10.0.0.5 port 80           ← allow web server inbound
Deny all                                          ← implicit deny at the end
```
> **Implicit deny** — if traffic doesn't match an allow rule, it's blocked. Default deny is best practice.

---

## Common Network Attacks

| Attack | Description | Defense |
|---|---|---|
| DoS / DDoS | Overwhelm a system with traffic | Rate limiting, CDN, scrubbing |
| Man-in-the-Middle | Intercept communications | TLS/HTTPS, certificate validation |
| ARP Spoofing | Fake ARP replies to redirect traffic | Dynamic ARP Inspection |
| DNS Spoofing | Redirect domain lookups to malicious IPs | DNSSEC |
| Port Scanning | Probe for open ports | Firewalls, IDS rules |
| Packet Sniffing | Capture network traffic | Encryption (TLS), VPN |

---

## Useful Commands

```bash
ping 8.8.8.8                     # test basic connectivity
traceroute google.com            # trace packet path
nslookup google.com              # DNS lookup
dig google.com                   # detailed DNS query
netstat -an                      # show active connections and listening ports
ip a                             # show network interfaces (Linux)
arp -a                           # show ARP cache
tcpdump -i eth0 -n               # capture packets on eth0
```

---

## My Take

This was the most intimidating course for me. Networks felt like a completely different language and the OSI model alone had me staring at the screen wondering if I'd gotten in over my head. But this is also where having the right resources around you makes all the difference.
I leaned on two things heavily to get through this one. First, I have friends who are programmers and have been around tech their whole lives — being able to sit down with them and say "okay explain this to me like I'm five" was invaluable. They helped me understand not just what these concepts were but why they exist and how they connect to each other. Second, I used AI constantly to break things down in plain language, generate analogies, and re-explain things from different angles until they clicked. Between those two resources I went from completely lost to actually feeling like things made sense.
And once it clicked, it really clicked. The OSI model stopped being a memorization exercise and became an actual troubleshooting tool. Understanding how protocols like ARP and DNS are supposed to work made it obvious why attacks like ARP spoofing and DNS poisoning are possible in the first place. That's the thing about networking — you can't defend what you don't understand. Port numbers I ended up drilling with flashcards and I'm glad I did because they show up everywhere in log analysis and CTF work.
