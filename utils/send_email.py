import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import dotenv_values



def send_email(html_content):    
    # Load environment variables from .env file
    env_vars = dotenv_values('.env')

    # Access the SMTP credentials
    smtp_username = env_vars['SMTP_USERNAME']
    smtp_password = env_vars['SMTP_PASSWORD']


    # Set up the email details
    sender_email = smtp_username
    receiver_email = 'receiveremail'
    subject = 'Urgent call'
    # html_content = '<h1>Accounts dept urgent</h1>'

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the email as plain text
    msg.attach(MIMEText(html_content, 'html'))

    # Set up the SMTP server
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    smtp_username = smtp_username
    smtp_password = smtp_password

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
