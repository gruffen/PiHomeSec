#!/usr/bin/python3

from picamera import PiCamera
import RPi.GPIO as GPIO
import facematch
import boto3 as b3
import time
import os
import requests

def main():

    PIR_PIN = 7 
    PT_PIN1 = 1  # TODO: Change this
    PT_PIN2 = 2  # TODO: Change this

    IFTTT_KEY = 'dTXcvAJ80UkK5S9OVHdAfr'
    directory= '/home/pi/PiHomeSec/testfaces'
    aws_collection = 'pisecproject'

    # Camera inits
    camera = PiCamera()
    camera.vflip = True
    camera.hflip = True

    # AWS API init
    aws_client = facematch.get_client()

    # GPIO inits
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIR_PIN, GPIO.IN)

    previousstate = 0

    # Wait for init to get to steady state
    while GPIO.input(PIR_PIN) == 1:
        currentstate = 0
   
    # Begin main loop
    try:
        while True:
            match = 'Unknown'
            currentstate = GPIO.input(PIR_PIN)
            if (currentstate == 1 and previousstate == 0):
                print("Motion detected!")

                milli = int(round(time.time() * 1000))
                
                image_name = '{0}/image_{1}.jpg'.format(directory, milli)
                camera.capture(image_name)
                
                print("Capture saved to %s" % image_name)
                
                face_detect_result, response = facematch.check_face(aws_client, image_name)

                if face_detect_result:
                    print("Faces detected with %r confidence" % (round(response['FaceDetails'][0]['Confidence'],2)))

                    print("Checking for a face match...")
                    face_recog_result, res = facematch.check_face_matches(aws_client, image_name, aws_collection)
                    
                    if (face_recog_result):
                        match = res['FaceMatches'][0]['Face']['ExternalImageId']
                        similarity = round(res['FaceMatches'][0]['Similarity'], 1)
                        conf = round(res['FaceMatches'][0]['Face']['Confidence'], 2)

                        print(match)

                    else:
                        similarity = 0
                        conf = 0

                        print(match)
                else:
                    print("No faces detected, notifying anyways...")
                requests.post('https://maker.ifttt.com/trigger/person_detected/with/key/dTXcvAJ80UkK5S9OVHdAfr', params={"value1":match,"value2":"none","value3":"none"})             

                previousstate = 1
                #print("Waiting 120 seconds...")
                time.sleep(8)

            elif currentstate == 0 and previousstate == 1:
                previousstate = 0

        #time.sleep(0.01)
        
    except KeyboardInterrupt:
        print("Quitting...")
        camera.close()
        GPIO.cleanup()

             

if __name__ == '__main__':
    main()



