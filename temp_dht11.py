# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:51:55 2018

@author: sofyan.fadli
"""

#!/usr/bin/python
import sys
import Adafruit_DHT

while True:
    # 11 menunjukkan tipe sensornya : DHT11
    # 4 menunjukkan nomor pin yang kita gunakan (GPIO4)
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))