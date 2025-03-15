import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import dotenv_values
from typing import List

def send_emails(html_content: str, recipients: List[str], subject: str) -> None:
    """
    Send emails to multiple recipients using Office365 SMTP
    
    Args:
        html_content (str): Rendered HTML template content
        recipients (List[str]): List of recipient email addresses
        subject (str): Email subject line
        
    Raises:
        ValueError: If SMTP credentials are missing
        smtplib.SMTPException: For SMTP-related errors
    """
    try:
        # Load environment variables
        env_vars = dotenv_values(".env")
        if not all(key in env_vars for key in ["SMTP_USERNAME", "SMTP_PASSWORD"]):
            raise ValueError("❌ Missing SMTP credentials in .env file")

        smtp_username = env_vars["SMTP_USERNAME"]
        smtp_password = env_vars["SMTP_PASSWORD"]

        # Create SMTP connection
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            print(f"🔑 Authenticated as {smtp_username}")

            # Send to each recipient individually for better tracking
            for email in recipients:
                try:
                    msg = MIMEMultipart()
                    msg["From"] = smtp_username
                    msg["To"] = email
                    msg["Subject"] = subject
                    msg.attach(MIMEText(html_content, "html"))
                    
                    server.sendmail(smtp_username, email, msg.as_string())
                    print(f"✉️ Sent to {email}")
                    
                except smtplib.SMTPException as e:
                    print(f"⚠️ Failed to send to {email}: {str(e)}")
                    continue

    except smtplib.SMTPException as e:
        print(f"🚨 SMTP Error: {str(e)}")
        raise
    except Exception as e:
        print(f"💥 Unexpected error: {str(e)}")
        raise
