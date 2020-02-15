import cv2
import numpy as np

from math import ceil

ascii_map = "@%#*+=-:. "
img_path = "./test.png"
img = cv2.imread(img_path, 0)
resized_img = cv2.resize(img, (50,28))
width = ceil(255/len(ascii_map))

for i in range(resized_img.shape[0]):
    for j in range(resized_img.shape[1]):
        character = ascii_map[-(ceil(resized_img[i,j]//width))-1]
        print(character, end="")
    print()
