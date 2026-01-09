from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os


SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_FROM = os.getenv("EMAIL_FROM")


async def send_otp(email: str, otp: int) -> bool:
    if not email or not otp:
        return False
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_FROM
        msg["To"] = email
        msg["Subject"] = "Your One Time Password"
        body = f"Thank you for registraion. Your One Time Password is: {otp}"

        msg.attach(MIMEText(body, "html"))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg=msg)

            return True

    except Exception as e:
        return False
