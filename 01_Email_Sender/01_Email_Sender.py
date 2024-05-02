# Import necessaries modules
from email.message import EmailMessage
from app2 import password
import ssl
import smtplib


email_sender = 'robertomartinromoo@gmail.com' # Email where we sending the message from
my_password = password # Password stored in other file

email_receiver = "" # Email where we want to send the message

# What we are going to send as subject and body
subject = 'This is an email sender'
body = """ This is my first Python project, let's go for more"""

# Definition of parameters needed to send the message
email = EmailMessage()
email['From'] = email_sender
email['To'] = email_receiver
email['subject'] = subject
email.set_content(body)

context = ssl.create_default_context()

# We finally send the message by assigning an email to email_receiver that we have to do it manually
with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())