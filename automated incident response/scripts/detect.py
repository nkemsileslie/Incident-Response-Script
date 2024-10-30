def detect_malicious_ip(malicious_ips):
    with open('/var/log/syslog', 'r') as log_file:
        for line in log_file:
            if any(ip in line for ip in malicious_ips):
                return line.strip()
    return None
