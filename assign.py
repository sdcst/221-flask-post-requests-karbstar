#!python
from flask import Flask,request
from flask_cors import CORS
import json
import sqlite3
app = Flask(__name__)
CORS(app)

@app.route("/going",methods=["POST"])
def postResponse():
    # a simple echo server that response with the payload received.
    payload = request.form
    print(request.form)
    print(payload)
    data = dict(payload)
    print(data)
    saf=data['get']
    if saf!='bce52a22495d704233dd4e720e942dbf63d0561ed813d77fd38776357db7108e':
        return 'incorect'
    file = 'quoteholder.db'
    connection = sqlite3.connect(file)
    print(connection)

    cursor = connection.cursor()
    query = "select quote from customers"
    cursor.execute(query)
    result = cursor.fetchall()

    new=data['quote']
    new=new.split(',')
    for i in result:
        i=i[0]
        #wd=i.split(' ')
        #for wd in i:
        if i in new:
            new.remove(i)
        
        
    data2 = [
        new
        ]
    if data2==[]:
        return'quote alredy in the system'
    for i in data2:
        i=i[0]
        query = f"insert into customers (quote) values ('{i}')" 
        print(query)
        cursor.execute(query)
    connection.commit()
    
    
    return json.dumps(data2)
@app.route("/",methods=['POST','GET'])
def main():
    return "hi"

app.run("0.0.0.0")