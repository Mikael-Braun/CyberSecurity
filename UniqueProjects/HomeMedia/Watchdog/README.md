# 👁️ Watchdog MediaServer

The **Watchdog MediaServer** is a monitoring component responsible for detecting new files uploaded to the server and sending them to the **security scanner** for analysis.

It continuously watches the `/incoming` directory and automatically forwards stable files to the scanner pipeline.

This component ensures that **every file uploaded to the media server is scanned before being processed or served**.

---

# ⚙️ Purpose

The Watchdog acts as a **file ingestion controller** in the media security pipeline.

Responsibilities:

- monitor the `/incoming` directory
- detect newly uploaded files
- ensure the file upload is complete
- avoid scanning the same file multiple times
- send files to the **security scanner queue**

---

# 🧱 System Architecture

```
User Upload
     │
     ▼
/incoming directory
     │
     ▼
Watchdog Monitor
     │
     ├ Check if file upload finished
     ├ Calculate SHA256
     ├ Check if already processed
     │
     ▼
Send file to Scanner Queue
     │
     ▼
Security Scanner
     │
     ▼
MEDIA or QUARANTINE
```

The watchdog is responsible **only for detecting and dispatching files**.

All security analysis happens in the **scanner module**.

---

# 📂 Incoming Directory

The watchdog monitors:

```
/incoming
```

Any file placed in this directory will eventually be processed.

However, the system first verifies that:

1. the file upload is complete
2. the file has not already been processed

---

# ⏳ File Stability Check

Uploads may take time, so the watchdog ensures the file is **fully written** before sending it to the scanner.

The system checks:

```
size1 = file size
wait STABLE_TIME seconds
size2 = file size
```

If both sizes match, the file is considered **stable**.

Configuration:

```
STABLE_TIME = 5 seconds
```

Files with size `0` are ignored.

This prevents:

- scanning partially uploaded files
- scanning corrupted uploads
- race conditions during file writes

---

# 🔐 SHA256 File Identification

Each file is identified using a **SHA256 hash**.

Example function:

```
sha256sum(path)
```

This hash is used to determine if the file has already been processed.

Benefits:

- avoids duplicate scanning
- guarantees unique file identification
- prevents infinite re-processing loops

---

# 🗄️ Processing Cache

The watchdog stores processed file hashes in a **SQLite database**.

Database location:

```
/scanner/cache/watchdog_cache.db
```

Table structure:

```
cache
 └ sha256
```

If a file hash already exists in the database, the file is skipped.

---

# 🔁 Duplicate Prevention

Before sending a file to the scanner, the watchdog checks:

```
SELECT sha256 FROM cache
```

If the hash exists:

```
File is ignored
```

If not:

```
File is sent to scanner
Hash is stored in database
```

This guarantees that **each file is scanned only once**.

---

# 📤 Sending Files to the Scanner

Once the file is validated, the watchdog forwards it to the scanner system:

```
enqueue_file(file)
```

This sends the file to the **scanner queue**, where worker threads will process it asynchronously.

This architecture ensures:

- non-blocking file ingestion
- scalable scanning pipeline
- stable performance under load

---

# ⏱️ Monitoring Loop

The watchdog runs in an **infinite monitoring loop**.

Configuration:

```
CHECK_INTERVAL = 3 seconds
```

Every cycle the system:

1. scans the `/incoming` directory
2. checks each file
3. validates file stability
4. checks the cache
5. forwards new files to the scanner

---

# 🖥️ Console Output

When the service starts:

```
**************************************************
*      [Watchdog] Started – watching /incoming    *
**************************************************
```

Example runtime messages:

```
[Watchdog] File ready: movie.mp4
[Watchdog] Sent to Scanner: movie.mp4
```

Errors are safely handled:

```
[Watchdog] ERROR: <description>
```

---

# 🔁 Continuous Operation

The watchdog runs continuously:

```
while True:
    scan directory
    process files
    sleep
```

This makes it ideal for **server environments and media pipelines**.

---

# 📁 Directory Structure

Example deployment:

```
/scanner
   ├ scanner.py
   ├ watchdog.py
   │
   ├ cache
   │   ├ scan_cache.db
   │   └ watchdog_cache.db
   │
   ├ media
   │
   └ quarantine

/incoming
```

---

# 🧩 Technologies Used

- Python 3
- SQLite
- SHA256 hashing
- filesystem monitoring
- queue-based processing

---

# 🛡️ Security Design

The watchdog is designed to protect the scanning pipeline by ensuring:

- incomplete uploads are never scanned
- files are scanned only once
- duplicate submissions are prevented
- scanner workers receive only valid files

This improves the **stability, security, and efficiency** of the media server.

---

# 🎯 Role in the Security Pipeline

The Watchdog acts as the **entry gate of the security system**.

Responsibilities:

```
Detect files
Validate uploads
Prevent duplicates
Send files to scanner
```

The scanner then performs the **actual malware analysis and classification**.

Together they form a **secure media ingestion pipeline**.