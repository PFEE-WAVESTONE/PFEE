from os import listdir
from PIL import Image
import os.path
import numpy as np

path = 'data/malware_samples/YouAreAnIdiot.exe'

h = 256 #height of image
w = 256 #width of image

#be careful with using this function, it will consume memory, access to disk and time
images = []
with open(path, 'rb') as img_set:
    img_arr = img_set.read(h*w)
    while img_arr:
        if len(img_arr) == h*w and img_arr not in images:
            images.append(img_arr)
        img_arr = img_set.read(h*w)

#And you can save them into png files
count = 0
for img in images:
    png = Image.fromarray(np.reshape(list(img), (h,w)).astype('float32'), mode='L')
    png.save('image_l%d.png'%count)
    count += 1