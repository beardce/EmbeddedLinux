#!/usr/bin/env python3
# FileName: etchASketch_2.py
# Description: simple implementation of an Etch A Sketch in Python
#imports
import pygame
import sys
from pygame.locals import *

# variables
#screenXSize = 600
#screenYSize = 400
#x = 300
#y = 200
screenXSize = input("Set screen width in pixels: ")
screenYSize = input("Set screen height in pixels: ")
x = input("Set cursor X position in pixels: ")
y = input("Set cursor Y position in pixels: ")


pygame.init()
screen = pygame.display.set_mode((screenXSize, screenYSize))

clock = pygame.time.Clock()
screen.fill((255,255,255))

while(1):
    clock.tick(60)
    pygame.draw.circle(screen, (0,0,0), (x,y), 2)
    pygame.display.update()
    key = pygame.key.get_pressed()
    if (key[pygame.K_RIGHT]):
        x+=1
    if (key[pygame.K_LEFT]):
        x-=1
    if (key[pygame.K_UP]):
        y-=1
    if (key[pygame.K_DOWN]):
        y+=1
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()
        elif (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            screen.fill((255,255,255))