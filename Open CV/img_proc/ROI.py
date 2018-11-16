# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:45:15 2018

@author: sofyan.fadli
"""

import cv2

img = cv2.imread('kucing.jpg')

#      img[y1:y2, x1:x2]
head = img[29:114, 116:202]

cv2.imshow("Faces found", head)
cv2.waitKey(10)