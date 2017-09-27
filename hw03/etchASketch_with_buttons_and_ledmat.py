#!/usr/bin/env python3
# FileName: etchASketch_2.py
# Description: simple implementation of an Etch A Sketch in Python
#imports
import pygame
import sys
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
# from pygame.locals import *


BUT1 = "GP0_3"
BUT2 = "GP0_4"
BUT3 = "GP0_5"
BUT4 = "GP0_6"
INT1 = "GP1_3"
INT2 = "GP1_4"

GPIO.setup(INT1, GPIO.IN)
GPIO.setup(INT2, GPIO.IN)
GPIO.setup(BUT1, GPIO.IN)
GPIO.setup(BUT2, GPIO.IN)
GPIO.setup(BUT3, GPIO.IN)
GPIO.setup(BUT4, GPIO.IN)

clock = pygame.time.Clock()

bus = smbus.SMBus(1)  # Use i2c bus 1
address1 = 0x48
address2 = 0x4a
matrix = 0x70         # Use address 0x70
disp = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# variables
x = 0
y = 0

bus.write_byte_data(address1, 2, 25)
bus.write_byte_data(address2, 2, 25)
bus.write_byte_data(address1, 3, 25)
bus.write_byte_data(address2, 3, 25)
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

while(1):
    clock.tick(10) #keeps game from exceeding 60 fps
    #pygame.draw.circle(screen, (0,0,0), (x,y), 2)
    #pygame.display.update()
    if (GPIO.input(BUT1)==0):
        x+=1
    if (GPIO.input(BUT3)==0):
        x-=1
    if (GPIO.input(BUT4)):
        y-=1
    if (GPIO.input(BUT2)):
        y+=1
        
    if x > 7:
        x=7
    if x<0:
        x=0
    if y>7:
        y=7
    if y<0:
        y=0
        
    disp[2*y] = disp[2*y] | (1<<x)
    
    if GPIO.input(INT1)==0 or GPIO.input(INT2)==0:
        disp = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    bus.write_i2c_block_data(matrix, 0, disp)
    
    #time.sleep(.25)
