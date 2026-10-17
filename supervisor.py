import subprocess
import time
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "supervisor.log")

def log(msg):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] [Supervisor:8090] {msg}"
    try:
        print(line, flush=True)
    except Exception:
        pass
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass

log("Starting Basit AI Interview Pro Python Supervisor...")

while True:
    try:
        log("Spawning node server.js...")
        proc = subprocess.Popen(
            ["node", "server.js"],
            cwd=BASE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1
        )
        log(f"Spawned PID: {proc.pid}")

        for line in proc.stdout:
            try:
                sys.stdout.write(line)
                sys.stdout.flush()
            except Exception:
                pass

        proc.wait()
        log(f"Node server exited with code {proc.returncode}. Restarting in 3 seconds...")
        time.sleep(3)
    except Exception as e:
        log(f"Supervisor error: {e}. Retrying in 5 seconds...")
        time.sleep(5)
