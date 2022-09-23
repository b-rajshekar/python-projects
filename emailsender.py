from email.message import EmailMessage
from app import password
import ssl
import smtplib

email_sender = "shekarmartinz@gmail.com"
email_password = "hkfrjffolqbwkqda"

email_receiver = "brajashekhar19@gmail.com"

subject = "MYKL Plant Codes"
body = """
1001 - Rudraram
2900 - Sotanala
3102 - Perundurai
2902 - Kaharani
1501 - Kalol
1012 - Piduguralla
3105 - CNA
2903 - Behror
2101 - Indore
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

