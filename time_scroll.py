#!/usr/bin/python3
import max7219.led as led
import datetime

device = led.matrix(cascaded = 3)

scrolls = 0

while scrolls == 0:
	now = datetime.datetime.now()
	message = now.strftime("%I:%M:%S")
	device.show_message(message)
