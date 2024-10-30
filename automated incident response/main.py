import yaml
import logging
from scripts.detect import detect_malicious_ip
from scripts.analyze import analyze_suspicious_process
from scripts.contain import contain_suspicious_process
from scripts.notify import send_alert

# Configure logging
logging.basicConfig(filename='logs/incident_logs.log', level=logging.INFO)

# Load configuration
with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

def main():
    logging.info("Starting Incident Response Script...")

    # Detection Phase
    ip_alert = detect_malicious_ip(config['malicious_ips'])
    process_alert = analyze_suspicious_process(config['suspicious_processes'])

    # Containment and Notification Phases
    if ip_alert:
        send_alert("Malicious IP Detected", f"Detected suspicious IP: {ip_alert}")
        logging.info(f"Alert sent for malicious IP: {ip_alert}")
        
    if process_alert:
        contain_suspicious_process(process_alert)
        send_alert("Suspicious Process Contained", f"Contained process: {process_alert}")
        logging.info(f"Process {process_alert} contained successfully.")

    logging.info("Incident Response Script completed.")

if __name__ == "__main__":
    main()
