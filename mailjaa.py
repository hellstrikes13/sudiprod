#!/usr/bin/python
import smtplib,datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
html="test mail blah blah blah..."
smpt_sername = "blah"
smtp_pass      = "blah"
tx = "sender@blah.com"
rx1 = "receiver@blah.com"
rx2 = "receiver2@blah.com"
def mailhandler(subject, message, recipients=None):
    msg = MIMEMultipart('alternative')
    if not recipients:
        return
    mailer = smtplib.SMTP('smtp.sendgrid.net', 465)
    mailer.starttls()
    mailer.login(smptp_username,smtp_pass)
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    msg['From'] = tx
    part = MIMEText(message, 'html')
    msg.attach(part)
    mailer.sendmail(msg['From'], recipients, msg.as_string())
mailhandler(subject="test123",message=html,recipients=[rx1,rx2])
print 'mail sent'
