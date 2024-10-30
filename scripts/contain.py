import os

def contain_suspicious_process(process_info):
    process_id = process_info.split()[1]  # Assumes PID is the second item
    os.kill(int(process_id), 9)  # Kill the process
    print(f"Process {process_id} terminated for containment.")
