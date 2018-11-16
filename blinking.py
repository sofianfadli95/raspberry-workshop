# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:07:11 2018

@author: sofyan.fadli
"""

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)
GPIO.output(17, GPIO.LOW)
time.sleep(2000)

GPIO.output(18, GPIO.LOW)
GPIO.output(17, GPIO.HIGH)
time.sleep(2000)

# Cleanup all GPIO
GPIO.cleanup()
