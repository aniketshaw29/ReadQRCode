import numpy as np
from pyzbar.pyzbar import decode
import cv2
img=cv2.imread("q2.png")
code = decode(img)
print(code)
for barcode in decode(img):
    print(barcode.data)
    text=barcode.data.decode('utf-8')
    print(text)
    print(barcode.rect)

#pip install numpy
#pip install pyzbar
#pip install opencv-python    
    
   