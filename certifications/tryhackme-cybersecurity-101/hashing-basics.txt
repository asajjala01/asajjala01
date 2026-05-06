```
┌──(abhi㉿security)-[~/certifications/tryhackme-soc-level-1]
└─$ cat hashing-basics.md
```

# Hashing Basics

**Path:** TryHackMe — SOC Level 1  
**Module:** SOC Team Internals  
**Room:** Hashing Basics  
**Status:** ✅ Completed

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)]()
[![Tool](https://img.shields.io/badge/Tool-Hashcat-grey?style=flat)]()
[![Module](https://img.shields.io/badge/Module-SOC%20Team%20Internals-212C42?style=flat&logo=tryhackme&logoColor=white)]()

---

## What This Room Covers

A foundational room on how hashing works, why it matters in security, and how attackers crack hashed passwords. Covers the theory behind hash functions, common algorithms, insecure password storage practices, rainbow tables, and hands-on password cracking using hashcat and online tools.

---

## Hash Functions — The Basics

A hash function takes an input of any size and produces a fixed-length output — the hash. A few key properties:

- **One-way** — you cannot reverse a hash back to the original input
- **Deterministic** — the same input always produces the same hash
- **Avalanche effect** — a tiny change in input produces a completely different hash
- **Fixed length** — regardless of input size, the output is always the same length

### Hexadecimal vs Binary

Hashes are typically represented in hexadecimal — a base-16 number system using digits 0-9 and letters A-F. Each hexadecimal character represents 4 bits, so a single byte (8 bits) is represented by two hex characters. This is why hash outputs look like long strings of letters and numbers rather than raw binary.

```
Binary:      01001000 01100101 01111001
Hex:         48 65 79
```

### The Pigeonhole Effect

When you have more possible inputs than possible outputs, collisions become inevitable — two different inputs producing the same hash. This is why older algorithms like MD5 are considered broken. Attackers can exploit collisions to bypass integrity checks or authentication.

---

## Common Hash Algorithms

| Algorithm | Output Length | Status |
|---|---|---|
| MD5 | 128-bit (32 hex chars) | ❌ Broken — do not use |
| SHA-1 | 160-bit (40 hex chars) | ❌ Weak — deprecated |
| SHA-256 | 256-bit (64 hex chars) | ✅ Secure |
| SHA-3 | Variable | ✅ Secure |
| bcrypt | Variable | ✅ Secure — designed for passwords |

---

## Insecure Password Storage Practices

The room covered three common mistakes organizations make that end up in breaches — and why `rockyou.txt` exists as a result.

**1. Storing passwords in plaintext**
No hashing at all. If the database is breached, every password is immediately readable. This is how massive credential dumps happen.

**2. Storing passwords using deprecated encryption**
Using reversible encryption rather than hashing. If the key is compromised, every password can be decrypted. Encryption is for data you need to retrieve — passwords should never need to be retrieved, only verified.

**3. Storing passwords using an insecure hashing algorithm**
Using MD5 or SHA-1 to hash passwords. These algorithms are fast — which is great for performance but terrible for security. Fast hashing means attackers can run billions of attempts per second against a hash. `rockyou.txt` is a wordlist built from real passwords leaked in breaches caused by exactly this practice — over 14 million real-world passwords that people actually used.

---

## Rainbow Tables

A rainbow table is a precomputed lookup table of hashes and their corresponding plaintext values. Instead of cracking a hash in real time, an attacker just looks it up.

```
Hash:     5f4dcc3b5aa765d61d8327deb882cf99
Lookup:   "password"
```

This is why **salting** exists — adding a unique random value to each password before hashing means the same password produces a different hash for every user, making precomputed rainbow tables useless.

### Online Tools Used
- **CrackStation** (crackstation.net) — large precomputed lookup table, good for common hashes
- **Hashes.com** — similar lookup service, useful for quick identification and cracking

---

## What I Actually Did — The Labs

### Identifying Hash Types

Before cracking a hash you need to know what algorithm produced it. Hash length and format give it away:

| Hash | Length | Type |
|---|---|---|
| `5f4dcc3b5aa765d61d8327deb882cf99` | 32 chars | MD5 |
| `aaf4c61ddcc5e8a2dabede0f3b482cd9aa9c` | 40 chars | SHA-1 |
| `9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1` | 64 chars | SHA-256 |

### Cracking Hashes with Hashcat

Hashcat uses the GPU to run through wordlists at massive speed — far faster than CPU-based cracking. The basic syntax:

```bash
hashcat -m [hash_type] -a 0 [hash_file] [wordlist]
```

| Flag | Meaning |
|---|---|
| `-m` | Hash type (1400 = SHA-256, 0 = MD5) |
| `-a 0` | Attack mode — dictionary attack |
| `hash_file` | File containing the hash to crack |
| `wordlist` | The wordlist to run through — rockyou.txt |

### Lab Results

**Command I ran:**
```bash
hashcat -m 1400 -a 0 hash2.txt /usr/share/wordlists/rockyou.txt --force
```

![Hashcat running SHA-256 crack against rockyou.txt wordlist](./screenshots/hashcat-command.png)

**Hashes cracked:**

| Hash File | Hash | Algorithm | Cracked Password |
|---|---|---|---|
| hash1.txt | `$2a$06$7yoU3Ng8dHTXphAg913cyO6Bjs3K5lBnwq5FJyA6d01pMSrddr1ZG` | bcrypt | `85208520` |
| hash2.txt | `9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1` | SHA-256 | `halloween` |
| hash3.txt | `$6$GQXVvW4EuM$ehD6jWiMsfNorxy5SINsgdlxmAEl3.yif0/c3NqzGLa0P.S7KRDYjycw5bnYkF5ZtB8wQy8KnskuWQS3Yr1wQ0` | SHA-512crypt | `spaceman` |
| hash4.txt | `b6b0d451bbf6fed658659a9e7e5598fe` | MD5 | `funforyou` |

![Correct answers showing cracked hashes halloween spaceman funforyou](./screenshots/hashcat-results.png)

---

## Key Takeaways

**Hash type identification is step one.** Before you can crack anything you need to know what you're dealing with. Hash length and format tell you the algorithm — knowing that determines the `-m` flag in hashcat.

**rockyou.txt is the go-to wordlist.** It contains over 14 million real passwords from actual breaches. If someone used a common password it's almost certainly in there. The fact that `halloween`, `spaceman`, and `funforyou` were all cracked instantly shows how weak common passwords are even when hashed.

**GPU cracking is orders of magnitude faster than CPU.** The `--force` flag tells hashcat to use available hardware. In a real environment with a dedicated GPU rig, billions of hashes per second is achievable against MD5.

**MD5 is effectively broken for passwords.** `funforyou` from an MD5 hash cracked almost instantly. Anyone still storing passwords with MD5 is one breach away from every account being compromised.

**Online tools are useful for quick lookups.** CrackStation and Hashes.com are fast for common hashes — if the password was ever in a breach before, it's probably already in their database.

---

## My Take

This room was satisfying in a way I didn't fully expect. I already understood hashing conceptually from the Google cert — the one-way nature of it, why MD5 is weak, why salting matters. But actually running hashcat in a terminal, pointing it at a real wordlist, and watching it crack a SHA-256 hash in seconds made all of that theory feel very concrete and very real.

The moment `halloween` came back as the cracked password for a SHA-256 hash was a good reminder that the algorithm being secure doesn't matter if the password itself is weak. A strong algorithm with a weak password is still a weak password. That's the takeaway that stuck with me most from this room.

The insecure practices section was also more impactful than expected — knowing that `rockyou.txt` exists because of real breaches caused by real organizations storing passwords incorrectly puts a human cost on what could otherwise feel like abstract security theory.
