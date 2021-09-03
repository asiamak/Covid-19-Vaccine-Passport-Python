#Author: Kobe Asiama (Preethi Ramamurthy)
#We have neither given nor recieved unauthorized assistance on this assignment

from flask import Flask, jsonify, request, make_response
from flask_httpauth import HTTPBasicAuth
import requests as prq
import json
import re
import pymongo
from pprint import pprint
import qrcode
from PIL import Image
from datetime import date

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['datastore'].utilization

@app.route('/validate', methods=['GET'])
def validate():
    # TO : DO Later check if user got vaccinated
    #return "Hello"
    data = request.values
    send = {
            "LastName": data["LastName"],
            "FirstName": data["FirstName"],
            "Doses": int(data["Doses"])
    }
    out = db.find_one(send)
    if out is None:
        return "Not Fully Vaccinated."
    return "Valid" if int(out['Doses']) == 2 else "Invalid"
    

@app.route('/add', methods=['POST'])
def add():
    # TO : DO Later Add user as vaccinated person
    data = request.values
    send = {
            "LastName": data["LastName"],
            "FirstName": data["FirstName"],
            "Doses": int(data["Doses"])
    }
    QRcode_data = (json.dumps(send))
    db.insert_one(send)
    out = db.find_one(send)
    if out is None:
        return "Insert Failed"
    # Generate QR Code
    # output file name with last name that is entered 
    filename = (f"{data['LastName']}.png")
    # generate qr code
    img = qrcode.make(QRcode_data)
    # save img to a file
    img.save(filename)
    return "Insert Succeeded"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

