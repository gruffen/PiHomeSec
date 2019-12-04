#!/usr/bin/python3

import RPi.GPIO as GPIO
from picamera import PiCamera 
import time
import os

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN)

camera = PiCamera()
camera.vflip = True
camera.hflip = True

directory = '/home/pi/PiHomeSec/'

while GPIO.input(7) == 1:
    currentstate =0

previousstate = 0
while True:
    currentstate = GPIO.input(7)
    if currentstate == 1 and previousstate == 0:
        print("Motion detected!")

        milli = int(round(time.time() * 1000))

        image_name = '{0}/image_{1}.jpg'.format(directory, milli)

       # camera.capture(image_name)

       # print("Capture saved to %s" % image_name)

        previousstate = 1
        time.sleep(10)

    elif currentstate == 0 and previousstate == 1:
        previousstate = 0

#    time.sleep(0.01)


