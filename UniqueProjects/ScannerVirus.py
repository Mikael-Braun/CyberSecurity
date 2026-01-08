#!/usr/bin/env python3
"""
Scanner Nível 3
Analisa ficheiros novos e decide se vão para /media ou /quarantine
"""

import os, hashlib, math, sqlite3, subprocess, requests, magic, shutil
from datetime import datetime
import sys

# ---------------- CONFIGURAÇÃO ----------------
VT_API_KEY = os.getenv("VT_API_KEY")  # opcional
CLAMAV_CMD = "clamscan --no-summary"
CACHE_DB = "/cache/scan_cache.db"
MEDIA_DIR = "/media"
QUARANTINE_DIR = "/quarantine"
MAX_ENTROPY = 7.5

ALLOWED_MEDIA_MIME = [
    "audio/mpeg", "audio/flac", "audio/x-wav",
    "video/mp4", "video/x-matroska", "video/x-msvideo"
]

# ---------------- CACHE ----------------
def init_cache():
    os.makedirs(os.path.dirname(CACHE_DB), exist_ok=True)
    conn = sqlite3.connect(CACHE_DB)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS cache (
                 sha256 TEXT PRIMARY KEY,
                 result TEXT)""")
    conn.commit()
    conn.close()

def cache_get(sha256):
    conn = sqlite3.connect(CACHE_DB)
    c = conn.cursor()
    c.execute("SELECT result FROM cache WHERE sha256=?", (sha256,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None

def cache_set(sha256, result):
    conn = sqlite3.connect(CACHE_DB)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO cache VALUES (?,?)", (sha256, result))
    conn.commit()
    conn.close()

# ---------------- UTIL ----------------
def sha256sum(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(8192), b""):
            h.update(block)
    return h.hexdigest()

def entropy(path):
    with open(path,"rb") as f:
        data = f.read()
    if not data: return 0.0
    freq = {}
    for b in data:
        freq[b] = freq.get(b,0)+1
    e = 0.0
    l = len(data)
    for v in freq.values():
        p = v/l
        e -= p*math.log2(p)
    return e

def detect_mime(path):
    return magic.from_file(path, mime=True)

def mime_ok(path):
    mime = detect_mime(path)
    return any(mime.startswith(ok) for ok in ALLOWED_MEDIA_MIME), mime

def clamav_scan(path):
    r = subprocess.run(f"{CLAMAV_CMD} '{path}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if "FOUND" in r.stdout: return "MALICIOUS"
    if "OK" in r.stdout: return "CLEAN"
    return "UNKNOWN"

def virustotal_check(sha):
    if not VT_API_KEY: return "VT_NOT_CONFIGURED"
    headers = {"x-apikey": VT_API_KEY}
    try:
        r = requests.get(f"https://www.virustotal.com/api/v3/files/{sha}", headers=headers, timeout=15)
        if r.status_code==404: return "NOT_IN_DB"
        if r.status_code==200:
            det = r.json()["data"]["attributes"]["last_analysis_stats"]["malicious"]
            return "CLEAN" if det==0 else f"DETECTED_{det}"
    except:
        return "VT_ERROR"

def move_file(src,dst):
    os.makedirs(dst,exist_ok=True)
    shutil.move(src, os.path.join(dst,os.path.basename(src)))

# ---------------- SCAN ----------------
def scan_file(path):
    print(f"\n[Scanner] Scanning {path}")
    sha = sha256sum(path)
    cached = cache_get(sha)
    if cached:
        print(f"🔁 Cached result: {cached}")
        return cached

    mime_okay, mime = mime_ok(path)
    print(f"MIME: {mime}")
    if not mime_okay:
        move_file(path, QUARANTINE_DIR)
        cache_set(sha,"REJECTED_BAD_MIME")
        return "REJECTED_BAD_MIME"

    ent = entropy(path)
    print(f"Entropy: {ent:.2f}")
    if ent>MAX_ENTROPY:
        move_file(path, QUARANTINE_DIR)
        cache_set(sha,"SUSPICIOUS_HIGH_ENTROPY")
        return "SUSPICIOUS_HIGH_ENTROPY"

    clam = clamav_scan(path)
    print(f"ClamAV: {clam}")
    if clam=="MALICIOUS":
        move_file(path, QUARANTINE_DIR)
        cache_set(sha,"MALICIOUS_CLAMAV")
        return "MALICIOUS_CLAMAV"

    vt = virustotal_check(sha)
    print(f"VirusTotal: {vt}")

    move_file(path, MEDIA_DIR)
    result = f"CLEAN_{vt}"
    cache_set(sha,result)
    return result

# ---------------- MAIN ----------------
if __name__=="__main__":
    init_cache()
    if len(sys.argv)<2:
        print("Usage: python3 scanner.py /path/to/file")
        exit(1)
    path = sys.argv[1]
    scan_file(path)
