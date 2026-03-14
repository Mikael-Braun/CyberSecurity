#!/usr/bin/env python3
"""
Watchdog MediaServer – versão estável e segura
"""
import time, hashlib, sqlite3, sys
from pathlib import Path
from scanner import enqueue_file

sys.stdout.reconfigure(line_buffering=True)

INCOMING = Path("/incoming")
CHECK_INTERVAL = 3
STABLE_TIME = 5  # segundos sem mudar de tamanho
DB_PATH = Path("/scanner/cache/watchdog_cache.db")
LINE_WIDTH = 80

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
conn.execute("""
CREATE TABLE IF NOT EXISTS cache (
    sha256 TEXT PRIMARY KEY
)
""")
conn.commit()
conn.close()

def sha256sum(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(8192), b""):
            h.update(block)
    return h.hexdigest()

def is_processed(sha):
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute(
            "SELECT 1 FROM cache WHERE sha256=?",
            (sha,)
        ).fetchone() is not None

def mark_processed(sha):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR IGNORE INTO cache VALUES (?)",
            (sha,)
        )
        conn.commit()

def is_stable(path):
    size1 = path.stat().st_size
    if size1 == 0:
        return False
    time.sleep(STABLE_TIME)
    size2 = path.stat().st_size
    return size1 == size2

print("*" * LINE_WIDTH)
print("*" + "[Watchdog] Iniciado, a vigiar /incoming".center(LINE_WIDTH - 2) + "*")
print("*" * LINE_WIDTH)

while True:
    try:
        for file in INCOMING.iterdir():
            if not file.is_file():
                continue

            if not is_stable(file):
                continue

            sha = sha256sum(file)

            if is_processed(sha):
                continue

            print(f"[Watchdog] Ficheiro pronto: {file.name}")
            enqueue_file(str(file))
            mark_processed(sha)
            print(f"[Watchdog] Enviado ao Scanner: {file.name}")

    except Exception as e:
        print(f"[Watchdog] ERRO: {e}")

    time.sleep(CHECK_INTERVAL)
