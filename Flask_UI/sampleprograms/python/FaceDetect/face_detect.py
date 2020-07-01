# Source: https://github.com/shantnu/FaceDetect

import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
print(imagePath)
file_name = imagePath.split('/')[-1].split('.')[0]
file_name += '-face.jpg'
cascPath = "FaceDetect/haarcascade_frontalface_default.xml"
print(file_name)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))
startx = 0
endx = 0
starty = 0
endy = 0
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    print("rect:",(x,y,w,h))
    startx = x
    starty = y
    endx = x + w
    endy = y + h
    face = image[starty:endy, startx:endx]
    cv2.imshow("Face Only", face)
    destination = 'img/faces/scraped-faces/' + file_name
    cv2.imwrite(destination, face)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(1000) # Pause with image found for 1 second
cv2.destroyAllWindows()