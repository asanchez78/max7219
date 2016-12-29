#!/usr/bin/python3
import max7219.led as led
import datetime
import time
import os
device = led.matrix(cascaded = 3)
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

scrolls = 0

while scrolls == 0:
	nyeEpoch = datetime.datetime(2017,1,1,0,0).timestamp()
	now = time.time()
	timeLeft = nyeEpoch - now
	days = int(timeLeft // 86400)
	#days = int(0)
	hours = int(timeLeft // 3600 % 24)
	#hours = int(0)
	minutes = int(timeLeft // 60 % 60)
	#minutes = int(0)
	seconds = int(timeLeft % 60 )
	if days > 0:
		message = str(days) + " days " + str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds"
		print(message)
		device.show_message(message)
	if days <= 0 :
		if hours > 0 :
			message = str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds"
			print(message)
			device.show_message(message)
		if hours <= 0 :
			if minutes > 0 :
				message = str(minutes) + " minutes " + str(seconds) + " seconds"
				print(message)
				device.show_message(message)
			if minutes <= 0 :
				if seconds >= 10 :
					message = str(seconds)
					print(message)
					device.show_message("    " + str(message),font=proportional(TINY_FONT),always_scroll=False)
					time.sleep(1)
				elif seconds < 10 and seconds > 0:
					message = str(seconds)
					print(message)
					device.show_message("  " + str(message),always_scroll=False)
					print(message)
					time.sleep(1)
	if (days == 0 and hours == 0 and minutes == 0 and seconds == 0) :
		device.show_message("HAPPY NEW YEAR!!")
			


