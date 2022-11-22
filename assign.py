#!python
from flask import Flask,request
from flask_cors import CORS
import json
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
    
    print(saf)
    
    return json.dumps(data)
@app.route("/",methods=['POST','GET'])
def main():
    return "hi"

app.run("0.0.0.0")