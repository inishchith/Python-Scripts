#Sending a mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = ""
toaddr = ""
#Parts of email

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "PyMail test"

body = "this is smtplib"
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587) #465 or 587 open
server.starttls()
# your login details
server.login(fromaddr, "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("email sent successfully")
server.quit()