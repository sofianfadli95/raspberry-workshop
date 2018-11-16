# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:33:37 2018

@author: sofyan.fadli
"""

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
ledPin_1 = 18 # Broadcom pin 18 (P1 pin 12)
ledPin_2 = 23 # Broadcom pin 23 (P1 pin 16)
butPin = 17 # Broadcom pin 17 (P1 pin 11)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin_1, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPin_2, GPIO.OUT) # PWM pin set as output
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for LEDs:
GPIO.output(ledPin_1, GPIO.HIGH)
GPIO.output(ledPin_2, GPIO.HIGH)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        if GPIO.input(butPin): # button is released
            time.sleep(20)
            GPIO.output(ledPin_1, GPIO.LOW)
            GPIO.output(ledPin_2, GPIO.HIGH)
        else: # button is pressed:
            time.sleep(20)
            GPIO.output(ledPin_1, GPIO.HIGH)
            GPIO.output(ledPin_2, GPIO.LOW)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO