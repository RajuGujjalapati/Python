
import smtplib
def gmailsend(body):
	server = 'smtp.gmail.com'
	port = 587
	sender = 'gujjalapatiraju@gmail.com'
	password = 'RRRnani@123$'
	receivers = 'gujjalapatiraju@gmail.com'
	fromPerson = 'TechOffice Automation'#masking
	subject = 'Application Health Check - Automated'
	message = "From:"+fromPerson+"\nTo:"+receivers+"\nMIME-Version: 1.0\nContent-Type: text/html\nSubject: "+\
                  subject+"\n\n\n\nHi<br><br> Please find the below checks <br><br>"+body
	smtpObj = smtplib.SMTP(server,int(port))
	smtpObj.starttls()#root  'tls' is the road(path) to connect the with server
	smtpObj.login(sender,password) 
	smtpObj.sendmail(sender,receivers.split(';'),message)
	
	print("Mail Sent Successfully")
gmailsend("test succesfully")



