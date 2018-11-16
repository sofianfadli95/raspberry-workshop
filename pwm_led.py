# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:01:51 2018

@author: sofyan.fadli
"""

# External module imports
import RPi.GPIO as GPIO

# Pin Definitons:
pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
butPin = 17 # Broadcom pin 17 (P1 pin 11)

dc = 0 # duty cycle (0-100) for PWM pin

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output
pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

pwm.start(dc)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        if GPIO.input(butPin): # button is released
            if dc < 110:
                dc += 10
            pwm.ChangeDutyCycle(dc)
        else: # button is pressed:
            if dc > 0:
                dc -= 10
            pwm.ChangeDutyCycle(dc)
            
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO