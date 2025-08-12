import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASS

def send_email(to_email, subject, body, sender_name=""):
    try:
        msg = MIMEMultipart()
        msg['From'] = f"{sender_name} <{SMTP_USER}>" if sender_name else SMTP_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))  # texto plano

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Error enviando email: {str(e)}")
        return False
