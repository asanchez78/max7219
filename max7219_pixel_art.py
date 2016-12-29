#!/usr/bin/python3

import max7219.led as led
import zmq


#  Prepare server context and socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    # Convert binary to string
    stringdata = message.decode('utf-8')
    print(stringdata)

    values = stringdata.split(",")

    #  Send reply back to client. Don't wait for for message to finish
    socket.send(b"OK")

    #  display message on 7219
    device = led.device()

    for i in range(8):
      value = int(values[i])
      position=i+1
      device.set_byte(0,position,value,False)

    device.flush()

