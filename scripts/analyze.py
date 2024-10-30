import os

def analyze_suspicious_process(suspicious_processes):
    running_processes = os.popen("ps aux").readlines()
    for process in running_processes:
        if any(proc in process for proc in suspicious_processes):
            return process.strip()
    return None
