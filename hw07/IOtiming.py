#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

IN1 = "GP1_3"
OUT1 = "GP1_4"

GPIO.setup(OUT1, GPIO.OUT)
GPIO.setup(IN1, GPIO.IN)

buttonMap = {IN1: OUT1}

def updateLEDs(number):
	print("LED number " + number)
	status = GPIO.input(number)
	GPIO.output(buttonMap[number],status)
	print(buttonMap[number] + "changed to status " + str(status))

GPIO.add_event_detect(IN1, GPIO.BOTH, callback = updateLEDs)

try: 
	while True:
		time.sleep(25)

except KeyboardInterrupt:
	print("stopping")
	GPIO.cleanup()
GPIO.cleanup()
