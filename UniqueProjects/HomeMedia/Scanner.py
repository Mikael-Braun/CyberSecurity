#!/usr/bin/env python3                                                                                       
"""                                                                                                          
Scanner Nível 3 - Completo com Queue                                                                         
Inclui: entropia, ClamAV, VirusTotal, strings suspeitas, MIME, tamanho suspeito, cache                       
Saída alinhada e barra de risco (bolas removidas)                                                            
Fila interna para processar múltiplos ficheiros                                                              
Versão robusta com melhorias de leitura e timeout                                                            
"""                                                                                                          
                                                                                                             
import os, hashlib, math, sqlite3, subprocess, requests, magic, shutil                                       
from queue import Queue                                                                                      
from threading import Thread                                                                                 
                                                                                                             
# ---------------- CONFIGURAÇÃO ----------------                                                             
VT_API_KEY = os.getenv("VT_API_KEY")                                                                         
CLAMAV_CMD = "clamscan --no-summary"                                                                         
CACHE_DB = "/scanner/cache/scan_cache.db"                                                                    
MEDIA_DIR = "/media"                                                                                         
QUARANTINE_DIR = "/quarantine"                                                                               
MAX_ENTROPY = 7.5
LINE_WIDTH = 80
CHECK_SIZE_MIN = 10      # B, muito pequeno pode ser suspeito
CHECK_SIZE_MAX = 1024*1024*1024*2  # 2GB

ALLOWED_MEDIA_MIME = [
    "audio/mp3", "audio/flac", "audio/x-wav",
    "video/mp4", "video/x-matroska", "video/x-msvideo"
]

SUSPICIOUS_STRINGS = ["eval(", "exec(", "base64", "cmd.exe", "powershell", "malware"]

# ---- YARA SCORE POLICY ----
YARA_QUARANTINE_RULES = {
    "MEDIA_Embedded_Executable",
    "MEDIA_Header_Mismatch",
    "MEDIA_Double_Extension"
}

YARA_SCORE_RULES = {
    "MEDIA_Suspicious_Strings",
    "MEDIA_Abnormal_Entropy"
}



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
    freq = {}
    total = 0
    try:
        with open(path,"rb") as f:
            while chunk := f.read(8192):
                total += len(chunk)
                for b in chunk:
                    freq[b] = freq.get(b,0)+1
        if total == 0: return 0.0
        e = 0.0
        for v in freq.values():
            p = v/total
            e -= p*math.log2(p)
        return e
    except Exception as ex:
        print(f"[Scanner] ERRO ao calcular entropia de {path}: {ex}", flush=True)
        return 0.0

def detect_mime(path):
    try:
        return magic.from_file(path, mime=True)
    except Exception as ex:
        print(f"[Scanner] ERRO ao detectar MIME de {path}: {ex}", flush=True)
        return "unknown/unknown"

def clamav_scan(path):
    try:
        r = subprocess.run(f"{CLAMAV_CMD} '{path}'", shell=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           text=True, timeout=30)
        if "FOUND" in r.stdout: return "MALICIOUS"
        if "OK" in r.stdout: return "CLEAN"
        return "UNKNOWN"
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    except Exception as ex:
        print(f"[Scanner] ERRO ClamAV em {path}: {ex}", flush=True)
        return "ERROR"

def virustotal_check(sha):
    if not VT_API_KEY: return "VT_NOT_CONFIGURED"
    headers = {"x-apikey": VT_API_KEY}
    try:
        r = requests.get(f"https://www.virustotal.com/api/v3/files/{sha}", headers=headers, timeout=15)
        if r.status_code==404: return "NOT_IN_DB"
        if r.status_code==200:
            det = r.json()["data"]["attributes"]["last_analysis_stats"]["malicious"]
            return f"DETECTED {det}" if det>0 else "CLEAN"
        print(f"[Scanner] VT status inesperado {r.status_code} para {sha}", flush=True)
        return "VT_ERROR"
    except Exception as ex:
        print(f"[Scanner] ERRO VirusTotal em {sha}: {ex}", flush=True)
        return "VT_ERROR"

def suspicious_strings(path):
    found = []
    try:
        with open(path,"rb") as f:
            data = f.read().decode(errors="ignore")
            for s in SUSPICIOUS_STRINGS:
                if s in data:
                    found.append(s)
    except Exception as e:
        print(f"[Scanner] ERRO ao ler strings de {path}: {e}", flush=True)
    return found

def yara_scan(path):
    matches = []
    try:
        rules = yara.compile(filepath={
            f: os.path.join(YARA_RULES_DIR, f)
            for f in os.listdir(YARA_RULES_DIR)
            if f.endswith(".yar") or f.endswith(".yara")
        })
        matches = rules.match(path)
    except Exception as e:
        print(f"[Scanner] ERRO YARA: {e}", flush=True)
    return [m.rule for m in matches]



def color_text(text,color):
    colors = {
        "red":"\033[91m",
        "yellow":"\033[93m",
        "green":"\033[92m",
        "blue":"\033[94m",
        "reset":"\033[0m"
    }
    return f"{colors.get(color,'')}{text}{colors['reset']}"

def move_file(src,dst):
    os.makedirs(dst,exist_ok=True)
    shutil.move(src, os.path.join(dst,os.path.basename(src)))

def print_box_line(text="", color="reset"):
    print("*" + color_text(text.ljust(LINE_WIDTH-2), color) + "*")

# ---------------- SCAN ----------------
def scan_file(path):
    init_cache()

    print("*"*LINE_WIDTH)
    print_box_line(f"A analisar ficheiro: {os.path.basename(path)}", "blue")

    sha = sha256sum(path)
    cached = cache_get(sha)
    if cached:
        print_box_line(f"Resultado em cache: {cached}", "yellow")
        return cached

    size = os.path.getsize(path)
    mime = detect_mime(path)
    ent = entropy(path)
    ent_status = "BAIXA" if ent<4 else "NEUTRA" if ent<7 else "ALTA"
    ent_color = "green" if ent<4 else "yellow" if ent<7 else "red"

    clam = clamav_scan(path)
    clam_color = "green" if clam=="CLEAN" else "yellow" if clam=="UNKNOWN" else "red"
    vt = virustotal_check(sha)
    vt_color = "green" if vt=="CLEAN" else "red" if vt in ["VT_NOT_CONFIGURED","NOT_IN_DB"] else "yellow"

    strings_found = suspicious_strings(path)
    strings_color = "green" if not strings_found else "red"

    yara_matches = yara_scan(path)
    yara_color = "green" if not yara_maches else "red"


    mime_ok = any(mime.startswith(ok) for ok in ALLOWED_MEDIA_MIME)
    mime_color = "green" if mime_ok else "red"

    size_color = "green" if CHECK_SIZE_MIN<size<CHECK_SIZE_MAX else "red"
    size_status = "OK" if CHECK_SIZE_MIN<size<CHECK_SIZE_MAX else "SUSPEITO"

    print_box_line(f"Tamanho: {size/1024:.2f} KB ({size_status})", size_color)
    print_box_line(f"MIME: {mime}", mime_color)
    print_box_line(f"SHA256: {sha}", "blue")
    print_box_line(f"Entropia: {ent:.2f} ({ent_status})", ent_color)
    print_box_line(f"ClamAV: {clam}", clam_color)
    print_box_line(f"VirusTotal: {vt}", vt_color)
    str_display = ", ".join(strings_found) if strings_found else "Nenhuma encontrada"
    print_box_line(f"Strings suspeitas: {str_display}", strings_color)
    print_box_line(f"Yara: {yara_matches}", yara_color)


    score = 0
    if ent_status=="ALTA": score += 20
    if clam_color=="red": score += 20
    if vt_color=="red": score += 30
    if strings_found: score += 25
    if not mime_ok: score += 10
    if size_status=="SUSPEITO": score += 10
    if score>100: score=100

    for rule in yara_matches:
        if rule in YARA_QUARANTINE_RULES:
            score += 40
        elif rule in YARA_SCORE_RULES:
            score += 20


    risk_color = "green" if score<30 else "yellow" if score<60 else "red"
    bar_len = LINE_WIDTH-50
    filled = int(bar_len * score / 100)
    bar = "[" + "#"*filled + "-"*(bar_len-filled) + "]"
    print_box_line(f" Probabilidade de ser malware: {bar} {score}%", risk_color)

    final_dir = MEDIA_DIR if score<30 else QUARANTINE_DIR
    move_file(path, final_dir)
    print_box_line(f"Resultado final: {' MEDIA' if final_dir==MEDIA_DIR else 'QUARANTINE'}")
    print_box_line(f"Movido para: {final_dir}","blue")
    print("*"*LINE_WIDTH)

    cache_set(sha, f"score={score}")
    return score

# ---------------- QUEUE ----------------
file_queue = Queue()

def worker():
    while True:
        path = file_queue.get()
        if path is None:
            break
        scan_file(path)
        file_queue.task_done()

thread = Thread(target=worker, daemon=True)
thread.start()

def enqueue_file(path):
    """Adicionar ficheiro à queue do scanner"""
    file_queue.put(path)

# ---------------- TESTE ----------------
if __name__ == "__main__":
    import sys
    for f in sys.argv[1:]:
        enqueue_file(f)
    file_queue.join()
