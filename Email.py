import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email="test@gmail.com"
reciver_email="test@gmail.com"
password="******"

msg=MIMEMultipart()
msg['From']=sender_email
msg['To']=reciver_email
msg['Subject']='EMAILING USING PYTHON'

body="IM USING PYTHON TO SEND EMAIL AND REALLY ITS EASY AND FUNNY"
msg.attach(MIMEText(body))
text=msg.as_string()

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.ehlo()
server.login(sender_email,password)
server.sendmail(sender_email,reciver_email,text)

server.quit()