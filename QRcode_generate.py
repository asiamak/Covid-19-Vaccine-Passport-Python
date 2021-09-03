#This program will generate a QR code
#https://www.thepythoncode.com/article/generate-read-qr-code-python 

import qrcode
from PIL import Image
from datetime import date

# example data
#data = "https://www.thepythoncode.com"
today = date.today()
date = today.strftime("%m/%d/%y")
print("Today's Date = ", date)
# today = date.today()
# print("Today's date:", today)
FirstName = input("First Name: ")
LastName = input("Last Name: ")
# DOB = input("Please enter your DOB in this format (MM/DD/YYYY): ")
# Location = input("Location of vaccine: ")
Dose = input("Which dose is the patient receiving? ")

QRcode_data = (f"Date: {date}, Patient: {LastName}, {FirstName}, Dose Number: {Dose}")

# output file name with last name that is entered 
filename = (f"{LastName}.png")
# generate qr code
img = qrcode.make(QRcode_data)
# save img to a file
img.save(filename)