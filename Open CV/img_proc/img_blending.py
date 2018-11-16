# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:43:48 2018

@author: sofyan.fadli
"""

import cv2

img1 = cv2.imread('kucing.jpg')
img2 = cv2.imread('opencv_logo.png')
height, width = img1.shape[:2]
resized_image = cv2.resize(img2, (width, height)) 

dst = cv2.addWeighted(img1,0.7,resized_image,0.3,0)

cv2.imshow('blending',dst)
cv2.waitKey(10)