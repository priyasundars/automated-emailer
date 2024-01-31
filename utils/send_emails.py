import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import dotenv_values


def send_emails(html_content, recipient_emails):

    # Current date
    today = datetime.today()
    formatted_date = today.strftime("%b %d %Y")
    print(formatted_date)

    # Load environment variables from .env file
    env_vars = dotenv_values(".env")

    # Access the SMTP credentials
    smtp_username = env_vars["SMTP_USERNAME"]
    smtp_password = env_vars["SMTP_PASSWORD"]

    # Set up the email details
    sender_email = smtp_username
    subject = f"Financial Rates {formatted_date}"

    # Create a multipart message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = ", ".join(recipient_emails)  # Join recipient emails with commas
    print(msg["To"])
    msg["Subject"] = subject

    # Attach the message to the email as plain text
    msg.attach(MIMEText(html_content, "html"))

    # Set up the SMTP server
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        print('logged in...')
        server.sendmail(sender_email, recipient_emails, msg.as_string())
