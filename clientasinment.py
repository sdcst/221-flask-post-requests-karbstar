#!python3

import json, requests
qrep=True
ql=[]
url = "http://10.22.103.18:5000/going"
while qrep==True:
    newq=input('give a quote:')
    ql.append(newq)
    cqrep=True
    while cqrep==True:
        yn=input('continue adding quotes y/n')
        if yn=='n':
            cqrep=False
            qrep=False
        elif yn=='y':
            cqrep=False
payload={'quote' : ql, 'get' :'bce52a22495d704233dd4e720e942dbf63d0561ed813d77fd38776357db7108e'}
response = requests.post(url,data=payload)
print(f"The response is {response}")
print(f"The response text is {response.text}")
#data = json.loads(response.text)
#print(f"The json decoded response is {data}")
