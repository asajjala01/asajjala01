# Course 4: Tools of the Trade — Linux and SQL

**Course:** Google Cybersecurity Certificate — Course 4 of 8  
**Status:** ✅ Completed

---

## Linux for Security

### Why Linux Matters in Cybersecurity
Most servers, security tools, and attack platforms run on Linux. As a SOC analyst or penetration tester, you'll be living in the terminal.

### File System Structure
```
/           root of everything
├── /bin    essential binaries (ls, cp, mv)
├── /etc    configuration files
├── /home   user home directories
├── /var    variable data (logs live here: /var/log)
├── /tmp    temporary files (often writable by all users — watch this)
├── /root   root user's home directory
└── /usr    user programs and utilities
```

### Essential Commands

**Navigation**
```bash
pwd                    # where am I?
ls -la                 # list all files with permissions
cd /etc                # change directory
cd ..                  # go up one level
```

**File Operations**
```bash
cat file.txt           # print file contents
less file.txt          # scroll through a file
head -n 20 file.txt    # first 20 lines
tail -n 20 file.txt    # last 20 lines
tail -f /var/log/syslog  # watch a log file live
cp file.txt /tmp/      # copy
mv file.txt newname.txt  # move / rename
rm file.txt            # delete
mkdir newfolder        # create directory
```

**Searching**
```bash
grep "error" /var/log/syslog        # search for "error" in a file
grep -r "password" /etc/            # recursive search in a directory
grep -i "failed" auth.log           # case-insensitive search
find / -name "*.conf" 2>/dev/null   # find all .conf files
find /tmp -newer /etc/passwd        # files newer than passwd
```

**Users and Permissions**
```bash
whoami                 # current user
id                     # user ID and group memberships
sudo -l                # what can this user run as sudo?
cat /etc/passwd        # list of users
cat /etc/shadow        # password hashes (root only)
adduser newuser        # create a user
passwd username        # change password
```

**Permissions Model**
```
-rwxrw-r-- 1 abe security 1234 Jan 01 file.sh

 - = file type (- file, d directory, l link)
 rwx = owner: read, write, execute
 rw- = group: read, write
 r-- = others: read only

chmod 755 file.sh      # rwxr-xr-x
chmod +x script.py     # add execute for all
chown abe:security file.sh  # change owner and group
```

**Processes and Network**
```bash
ps aux                 # all running processes
kill -9 [PID]          # force kill
top                    # live process monitor
netstat -an            # active connections
ss -tulnp              # listening ports (modern alternative to netstat)
```

---

## SQL for Security Analysts

SQL lets you query databases to investigate security incidents — user logins, access logs, failed authentications, etc.

### Core Syntax
```sql
SELECT *
FROM log_table
WHERE status = 'failed'
AND timestamp > '2026-01-01'
ORDER BY timestamp DESC
LIMIT 100;
```

### Filtering
```sql
-- Exact match
WHERE username = 'admin'

-- Range
WHERE login_time BETWEEN '2026-01-01' AND '2026-01-31'

-- Pattern match (% = wildcard)
WHERE email LIKE '%@gmail.com'

-- Multiple values
WHERE status IN ('failed', 'blocked', 'denied')

-- Null check
WHERE resolved_at IS NULL
```

### Aggregation
```sql
-- Count failed logins per user
SELECT username, COUNT(*) AS failed_attempts
FROM auth_log
WHERE status = 'failed'
GROUP BY username
HAVING COUNT(*) > 10
ORDER BY failed_attempts DESC;
```

### Joins
```sql
-- Match log entries with user records
SELECT u.username, u.department, l.event, l.timestamp
FROM users u
JOIN access_log l ON u.user_id = l.user_id
WHERE l.event = 'unauthorized_access';
```

### Security Investigation Queries

**Find all failed logins in the last 24 hours:**
```sql
SELECT username, ip_address, COUNT(*) AS attempts
FROM auth_log
WHERE status = 'failed'
AND timestamp >= NOW() - INTERVAL 1 DAY
GROUP BY username, ip_address
ORDER BY attempts DESC;
```

**Find logins from unusual hours:**
```sql
SELECT *
FROM auth_log
WHERE HOUR(timestamp) NOT BETWEEN 7 AND 19
AND status = 'success';
```

**Find accounts that were never supposed to log in:**
```sql
SELECT l.*
FROM auth_log l
LEFT JOIN authorized_users a ON l.username = a.username
WHERE a.username IS NULL;
```

---

## My Take

This was genuinely one of my favorite courses and I had a lot of fun with it. I'd messed around with Windows terminal before so the idea of a command line wasn't completely foreign to me — but Linux felt different in a good way. It just made more sense. Everything is transparent, everything is a file, and once you understand the structure it feels intuitive in a way that Windows terminal never quite did for me.

The SQL and Python portions I'll be honest — I breezed through those. I'd worked with both before so the content was pretty much second nature to me. It was actually a confidence boost at the right time, coming off the Linux permission stuff which took me a bit longer to fully absorb. File permissions specifically — the `rwx` notation and the logic behind `chmod` numbers took a few passes before it really clicked. But I got there, and once I did it became one of the most used concepts throughout the rest of the course.

What I loved most about this one overall was how immediately practical it felt. Running `grep` through log files, using `tail -f` to watch a log update in real time, checking `sudo -l` to see what a user can run — these aren't abstract exercises, this is actual SOC analyst work. By the end of this course I felt like I was actually doing security, not just reading about it.
