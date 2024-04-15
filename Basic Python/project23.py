import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.linkedin.com/in/yash-pandey-4029ba2b9/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("mylinkedin.svg", scale = 8) 