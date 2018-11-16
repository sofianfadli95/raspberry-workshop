# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:51:55 2018

@author: sofyan.fadli
"""

#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

while True:
    # 11 menunjukkan tipe sensornya : DHT11
    # 4 menunjukkan nomor pin yang kita gunakan (GPIO4)
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    mylcd.lcd_display_string('Suhu: {0:0.1f} C'.format(temperature),1)
    mylcd.lcd_display_string('Kelembapan: {0:0.1f}'.format(humidity),2)