# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:13:33 2018

@author: sofyan.fadli
"""

############################################
# Accessing and Modifying Pixel Values
############################################

import cv2
import numpy as np

img = cv2.imread('kucing.jpg')

px = img[100,100]
print(px)

# accessing only blue pixel
blue = img[100,100,0]
print(blue)

img[100,100] = [255,255,255]
print(img[100,100])

# accessing RED value
img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

############################################
# Accessing Image Properties
############################################
print(img.shape)
print(img.size)
print(img.dtype)

############################################
# Image ROI
############################################
head = img[100:125, 330:390]
img[100:125, 330:390] = head

cv2.imshow("Faces found", head)
cv2.waitKey(0)