from email.message import EmailMessage  # <-- fixed this line
from password import password          # <-- make sure you have password defined in password.py

import ssl
import smtplib

email_sender = 'ismailarshad99699@gmail.com'
email_password = password
email_receiver = 'sheikhmuhammadismail79@gmail.com'  # <-- replace with actual email

subject = 'Like This Page'
body = "My First Python Email Sender"

# Create the email message
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Set up secure connection
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
