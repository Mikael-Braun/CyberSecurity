# 🔥 Ethical Hacking Writeups & Learning Lab

> A curated collection of writeups, scripts and notes about offensive security, CTFs and reverse engineering.  
> Focused on reproducibility, clear documentation and responsible learning.

---

## Table of Contents

- [Overview](#overview)  
- [Included Platforms](#included-platforms)  
- [Repository Structure](#repository-structure)    
- [Projects By area ](#Projects-By-area)
- [Ethics & Legal Notice](#ethics--legal-notice)  
- [Security Recommendations](#security-recommendations)
- [License](#license)  


---

## Overview

This repository holds writeups and tooling from various challenge platforms and learning resources. It’s organized for easy browsing and reproducible practice, always run everything in isolated environments (VMs / Docker).

**Goals**
- Document every step that was taken  
- Provide reusable scripts and templates.  
- Encourage reproducible learning and ethical hacking practice.

---

## Included Platforms

- **OverTheWire** : Bandit, Narnia, etc.  
- **HackThisSite**: Basic & Realistic missions  
- **PicoCTF** : CTF challenge writeups  
- **HackTheBox** : Resolved machines (recon → exploit → post-exploit)  
- **Crackmes** : Binary analysis & reverse engineering  
- **BOOKS** : Scripts, snippets and experiments learned from books
- **CryptoHack** : Elliptic Curves, Modular Arithmetic, Symmetric/Asymmetric Cryptography

---

## Repository Structure

Each platform folder should include:
- `README.md` (local index / summary)  
- writeups in `.md` format or notes
- `scripts/` for exploits or helper utilities 
- optional `screenshots/` or `captures/` for images

---

## Projects By area

### Reverse Engineering & Exploit Development
- CrackMe challenges: [Crackmes folder](./Crackmes/BinaryAnalysis)  
- picoCTF binary challenges: [picoCTF](./PicoCTF/Cryptography)

### Web Application Pentesting
- HackTheBox web labs: [HackTheBox folder](./HackTheBox)  
- picoCTF web challenges: [picoCTF folder](./PicoCTF/WebExploitation)  

### Cloud Security
 
- AWS / Cloud labs (learning modules): [folder link](./HTBCloudLabs)  

### Cryptography 

### Hardware & IoT Security
- Flipper Zero experiments: [Flipper folder](./Flipper)  
- Raspberry Pi lab projects: [RaspberryPi folder](./RaspberryPi)

---
## Ethics & Legal Notice

This repository is for educational purposes only.
Do not use techniques from these writeups against systems you don’t own or don’t have explicit permission to test. Unauthorized 
access is illegal and unethical. You are responsible for how you use this material.


## Security Recommendations

- Never store credentials, private keys, or secrets in the repository.
- Run exploits and scripts in sandboxed environments (VMs, containers).
- Use minimal privilege accounts for testing; avoid root unless necessary.
- Add basic static checks (linters) for scripts before running.
- Consider using encryption for sensitive notes kept outside repo.


## License

Copyright (c) 2025 Mikael Braun

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE ABOVE COPYRIGHT NOTICE AND THIS PERMISSION NOTICE SHALL BE INCLUDED IN ALL
COPIES OR SUBSTANTIAL PORTIONS OF THE SOFTWARE.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.