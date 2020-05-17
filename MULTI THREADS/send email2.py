import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
sender="gujjalapatiraju@gmail.com"
receiver="gujjalapatiraju@gmail.com"

msg=MIMEMultipart()
msg['From']='gujjalapatiraju@gmail.com'#
msg['To']='gujjalapatiraju@gmail.com'
msg['Subject']="checking this mail"
body="hi raju garu! how are you<br>new line"
msg.attach(MIMEText(body,'html\n'))#giving body in html .so, that we can add html keys to load data.
filename="MYSQL"
#filename1='screenshot'
fileattach=open(r'C:\Users\New\OneDrive\Desktop/MY SQL.txt','rb')
#fileattach1=open(r'C:\Users\New\OneDrive\Pictures\Screenshots/2018-08-20.png','rb')
p = MIMEBase('application', 'txt') 
  
# To change the payload into encoded form 
p.set_payload((fileattach.read()) )
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security

s.starttls() 
  
# Authentication 
s.login(sender, "RRRnani@123$") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(sender, receiver, text) 
  
# terminating the session 
s.quit() 


