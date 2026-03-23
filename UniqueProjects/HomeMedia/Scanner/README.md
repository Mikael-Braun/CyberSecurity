# 🛡️ Level 3 File Security Scanner

A **multi-layer security scanner for media files**, written in Python.  
It analyzes files using several detection techniques to determine the **probability that a file contains malware**.

The scanner combines:

- static analysis
- antivirus scanning
- entropy analysis
- YARA rules
- reputation checks
- heuristic detection

Based on the results, the file is automatically **accepted as safe media or moved to quarantine**.

---

# ⚙️ Scanner Architecture

The scanner is designed to be **robust, scalable, and fault-tolerant**.

Main features:

- file processing **queue**
- **result caching**
- **multi-layer security analysis**
- **timeouts and error handling**

General workflow:

```
File received
      │
      ▼
SHA256 Hash
      │
      ▼
Cache lookup
      │
      ├ Cached result → return
      │
      ▼
Security analysis
      │
      ├ Entropy analysis
      ├ ClamAV scan
      ├ VirusTotal check
      ├ Suspicious strings
      ├ MIME validation
      ├ File size check
      └ YARA rules
      │
      ▼
Risk score calculation
      │
      ▼
File classification
 ├ MEDIA
 └ QUARANTINE
```

---

# 🔐 SHA256 Hashing

Each file is identified using a **SHA256 hash**.

Used for:

- unique file identification
- cache lookup
- VirusTotal queries
- malware reputation checks

---

# 🧠 Entropy Analysis

Entropy measures the **randomness of the file content**.

Typical values:

| Entropy | Meaning |
|--------|--------|
| < 4 | Low |
| 4 – 7 | Normal |
| > 7 | Suspicious |

High entropy often indicates:

- packed executables
- encrypted payloads
- obfuscated malware

---

# 🦠 ClamAV Antivirus Scan

The scanner integrates **ClamAV**, an open-source antivirus engine.

Command used:

```
clamscan --no-summary
```

Possible results:

| Result | Meaning |
|------|--------|
| CLEAN | No malware detected |
| MALICIOUS | Malware detected |
| UNKNOWN | Inconclusive result |
| TIMEOUT | Scan took too long |

---

# 🌐 VirusTotal Reputation Check

If a **VirusTotal API key** is configured, the scanner queries the file hash against the VirusTotal database.

API endpoint:

```
https://www.virustotal.com/api/v3/files/{sha256}
```

Possible responses:

| Result | Meaning |
|------|--------|
| CLEAN | No antivirus engines flagged the file |
| DETECTED | One or more engines detected malware |
| NOT_IN_DB | File unknown to VirusTotal |

---

# 🔍 Suspicious String Detection

The scanner searches for **known suspicious strings** inside files.

Examples:

```
eval(
exec(
base64
cmd.exe
powershell
malware
```

These may indicate:

- malicious scripts
- command execution
- encoded payloads
- exploit code

---

# 📄 MIME Type Validation

The scanner verifies the **actual MIME type** using `libmagic`.

Allowed media types include:

```
audio/mp3
audio/flac
audio/x-wav
video/mp4
video/x-matroska
video/x-msvideo
```

If the MIME type does not match an expected media format, the file is flagged as **suspicious**.

---

# 📏 File Size Validation

The scanner checks whether the file size is reasonable.

Configuration:

```
minimum size: 10 bytes
maximum size: 2 GB
```

Files outside this range may indicate:

- corruption
- hidden payloads
- malformed files

---

# 🧬 YARA Rule Detection

The scanner supports **YARA rules**, commonly used in malware research and threat intelligence.

### Quarantine Rules

```
MEDIA_Embedded_Executable
MEDIA_Header_Mismatch
MEDIA_Double_Extension
```

These rules add a **high risk score**.

### Score Rules

```
MEDIA_Suspicious_Strings
MEDIA_Abnormal_Entropy
```

These rules increase the suspicion level.

---

# 📊 Risk Scoring System

Each detection contributes to a **final risk score**.

| Detection | Score |
|----------|------|
| High entropy | +20 |
| ClamAV detection | +20 |
| VirusTotal detection | +30 |
| Suspicious strings | +25 |
| Invalid MIME | +10 |
| Suspicious size | +10 |
| Critical YARA rule | +40 |

Maximum score:

```
100%
```

---

# 📈 Risk Probability Bar

Example output:

```
Malware probability:

[###########-------] 45%
```

Color indicators:

| Color | Meaning |
|------|--------|
Green | Safe |
Yellow | Suspicious |
Red | High risk |

---

# 📂 Final File Decision

After calculating the risk score:

| Score | Action |
|------|-------|
| < 30 | Move to `/media` |
| ≥ 30 | Move to `/quarantine` |

---

# 🗄️ Cache System

To avoid repeated scans, the scanner uses **SQLite**.

Database location:

```
/scanner/cache/scan_cache.db
```

Table structure:

```
cache
 ├ sha256
 └ result
```

If a file was previously scanned:

```
Cached result: score=XX
```

---

# 🔁 Queue-Based Processing

The scanner processes files asynchronously using:

- `Queue`
- `Thread`

Workflow:

```
enqueue_file(path)
      │
      ▼
Internal queue
      │
      ▼
Worker thread
      │
      ▼
scan_file()
```

This allows the system to process **multiple files without blocking execution**.

---

# 🚀 Running the Scanner

Example:

```
python scanner.py file1.mp4 file2.mp3
```

Each file will be:

1. analyzed
2. scored
3. moved to the appropriate directory

---

# 📁 Directory Structure

```
/scanner
   ├ cache
   │   └ scan_cache.db
   │
   ├ rules
   │   └ yara_rules
   │
   ├ media
   │
   └ quarantine
```

---

# 🧩 Technologies Used

- Python 3
- ClamAV
- VirusTotal API
- YARA
- SQLite
- libmagic
- Python threading + queue

---

# 🎯 Goal

The goal of this scanner is to provide **multi-layer protection against malicious files disguised as media content**.

By combining:

- antivirus scanning
- heuristic detection
- threat intelligence
- rule-based detection

the scanner provides a **reliable malware risk assessment before allowing files into the system**.