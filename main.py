from math import ceil

import cv2
import numpy as np

from constants import (
        ASCII_MAP,
        ASCII_MAP_LEN,
        DEFAULT_HEIGHT_CORRECTION,
        DEFAULT_SCALE,
        DEFAULT_IMAGE
        )

def image_correction(img, scale=DEFAULT_SCALE, height_correction=DEFAULT_HEIGHT_CORRECTION):
    '''
    This function is used to scale the image and have height correction
    to handle the size of the ASCII characters.

    Parameters
    ----------
    img - Image as a numpy array which is to be corrected.
    scale - Parameter to scale the image up or down.
    height_correction - Height scale to handle difference in ASCII character height.
    '''
    dimensions = (
                 int(img.shape[0]*DEFAULT_SCALE),
                 int(img.shape[0]*DEFAULT_SCALE*DEFAULT_HEIGHT_CORRECTION)
                 )
    corrected_img = cv2.resize(img, dimensions)
    return corrected_img

def main():

    img = cv2.imread(DEFAULT_IMAGE, 0)
    width = ceil(255/ASCII_MAP_LEN)

    resized_img = image_correction(img)
    for i in range(resized_img.shape[0]):
        for j in range(resized_img.shape[1]):
            character = ASCII_MAP[-(ceil(resized_img[i,j]//width))-1]
            print(character, end="")
        print()

if __name__ == "__main__":
    main()