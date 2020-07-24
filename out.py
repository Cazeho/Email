import win32com.client
from os import path
#####send

outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
#mail.To = 'romain.manuel22@gmail.com'#'romain.manuel@etu.univ-cotedazur.fr'
#mail.Subject = 'Hello this is you!'
#mail.Body = 'Hello!!!!!!'
#mail.HTMLBody = '<h2>This is an H2 message</h2>' #this field is optional

# To attach a file to the email (optional):
#attachment  = "C:/Users/OneDrive/Documents/Desktop/Social_Network_Ads.csv"
#mail.Attachments.Add(attachment)

#mail.Send()

#########read

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder




messages = inbox.Items
import sys

message = messages.GetFirst()
attachments=message.Attachments
rec_time = message.CreationTime
body_content = message.body
subj_line = message.subject

while message:
        print(message.subject,message.CreationTime,message.body)#,(message.Sender.GetExchangeUser().PrimarySmtpAddress)
        message = messages.GetNext()
	



