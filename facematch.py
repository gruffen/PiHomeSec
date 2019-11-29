#!/usr/bin/python3

import boto3 as b3
from time import gmtime, strftime

def get_client():
    return b3.client('rekognition')
   
def check_face(client, file):
    face_detected = False
    with open(file, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()})
        if (not response['FaceDetails']):
            face_detected = False
        else
            face_detected = True

    return face_detected, response

def check_face_matches(client, file, collection):
    face_matches = False
    with open(file, 'rb') as image:
        response = client.search_faces_by_image(CollectionId=collection, Image={'Bytes': image.read()}, MaxFaces = 1, FaceMatchThreshold=85)
        if (not response['FaceMatches']):
            face_matches = False
        else:
            face_matches = True

    return face_matches, response



