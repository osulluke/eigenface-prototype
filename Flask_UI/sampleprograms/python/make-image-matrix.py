from PIL import Image
import numpy as np
import os

read_path = 'img/faces/eigen-faces/'
entries = os.listdir(read_path)
print(entries)

x = []
for f in entries:
    im = Image.open(read_path + f).convert('LA')
    np_im = np.array(im)
    #print(np_im.shape)
    im_flat = np_im.ravel()
    #im_flat = im_flat.reshape(im_flat.size, 1)
    x.append(im_flat)

arr = np.array(x)
print(x)
print(arr)
mat = np.matrix(arr)
cov = mat.dot(mat.T)