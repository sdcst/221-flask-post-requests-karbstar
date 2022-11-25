from flask import Flask,request
from flask_cors import CORS
import json
import sqlite3
import random
nop=True
file = 'quoteholder.db'
connection = sqlite3.connect(file)
print(connection)
cursor = connection.cursor()
query = "select quote from customers"
cursor.execute(query)
result = cursor.fetchall()
a=[]
data={'quote' : 'what what dop best', 'get' :'bce52a22495d704233dd4e720e942dbf63d0561ed813d77fd38776357db7108e'}
new=data['quote']
new=new.split(',')
nu=0
for i in result:
    i=i[0]            
    if i in new:
        new.remove(i)
        nop==False
        che=False
    elif nop==True:
        che=True
if che==True:
    for l in new:
        wild=new[nu].split(' ')
        x=len(wild)
        x=round(x/2)+random.randint(-1,1)
        if x>=len(wild):
            x=round(x/2)
        che=''.join(['%', f'{wild[1]}', '%'])
        w=wild[-1].split('-')
        che2=''.join(['%', f'{w[0]}', '%'])
        che3=''.join(['%', f'{wild[x]}', '%'])
        kil=0
        if che2==che3 or che==che2:
            queries=[che,che3]
        else:
            queries=[che,che2,che3]
        for j in queries:
            q = f"select * from customers where quote like '{j}'"
            r = cursor.execute(q)
            data = list(r)
            if data!=[]:
                kil=kil+1
            print(j, data)
            if kil==2:
                new.remove(i)