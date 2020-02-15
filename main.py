import logging
from math import ceil
from sys import stdout

import cv2
import numpy as np

from constants import (
        ASCII_MAP,
        ASCII_MAP_LEN,
        DEFAULT_HEIGHT_CORRECTION,
        DEFAULT_SCALE,
        DEFAULT_IMAGE_PATH,
        WIDTH
        )

from log import setup_logger

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
    logging.debug(
                    "Dimensions of the image after correction (height={0}, width={1})"
                    .format(corrected_img.shape[0], corrected_img.shape[1])
                    )
    return corrected_img

def generate_ascii(img, output_file=stdout):
    '''
    This function is used to generate the ASCII image and writes it to the specified file.

    Parameters
    ----------
    img - An image as a numpy array which is to be printed
    output_file - file where the ASCII image has to be written
    '''
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            character = ASCII_MAP[-(ceil(img[i,j]//WIDTH))-1]
            print(character, end="")
        print()

    
def main():
    setup_logger()
    img = cv2.imread(DEFAULT_IMAGE_PATH, 0)
    resized_img = image_correction(img)
    generate_ascii(resized_img)

if __name__ == "__main__":
    main()
