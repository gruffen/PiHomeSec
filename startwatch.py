#!/bin/usr/python3

from picamera import PiCamera
import RPI.GPIO as GPIO
import facematch
import boto3 as b3
import time
import os
import requests

def main():
    PIR_PIN = 17 # TODO: Change this

    camera = PiCamera()
    GPIO.setmode(GPIO.BCM)

    GPIO.setwarning(False)
    GPIO.setup(PIR_PIN, GPIO.IN)

    while GPIO.input(PIR_PIN) == 1:
        currentstate = 0
    
    try:
       while True:
           
         # Read from pins
         # Do additional processing
            # If something was detected
                # If light outside
                    # Take normal picture
                # Else if dark outside
                    # Take flash/longer exposure picture
                # Run facial recognition
                    # If no faces detected, take another picture just to be sure
                # Post a request to IFTTT with name of person (or unknown)
                # Post a request to webserver with name of person (or unknown), and image
        
    except KeyboardInterrupt:
        print("Quitting...")

        GPIO.cleanup()

             

if __name__ == '__main__':
    main()



