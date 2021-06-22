import smtplib

sender_username = input("Enter your IITK username: ")
sender_password = input("Enter password: ")

sender = sender_username + '@iitk.ac.in'
receiver = 'harshitr@cse.iitk.ac.in'

message = """From: Stamatics IIT Kanpur <{0}>
To: <{1}>
MIME-Version: 1.0
Content-type: text/html
Subject: {2}
{3}
"""

try:
   s = smtplib.SMTP('mmtp.iitk.ac.in', 25)
   s.starttls()
   s.login(sender_username, sender_password)
   s.sendmail(sender, receiver, message.format(
       sender, receiver, "Subject", "Text"))
   print("Successfully sent email")
except Exception:
   print("Error: unable to send email")
