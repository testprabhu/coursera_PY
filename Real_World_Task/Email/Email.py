from email.message import EmailMessage
import os.path
import mimetypes
import smtplib
import getpass

attachment_path = "D:/Trainings & Certification Works/GitHub_Repo/coursera_PY/Real_World_Task/report.pdf"
message = EmailMessage()
print(message)
sender = "saravanaprabhua@hotmail.com"
recipient = "saravanaprabhua@gmail.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = "Greetings from {} to {}".format(sender, recipient)
body = """Hey There!

I am learning to send emails using Python!
"""
message.set_content(body)
print(message)

attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=os.path.basename(attachment_path))
 
print(message)

mail_server = smtplib.SMTP('smtp-mail.outlook.com', 587)
mail_server.set_debuglevel(1)
mail_server.starttls() #require for secure connection, without this it won't work
mail_pass = getpass.getpass('Password? ')
print(mail_pass)
mail_server.login(sender, mail_pass)
#mail_server.login("saravanaprabhua@hotmail.com", "Nokia@143")
mail_server.send_message(message)
mail_server.quit()
