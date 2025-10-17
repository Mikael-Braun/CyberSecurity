# crackmes.one — Reverse-Engineering Platform



**Website:** https://crackmes.one a public collection of *crackmes* (small programs created for practicing reverse engineering).  

> ⚠️ **Legal & Ethical Notice**  
> Crackmes are intended for educational use and legal reverse engineering practice only. Do **not** use techniques learned here to attack software or infrastructure without explicit authorization. Always use isolated lab environments (VMs or containers).

---

## Table of Contents

- [Overview](#overview)
- [Public Stats](#public-stats)
- [Main Functionality](#main-functionality)
- [Known Open-Source Implementation (Stack)](#known-open-source-implementation-stack)
- [FAQ / Legality / Community](#faq--legality--community)
- [Submissions](#submissions)
- [Security Recommendations for Users and Operators](#security-recommendations-for-users-and-operators)
- [History](#history)


---
## Overview
crackmes.one is a public platform where authors publish crackmes, and the community can download, solve, and submit writeups. 
The homepage displays public counters (users, crackmes, writeups) and useful links (FAQ, Discord, latest).

## Public Stats 

### Values visible on the homepage at the time of verification:

- Registered users: ~77,733
- Available crackmes: ~4,234
- Submitted writeups: ~5,974
(These numbers are publicly displayed and may vary over time.)

## Main Functionality

- Catalog of crackmes by platform (Windows, Linux, etc.).
- Individual crackme pages with metadata: author, language, architecture, difficulty, quality, platform, date, comments, and writeups.
- User registration required to submit crackmes/writeups.
- Rating and commenting system; public listings like “latest” for discovery.
- Examples and individual crackme pages are available for download and for reading descriptions/writeups.

## Known Open-Source Implementation (Stack)

A public contribution on GitHub (sar5430/crackmes.one) is frequently referenced as the site’s implementation. This implementation uses:
Backend: Go
Database: MongoDB
Frontend: templates / assets served by the backend
The repository includes basic instructions for local development (e.g., configuring MongoDB, editing route files for dev environment). This repo is used as a reference to run a local copy.

## FAQ / Legality / Community

The site’s FAQ explains that the project’s purpose is to help learn reversing, and that crackmes are intentionally created to be cracked. Therefore, practicing with them is presented as legal within this educational context. Reading the FAQ is recommended before submitting content.
The site also indicates that a Discord server exists for questions and community interaction (link available on the site). For questions regarding rules and submissions, the Discord and FAQ are the suggested channels.

## Submissions 

To submit a crackme or a writeup, you must register and log in. The author should provide metadata (description, difficulty, platform, etc.). Comments and writeups are moderated (the site encourages responsible uploads and writeups rather than posting solutions in comments). Submission page examples and instructions appear on individual pages.

## Security Recommendations for Users and Operators

- For Users:
Never run unknown files on your main host; always use an isolated VM or container. Many crackmes can trigger antivirus or exhibit potentially dangerous behavior. The community recommends using virtual machines.

- For Operators / Maintainers:

Validate uploads, limit file size/type, scan files (AV/heuristics), isolate processing (workers in containers), enforce HTTPS, CSP, rate limiting, and logging/monitoring.

These practices follow standard security guidelines for platforms that accept executable files.

## History 

crackmes.one emerged as a meeting point and continuation for the crackme community (many mention that it fills the gap left by crackmes.de). The reversing community has used the site as a repository and hub since its creation/relauch. Discussions and posts about the site and related writeups appear on community platforms like Reddit and Medium.
