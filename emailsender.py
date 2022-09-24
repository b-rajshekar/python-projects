from email.message import EmailMessage
from app import password
import ssl
import smtplib

email_sender = "shekarmartinz@gmail.com"
email_password = ""

email_receiver = "brajashekhar19@gmail.com"

subject = "subject"
body = """
#Write your mail body
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

