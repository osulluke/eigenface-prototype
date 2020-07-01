from PIL import Image
import os
import numpy as np

read_path = 'img/faces/scaled-faces/'
average_face_path = 'img/faces/average-face/average-face.jpg'
write_path = 'img/faces/average-faces/'

entries = os.listdir(read_path)
average_face = Image.open(average_face_path)
average_face_vector = np.array(average_face)
for f in entries:
    face = Image.open(read_path + f)
    face_vector = np.array(face)
    diff_vector = face_vector - average_face_vector
    diff_face = Image.fromarray(diff_vector)
    diff_face.save(write_path + 'average-' + f)
