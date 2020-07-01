#! /bin/bash

FILES=./img/faces/base-faces/*
rm ./img/faces/scraped-faces/*.jpg
for f in $FILES
do
    python3 FaceDetect/face_detect.py $f
done