# -*- coding: utf-8 -*-
"""OCR_ARABIC AND ENGLISH.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14hLOSWsJQcwa_I8bZo0MJVDLnGdXSTDK
"""

!pip install ArabicOcr

!sudo apt install tesseract-ocr
!pip install pytesseract

from ArabicOcr import arabicocr
image_path='/content/drive/MyDrive/arabic/new/card.jpeg'
out_image='out.jpg'
results=arabicocr.arabic_ocr(image_path,out_image)
print(results)
words=[]
for i in range(len(results)):	
		word=results[i][1]
		words.append(word)
with open ('file.txt','w',encoding='utf-8')as myfile:
		myfile.write(str(words))

print(words)

from ArabicOcr import arabicocr
image_path='/content/drive/MyDrive/arabic/new/eng.jpeg'
out_image='out.jpg'
results=arabicocr.arabic_ocr(image_path,out_image)
print(results)
words=[]
for i in range(len(results)):	
		word=results[i][1]
		words.append(word)
with open ('file.txt','w',encoding='utf-8')as myfile:
		myfile.write(str(words))

words

from ArabicOcr import arabicocr
image_path='/content/drive/MyDrive/arabic/new/arabic.jpeg'
out_image='out.jpg'
results=arabicocr.arabic_ocr(image_path,out_image)
print(results)
words=[]
for i in range(len(results)):	
		word=results[i][1]
		words.append(word)
with open ('file.txt','w',encoding='utf-8')as myfile:
		myfile.write(str(words))

words









import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image

import matplotlib.pyplot as plt
import cv2

im = cv2.imread("/content/drive/MyDrive/arabic/new/eng.jpeg", cv2.IMREAD_COLOR)

im = cv2.bitwise_not(im)
plt.imshow(im)
plt.show()

image_path_in_colab="/content/drive/MyDrive/arabic/new/eng.jpeg"
extract = pytesseract.image_to_string(Image.open(image_path_in_colab))
print(extract)
#type(extract)

extract=''.join(extract)
type(extract)

extract=extract.split('\n')

extract

l=list()
for i in extract:
  if i!='' and i!=' ':
    l.append(i)
l

