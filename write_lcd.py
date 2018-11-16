# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 15:00:58 2018

@author: sofyan.fadli
"""

import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

mylcd.lcd_display_string("Hello World!", 2)
