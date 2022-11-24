from flask import Flask,request
from flask_cors import CORS
import json
import sqlite3
import random
file = 'quoteholder.db'
connection = sqlite3.connect(file)
print(connection)
cursor = connection.cursor()
query = "select quote from customers"
cursor.execute(query)
result = cursor.fetchall()
a=[]
data={'quote' : 'what what what', 'get' :'bce52a22495d704233dd4e720e942dbf63d0561ed813d77fd38776357db7108e'}
new=data['quote']
    new=new.split(',')
    nu=0
    for i in result:
        i=i[0]            
        if i in new:
            new.remove(i)
        else:
            wild=new[nu].split(' ')
            x=len(wild)
            x=round(x/2)+random.randint(-1,1)
            if x>=len(wild):
                x=round(x/2)
            che=''.join(['%', f'{wild[1]}', '%'])
            w=wild[-1].split('-')
            che2=''.join(['%', f'{w[0]}', '%'])
            che3=''.join(['%', f'{wild[x]}', '%'])
            nu=nu+1
            queries=[che,che2,che3]
            for i in queries:
                q = f"select * from customers where quote like '{i}'"
                r = cursor.execute(q)
                data = list(r)
                print(i, data)