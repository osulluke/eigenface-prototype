# Adapted from https://kite.com/python/examples/4887/PIL-convert-between-a-pil-%60image%60-and-a-numpy-%60array%60

from PIL import Image
import numpy as np

# Load up an image and convert it to an array
im = Image.open("img/to-array/office-1.jpg")
np_im = np.array(im)
print(np_im.shape)

# Modify the array elements
np_im -= 40

print("size =", np_im.size)
# print(np_im)

# Transform back into and save as an image
new_im = Image.fromarray(np_im)
new_im.save("img/to-array/office-1v2.png")

# Resize the image and save a smaller version
new_im = new_im.resize((300, 200))
print(new_im.size)
new_im.save("img/to-array/office-1vResize.png")