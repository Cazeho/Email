import tkinter as tk
from tkinter import *
import os
from firebase import firebase
from datetime import datetime
import json
import binascii
from ecdsa import SigningKey,BRAINPOOLP160r1
import base64
import sys
from base64 import b64decode,b64encode

root= tk.Tk()
fonte =font=('Arial', '11')
canvas1 = tk.Canvas(root, width = 500, height = 500)
canvas1.pack()


label_normal = tk.Label(root,text="",fg='green',font=('helvetica', 12, 'bold'))
label_normal.place(x=100,y=300)
#label_normal.pack()
var_modifiable = tk.StringVar()
label_modifiable = tk.Label(root, textvariable=var_modifiable)
#label_modifiable.pack()
##################
label_normal2 = tk.Label(root,text="",fg='green',font=('helvetica', 12, 'bold'))
label_normal2.place(x=100,y=250)
#label_normal.pack()
var_modifiable2 = tk.StringVar()
label_modifiable2 = tk.Label(root, textvariable=var_modifiable2)
##################
label_normal3 = tk.Label(root,text="",fg='green',font=('helvetica', 12, 'bold'))
label_normal3.place(x=100,y=200)
#label_normal.pack()
var_modifiable3 = tk.StringVar()
label_modifiable3 = tk.Label(root, textvariable=var_modifiable3)
######################
label_normal4 = tk.Label(root,text="",font=('helvetica', 12, 'bold'))
label_normal4.place(x=220,y=140)
#label_normal.pack()
var_modifiable4 = tk.StringVar()
label_modifiable4 = tk.Label(root, textvariable=var_modifiable4)
####################


inf= tk.Entry(root, font=fonte, bg='white', fg='black',width=50)#entrée des adresses
inf.place(x=20,y=100)#emplacement de l'objet
a="jhgkdhk"

##################################################################
firebase = firebase.FirebaseApplication("https://email-signature-920bd.firebaseio.com/", None)
goresult = firebase.get('/email-signature-920bd/keys/', '')
js=json.dumps(goresult)

#############
print(100*"=")
print(js)
data_list=[]
data_key=[]
for x in goresult.values():
  data_key.append(x["Ecdsa-public-key"])
  data_list.append(x)



#################
print(100*"=")
print(data_list[0])
print(100*"=")
print(data_key)

r=data_key[0].replace("b","").replace("\\n",'\n').replace("\'","").encode()
print(r)
cur=BRAINPOOLP160r1
sk = SigningKey.generate(curve=cur)
vk3 = sk.get_verifying_key().from_pem(((r)))
print(vk3)
msg="Hello"

#################################################################
def hello ():
    #label1 = tk.Label(root, text= 'Hello World!', fg='green', font=('helvetica', 12, 'bold'))
    #label2 = tk.Label(root, text= "email: "+a,fg='green', font=('helvetica', 12, 'bold'))
    #canvas1.create_window(150, 200, window=label1)
    #canvas1.create_window(150, 250, window=label2)
    choix1 = inf.get()
    print(base64.b64decode(inf.get()))
    print(vk3.verify(base64.b64decode(inf.get()), msg.encode()))
    z=vk3.verify(base64.b64decode(inf.get()), msg.encode())
    #######################
    i = 0

    
    while i < len(data_key):
      print(i,"aaaaaa")
      if (sk.get_verifying_key().from_pem(((data_key[i].replace("b","").replace("\\n",'\n').replace("\'","").encode())))).verify(base64.b64decode(inf.get()), msg.encode())==True:
            #print(True,"aaaa")
            #print(data_list[i])
            bg=data_list[i]
            data=[]
            for o in bg.values():
                #print(o)
                data.append(o)
            #print(data)
            label_normal4.config(text="Signatures match: True",fg='green')
            label_normal3.config(text="Email: "+data[1])
            label_normal2.config(text="Name: "+data[2])
            label_normal.config(text="Timestamp: "+data[3])
            break
        
      i += 1
    else:
        label_normal4.config(text="Signatures match: False",fg='red')
        label_normal3.config(text="")
        label_normal2.config(text="")
        label_normal.config(text="")
    ##################
    #if z==True:
     #   label_normal4.config(text="Signatures match: True",fg='green')
      #  label_normal3.config(text="Email: "+"hfhfhfh")
       # label_normal2.config(text="Name: "+"hfhfhfh")
       # label_normal.config(text="Timestamp: "+choix1)
   # else:
    #    label_normal4.config(text="Signatures match: False",fg='red')
     #   label_normal3.config(text="")
      #  label_normal2.config(text="")
      #  label_normal.config(text="")
    #print(inf.get())
    

    
button1 = tk.Button(text='Verifier',command=hello, bg='brown',fg='white')
canvas1.create_window(170, 150, window=button1)



root.mainloop()
