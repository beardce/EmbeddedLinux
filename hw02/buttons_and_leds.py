#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

BUT1 = "GP0_3"
BUT2 = "GP0_4"
BUT3 = "GP0_5"
BUT4 = "GP0_6"
LED1 = "GP1_3"
LED2 = "GP1_4"
LED3 = "RED"
LED4 = "GREEN"

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(BUT1, GPIO.IN)
GPIO.setup(BUT2, GPIO.IN)
GPIO.setup(BUT3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUT4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

buttonMap = {BUT1: LED1, BUT2: LED2, BUT3: LED3, BUT4: LED4}

def updateLEDs(number):
	print("LED number " + number)
	status = GPIO.input(number)
	GPIO.output(buttonMap[number],status)
	print(buttonMap[number] + "changed to status " + str(status))

GPIO.add_event_detect(BUT1, GPIO.BOTH, callback = updateLEDs)
GPIO.add_event_detect(BUT2, GPIO.BOTH, callback = updateLEDs)
GPIO.add_event_detect(BUT3, GPIO.BOTH, callback = updateLEDs)
GPIO.add_event_detect(BUT4, GPIO.BOTH, callback = updateLEDs)

try: 
	while True:
		time.sleep(25)

except KeyboardInterrupt:
	print("stopping")
	GPIO.cleanup()
GPIO.cleanup()
