# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:59:01 2018

@author: sofyan.fadli
"""

#############################################
#               Image Addition
#############################################
import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print (cv2.add(x,y)) # 250+10 = 260 => 255

print (x+y)          # 250+10 = 260 % 256 = 4

#############################################
#               Image Blending
#############################################
import cv2

img1 = cv2.imread('kucing.jpg')
img2 = cv2.imread('opencv_logo.png')
height, width = img1.shape[:2]
resized_image = cv2.resize(img2, (width, height)) 

dst = cv2.addWeighted(img1,0.7,resized_image,0.3,0)

cv2.imshow('blending',dst)
cv2.waitKey(10)
# cv2.destroyAllWindows()