#!/usr/bin/python3

from picamera import PiCamera
import time
import os

count =2 
camera = PiCamera()
camera.vflip = True
camera.hflip = True
directory = '/home/pi/PiHomeSec/faces'

if not os.path.exists(directory):
    os.makedirs(directory)

print('[+] A photo will be taken in 10 seconds...')

for i in range(count):
    print (count - i)
    time.sleep(1)

milli = int(round(time.time() * 1000))
image = '{0}/image_{1}.jpg'.format(directory, milli)

#image = 'testalex.jpg'
camera.capture(image)
print('Your image was saved to %s' % image)


