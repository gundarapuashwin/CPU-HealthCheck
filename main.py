import time
import json
import random

from monitor import get_cpu, get_ram, get_disk, get_heavy_process
from actions import kill_process, clean_temp
from logger import log

# Load config
with open("config.json") as f:
    config = json.load(f)

CPU_LIMIT = config["cpu_limit"]
RAM_LIMIT = config["ram_limit"]
DISK_LIMIT = config["disk_limit"]
INTERVAL = config["check_interval"]

PROTECTED_PROCESSES = config["protected_processes"]
PROTECTED_DRIVES = config["protected_drives"]
SAFE_PATHS = config["safe_cleanup_paths"]

LOW_PRIORITY = 10
SAFE_CPU_THRESHOLD = 10

roasts = [
    "Bro this laptop is struggling 😭",
    "Too many apps open, chill!",
    "Even I am tired watching this CPU 💀"
]

print("🛡️ Self-Healing System Started...")

while True:
    cpu = get_cpu()
    ram = get_ram()
    disk = get_disk()

    print(f"CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")

    # 🔥 CPU Healing
    if cpu > CPU_LIMIT:
        print("⚠️ High CPU detected")
        print(random.choice(roasts))

        proc = get_heavy_process()

        if proc:
            name = proc["name"]
            pid = proc["pid"]
            cpu_usage = proc["cpu"]
            priority = proc["priority"]

            # Skip protected apps
            if name in PROTECTED_PROCESSES:
                print(f"🛑 Skipping protected process: {name}")
                continue

            # Skip efficiency-like processes
            if priority >= LOW_PRIORITY or cpu_usage < SAFE_CPU_THRESHOLD:
                print(f"🛑 Skipping {name} (efficiency-mode-like)")
                continue

            msg = kill_process(pid)
            print(msg)
            log(msg)

    # 🧠 RAM warning
    if ram > RAM_LIMIT:
        msg = "⚠️ High RAM usage detected"
        print(msg)
        log(msg)

    # 💾 Disk cleaning
    if disk > (100 - DISK_LIMIT):
        print("⚠️ Low disk space detected")
        msg = clean_temp(SAFE_PATHS, PROTECTED_DRIVES)
        print(msg)
        log(msg)

    time.sleep(INTERVAL)
