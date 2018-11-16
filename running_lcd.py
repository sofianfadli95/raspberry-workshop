# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:04:06 2018

@author: sofyan.fadli
"""

import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

str_pad = " " * 16
my_long_string_1 = "Lari...Lari...Lari..."
my_long_string_1 = str_pad + my_long_string_1

my_long_string_2 = "Tendang dan berlariii..."
my_long_string_2 = str_pad + my_long_string_2

while True:
    for i in range (0, len(my_long_string_1)):
        lcd_text = my_long_string_1[i:(i+16)]
        mylcd.lcd_display_string(lcd_text,1)
        sleep(0.05)
        mylcd.lcd_display_string(str_pad,1)
    
    for i in range (0, len(my_long_string_2)):
        lcd_text = my_long_string_2[i:(i+16)]
        mylcd.lcd_display_string(lcd_text,2)
        sleep(0.05)
        mylcd.lcd_display_string(str_pad,2)