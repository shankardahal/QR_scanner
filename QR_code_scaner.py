

import pyqrcode
import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "https://www.facebook.com/shankar.dahal.39566"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 7)
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 4)