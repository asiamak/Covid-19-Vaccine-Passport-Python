#Author: Preethi Ramamurthy (Kobe Asiama)
#We have neither given nor recieved unauthorized assistance on this assignment



from flask import Flask, jsonify, request, make_response
from flask_httpauth import HTTPBasicAuth
import requests as prq
import json
import re
import cv2
import threading

app = Flask(__name__)
def captureQR():
    # read the QRCODE image
    img = cv2.imread(input("QR Name:\t"))
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    # detect and decode
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    # if there is a QR code
    # display the image with lines
    # length of bounding box
    cv2.destroyAllWindows()
    return data

@app.route('/', methods=['GET'])
def home():
    # TO : DO Later
    return "<p><a href='/scan'>Scan</a></p><p><a href='/generate'>Generate</a></p>"

@app.route('/scan', methods=['GET'])
def scan():
    # TO : DO Later read qrcode post data to server 

    # Scan and get object
    # Format object
    # Send rest api request using prq.get to server **Ask if don't know**
    # Check response output do at the very end
    # initalize the cam
    out = "<p><a href='/'>Home</a></p>"
    data = captureQR()
    obj = json.loads(data)
    x = prq.get('http://127.0.0.1:5000/validate', params=obj)
    print(x)
    if x.status_code == 200 and x.content == b'Valid':
        return "<p>Person is validated</p>" + out
    return "<p>Person not fully vaccinated</p>" + out

@app.route('/generate', methods=['GET'])
def form():
    # TO : DO Later Open Form gen qr code and send to server. Display on screen
    # Open form that when button clicks submit it posts data to api
    return "<form action='http://127.0.0.1:5558/add' method = 'POST'> <p>LastName <input type = 'text' name = 'LastName' /></p><p>FirstName <input type = 'text' name = 'FirstName' /></p><p>Doses <input type = 'text' name = 'Doses' /></p><input type='submit' value='Submit'></form>"

@app.route('/add', methods=['POST'])
def add():
    # TO : DO Later Open Form gen qr code and send to server. Display on screen
    # Open form that when button clicks submit it posts data to api
    out = "<p><a href='/'>Home</a></p>"
    data = request.form
    x = prq.post('http://127.0.0.1:5000/add', params=data)
    if x.status_code == 200 and x.content == b'Insert Succeeded':
        return "<p>Person is inserted</p>" + out
    return "<p>Person is not inserted</p>" + out

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5558, debug=True)

