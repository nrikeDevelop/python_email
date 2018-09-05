import pyxhook
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
import smtplib
import os
import sys

usermail = "USER"
passwordmail = "PASSWORD"

def footer():
	print ""
	print ""
	print "github: nrikeDevelop"
	print ""

def sendEmail(): 

	msg = MIMEMultipart()

#get Data
	exit = 1
	while exit == 1:

		msg['From'] = usermail
		msg['To'] = raw_input("Email_to:	")
		msg['Subject'] = raw_input("Subject:	")
		message = raw_input("Message:	")

		msg.attach(MIMEText(message, 'plain'))

		sendFile = raw_input("Do you want send any file?(y/n):	")

		if sendFile == "y":
			exitFile = 1
			while exitFile == 1:
				pathFile = raw_input("Introduce path file:	")
				if os.path.isfile(pathFile):
					part = MIMEBase('application', "octet-stream")
					part.set_payload(open(pathFile, "rb").read())
					Encoders.encode_base64(part)
					part.add_header('Content-Disposition', 'attachment; filename="file.log"')
					msg.attach(part)
					exitFile = 0
				else:
					print "file no exist"

		is_correct = raw_input("The data is correct? (y/n):	")

		if is_correct == "y":
			exit = 0

	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(usermail, passwordmail)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()

	print "[+]	successfully sent email to %s:" % (msg['To'])

	footer()

##--MAIN--

try:
	sendEmail()
except KeyboardInterrupt:
	footer()
	sys.exit()






"""
BASE:

	-data

	msg = MIMEMultipart()
	msg['From'] = email_from
	msg['To'] = email_to
	msg['Subject'] = subject
	message = message

	-file

	part = MIMEBase('application', "octet-stream")
	part.set_payload(open(PATHFILE, "rb").read())
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="NAMEFILE"')
	msg.attach(part)

	-server

	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(USER_EMAIL, PASSWORD_EMAIL)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()
"""

