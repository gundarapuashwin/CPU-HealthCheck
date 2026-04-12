import psutil

def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_ram():
    return psutil.virtual_memory().percent

def get_disk():
    return psutil.disk_usage('C:\\').percent


def get_heavy_process():
    processes = []

    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            proc = psutil.Process(p.info['pid'])
            priority = proc.nice()

            processes.append({
                "pid": p.info['pid'],
                "name": p.info['name'],
                "cpu": p.info['cpu_percent'],
                "priority": priority
            })

        except:
            pass

    processes.sort(key=lambda x: x['cpu'], reverse=True)

    return processes[0] if processes else None
