#1/usr/bin/python3

from argparse import ArgumentParser
from picamera import PiCamera
import boto3 as b3
import time
import os
import simplejson as json

def get_args():
    parser = ArgumentParser(description='Call index faces')
    parser.add_argument('-i', '--image')
    parser.add_argument('-c', '--collection')
    parser.add_argument('-l', '--label')
    return parser.parse_args()

def get_client():
    client = b3.client('rekognition')
    return client

def init_file():
    if (not os.path.isfile('faces.txt')):
        with open('faces.txt', 'w') as init_file:
            init_file.write('Date | Label | Collection | FaceId | ImageId\n')

def capture_image():
    count = 5
    camera = PiCamera()
    camera.vflip = True
    camera.hflip = True

    directory = '/home/pi/PiHomeSec/faces'

    if not os.path.exists(directory):
        os.makedirs(directory)

    print('[+] A photo will be taken in 5 seconds...')

    for i in range(count):
        print (count - i)
        time.sleep(1)

    milli = int(round(time.time() * 1000))

    image ='{0}/image_{1}.jpg'.format(directory, milli) 

    capture.capture(image)
    print('Image was saved to %s' % image)

def add_image():
    with open(args.image, 'rb') as image:
        response = client.index_faces(Image={'Bytes': image.read()}, CollectionId=args.collection, Extern
                alImageId=args.label, DetectionAttributes=['ALL'])

        with open ('faces.txt', 'a') as file:
            current = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            file.write(('%s | %s | %s | %s | %s\n') % (current, args.label, args.collection, response['FaceRecords'][0]['Face']['FaceId'], response['FaceRecords'][0]['Face']['ImageId']))


if __name__ == '__main__':
    args = get_args()
    client = get_client()
    capture_image()

    add_image()
