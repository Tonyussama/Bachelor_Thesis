# load the library using the import keyword
# OpenCV must be properly installed for this to work. If not, then the module will not load with an
# error message.

import cv2
import sys

# Gets the name of the image file (filename) from sys.argv
url = 'rtsp://admin:Tony0000@192.168.1.108/cam/realmonitor?channel=1&subtype=00&authbasic=YWRtaW46YWRtaW4='

cap = cv2.VideoCapture(url)

cascPath = "haarcascade_frontalface_default.xml"

# This creates the cascade classifcation from file

faceCascade = cv2.CascadeClassifier(cascPath)

# The image is read and converted to grayscale

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # The face or faces in an image are detected
    # This section requires the most adjustments to get accuracy on face being detected.

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(1, 1),
        flags=cv2.CASCADE_SCALE_IMAGE
        )

    print("Detected {0} faces!".format(len(faces)))

    # This draws a green rectangle around the faces detected

    for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Frame', frame)
    
    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
