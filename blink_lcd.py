# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 15:02:53 2018

@author: sofyan.fadli
"""

import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

while(1):
    mylcd.lcd_display_string("Met malem minggu", 1)
    sleep(1)
    
    mylcd.lcd_display_string("guyss...", 2)
    sleep(1)
    
    mylcd.lcd_clear()