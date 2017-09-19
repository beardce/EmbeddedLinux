#!/usr/bin/env python3

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO
import sys

bus = smbus.SMBus(1)
address1 = 0x48
address2 = 0x4a
INT1 = "GP1_3"
INT2 = "GP1_4"

GPIO.setup(INT1, GPIO.IN)
GPIO.setup(INT2, GPIO.IN)

#setup
bus.write_byte_data(address1, 2, 25)
bus.write_byte_data(address2, 2, 25)
bus.write_byte_data(address1, 3, 25)
bus.write_byte_data(address2, 3, 25)

while True:
    
    temp1 = bus.read_byte_data(address1, 0)
    temp2 = bus.read_byte_data(address2, 0)
    if GPIO.input(INT1)==0:
        print ("temp 1 = " + str(temp1) + "\r")
        
    if GPIO.input(INT2)==0:
        print ("temp 2 = " + str(temp2) + "\r")
    time.sleep(.25)