# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:40:12 2018

@author: sofyan.fadli
"""

#!/usr/bin/env python
import serial

ser = serial.Serial(
        port=' /dev/ttyUSB0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while 1:
        x=ser.readline()
        print (x)