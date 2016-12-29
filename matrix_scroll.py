#!/usr/bin/python3
import max7219.led as led
import argparse

device = led.matrix(cascaded = 3)

parser = argparse.ArgumentParser(description='Scrolls message on LED matrix')

parser.add_argument('-m','--message',help='The message to scroll on the LED matrix',required=True)

parser.add_argument('-r','--repeat',help='The number of times to repeat the message. 0 will scroll forever.',required=True,type=int)

arguments = parser.parse_args()

message = arguments.message

scrolls = arguments.repeat

if scrolls == 0:
	while scrolls == 0:
		device.show_message(message)
else:
	while scrolls > 0 :
		device.show_message(message)
		scrolls -= 1
