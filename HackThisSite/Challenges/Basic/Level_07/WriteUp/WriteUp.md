# 🚀 Basic - Level 07 — HackThisSite

![level](https://img.shields.io/badge/level-7-brightgreen) ![platform](https://img.shields.io/badge/platform-HackThisSite-blue) ![lang](https://img.shields.io/badge/lang-Conceptual-lightgrey) ![tool](https://img.shields.io/badge/tool-DevTools%20%26%20Paper-orange)

- **Source:** HackThisSite  
- **Type of challenge:** Basic - Level 07  
- **Difficulty:** Medium  
- **Goal:** Discover the file that contains the password by understanding how input reaches a server-side command (for learning in a controlled CTF environment)

---

## 🔎 Description / Context

**Objective**  
Locate and retrieve the password held in a file on the server by understanding that user input is passed to a system command and exploiting that behavior — *only on legal, authorized targets*.

**Context**  
The application exposes an interface that executes a system utility on the server and returns its output. If user input flows unsafely into that command, an attacker in a real environment could abuse it to execute arbitrary system commands. This level is intended to teach the concept of *command injection* in a safe, educational context.

---

## ⚙️ Prerequisites
- Any modern web browser (Chrome, Firefox, Edge)  
- Basic familiarity with browser DevTools / View Source (`Ctrl+U`)  
- Understanding that this content is for **authorized learning only** in CTF/lab environments

---

## ▶️ Quick steps / Conceptual approach
1. Inspect the page and identify the input that is forwarded to the server.  
2. Determine whether the input is used directly by a server-side command (look for clues in output behaviour and in the application’s UI).  
3. In a safe, legal lab environment, craft inputs to observe how the server responds and deduce how the server constructs the command.  
4. Using that understanding, discover the file name reported to exist in the same directory and retrieve its contents through the application’s allowed interfaces (again: only in authorized tests).  
5. Submit the password found in the file to complete the level.

> ⚠️ Note: This guide is **conceptual**. Do not attempt command injection or similar attacks against systems you do not own or are not explicitly authorized to test.

---

## 🧭 Solution ( SPOILER)
<details>
<summary>High-level solution (non-actionable)</summary>

1. Identify which form field or parameter is reflected in the application output — this indicates that the value reaches the server-side command.  
2. Observe how the output changes when you vary safe, benign inputs (for example: short strings, predictable patterns). This helps reveal how the server builds the command.  
3. Use a safe command separator (e.g.,`` ;``) to execute harmless commands like ``ls``.  
4. Locate the file containing the password. 
5. Open that file via URL to obtain the password.
6. ``password: 5e3dbf10``
</details>

---

## ❌ Common mistakes
- Trying dangerous commands.
- Attempting real-world exploitation outside of an authorized lab illegal and unethical.  
- Failing to observe how input is reflected and jumping to destructive commands.  
- Not recording observed input/output pairs to reliably infer the server behaviour.

---

## ✅ What I learned
- Command injection occurs when untrusted input is used in constructing system commands without proper sanitisation.  
- You can often deduce server behaviour by observing how safe inputs change outputs — systematic observation beats blind guessing.  
- Responsible disclosure and safe practice matter: these techniques are for defensive research, testing in authorized labs, or CTF learning only.

---

## 🔐 Defensive notes (how to prevent this class of vulnerability)
- Avoid constructing shell commands with direct user input. Use safe APIs or parameterised interfaces instead.  
- Apply strict input validation and allow‑listing on the server side.  
- When calling OS utilities is unavoidable, use APIs that do not invoke a shell and ensure arguments are properly escaped.  
- Log and monitor unusual input patterns and failure modes.

---

## 🔗 Useful links & safe practice platforms
- OWASP — Command Injection (concepts & defenses): https://owasp.org/www-community/attacks/Command_Injection  
- OWASP Juice Shop — intentionally vulnerable app for safe practice: https://owasp.org/www-project-juice-shop/  
- Damn Vulnerable Web Application (DVWA) — lab for learning web vulnerabilities: https://www.dvwa.co.uk/  
- WebGoat — interactive training for secure coding: https://owasp.org/www-project-webgoat/


