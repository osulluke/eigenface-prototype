from PIL import Image
import os
import numpy as np

read_path = 'img/faces/scraped-faces/'
save_path = 'img/faces/scaled-faces/'
save_average_face = 'img/faces/average-face/'
entries = os.listdir(read_path)
print(entries)

average = 0
i = 0
for f in entries:
    im = Image.open(read_path + f)
    im = im.resize((300,300))
    im.save(save_path + f)
    pixel_values = np.array(im)
    pixel_values = pixel_values.astype('int32') # we need a larger data type to store data
    average += pixel_values
    i += 1

average = average / i
average = np.round(average)
average = average.astype('uint8') # convert back into datatype appropriate for images

average_face = Image.fromarray(average)
average_face.save(save_average_face + 'average-face.jpg')
average_face.show()