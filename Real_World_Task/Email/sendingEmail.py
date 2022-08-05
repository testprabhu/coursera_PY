# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
  
# creates SMTP session
s = smtplib.SMTP('smtp-mail.outlook.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login("saravanaprabhua@hotmail.com", "Nokia@143")
  
# message to be sent
message = "Message_you_need_to_send"
  
# sending the mail
s.sendmail("saravanaprabhua@hotmail.com", "saravanaprabhua@gmail.com", 'Subject: Test Mail')
  
# terminating the session
s.quit()