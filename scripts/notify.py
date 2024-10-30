import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "your_email@example.com"
    msg["To"] = "security_team@example.com"

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your_email@example.com", "your_password")
        server.sendmail("your_email@example.com", ["security_team@example.com"], msg.as_string())

    print("Alert sent to security team.")
