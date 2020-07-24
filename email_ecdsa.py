import os
from firebase import firebase
from datetime import datetime
import json

import binascii
from ecdsa import SigningKey,BRAINPOOLP160r1
import base64
import sys

from base64 import b64decode,b64encode

cur=BRAINPOOLP160r1
sk = SigningKey.generate(curve=cur)
vk = sk.get_verifying_key()
vk_pem=vk.to_pem()
vk2 = sk.get_verifying_key().from_pem((vk_pem))
print(vk)
print(vk2)

firebase = firebase.FirebaseApplication("https://email-signature-920bd.firebaseio.com/", None)
datetime=str(datetime.now())
data =  { "Name": "philippe",
          "Email": "phmanuel1@gmail.com",
          "Ecdsa-public-key": str(vk_pem),
          "Timestamp": datetime
          }

#print(data)

#####envoie
result = firebase.post('/email-signature-920bd/keys/',data)
#print(result)
#####receive
goresult = firebase.get('/email-signature-920bd/keys/', '')
a=json.dumps(goresult)
y=json.loads(a)
data_list=[]
data_key=[]
print(y)
print(10*"=")
for x in goresult.values():
  print(x)
  print(data_key.append(x["Ecdsa-public-key"]))
  data_list.append(x)
print(10*"=")
for x, y in goresult.items():
  print(x, y)


print(10*"=")
print(data_list[0],"bbbbbbbbbbbb")
print(10*"=")
for x in data_list[0].values():
    print((x))

print(10*"=")
print(goresult.values(),"aaaaa")
print(10*"=")

print(data_list[0].values())


print(data_key)


print(data_list)


#####################
i=-1
for j in data_key:
    print(j)
    i=i+1
    print(i)
    #if a==true





print(45*"=")


msg="Hello"
type = 1





signature = sk.sign(msg.encode())

print("Message:\t",msg)
print("Type:\t\t",cur.name)
print("=========================")

print("Signature:\t",base64.b64encode(signature))

print("private:" ,sk.to_string().hex())
print("public:" ,vk.to_string().hex())

print("=========================")

print("Signatures match:\t",vk.verify(signature, msg.encode()))

print(data_key[0])
a=data_key[0].replace("b","").replace("\\n",'\n').replace("\'","").encode()
print(a)
print((vk_pem).__class__)
print((a).__class__)

vk3 = sk.get_verifying_key().from_pem(((a)))
print(vk3)
#print(vk3.verify(signature, msg.encode()))
print(100*"=")
print(data_key[0])
