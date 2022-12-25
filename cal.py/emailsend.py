import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = ''
email_password = ''
email_send = ''

subject = 'Subject of the email'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

filename='example.txt'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

server.sendmail(email_user,email_send,text)
server.quit()

# Path: emailsend.py
# Compare this snippet from randompasswordgen.py:
# import string
# from random import *
# characters = string.ascii_letters + string.punctuation  + string.digits

# len_characters = int(input("How long should the password be?"))



