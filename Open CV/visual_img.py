# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:21:08 2018

@author: sofyan.fadli
"""

import cv2

img = cv2.imread('kucing.jpg')
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', img)
cv2.waitKey(10)
