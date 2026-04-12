import psutil
import os
import time

def kill_process(pid):
    try:
        p = psutil.Process(pid)
        name = p.name()
        p.terminate()
        return f"🔥 Killed process: {name}"
    except Exception as e:
        return f"❌ Failed to kill process: {e}"


def is_protected(path, protected_drives):
    return any(path.startswith(drive) for drive in protected_drives)


def clean_temp(safe_paths, protected_drives):
    deleted = 0

    for base in safe_paths:
        base = os.path.expandvars(base)

        if not os.path.exists(base):
            continue

        for root, dirs, files in os.walk(base):

            # EXTRA SAFETY: skip protected drives
            if is_protected(root, protected_drives):
                continue

            for file in files:
                try:
                    file_path = os.path.join(root, file)

                    # HARD BLOCK (double safety)
                    if file_path.startswith("D:\\") or file_path.startswith("F:\\"):
                        continue

                    # Only delete old files (1 day)
                    if time.time() - os.path.getmtime(file_path) > 86400:
                        os.remove(file_path)
                        deleted += 1

                except:
                    pass

    return f"🧹 Safely cleaned {deleted} temp files"
