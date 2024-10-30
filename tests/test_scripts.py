import unittest
from scripts.detect import detect_malicious_ip
from scripts.analyze import analyze_suspicious_process
from scripts.contain import contain_suspicious_process
from scripts.notify import send_alert

class TestIncidentResponseScripts(unittest.TestCase):

    def test_detect_malicious_ip(self):
        malicious_ips = ["203.0.113.5"]
        result = detect_malicious_ip(malicious_ips)
        self.assertIsNone(result, "No malicious IP should be detected in a clean log")

    def test_analyze_suspicious_process(self):
        suspicious_processes = ["netcat"]
        result = analyze_suspicious_process(suspicious_processes)
        self.assertIsNone(result, "No suspicious process should be detected in a clean environment")

    def test_notify(self):
        try:
            send_alert("Test Alert", "This is a test alert.")
            success = True
        except Exception as e:
            success = False
        self.assertTrue(success, "Sending alert should not raise an exception")

if __name__ == "__main__":
    unittest.main()
