# Copyright (C) 2017
# Author: Stijn Goethals
# Contact: stijn.goethals@outlook.be

""" 
Places an watermark on the bottom right side of an picture.

usage: main.py [-h] path path_output watermark

positional arguments:
  path         Path to the input folder
  path_output  Path to the output folder
  watermark    Path to the watermark image

optional arguments:
  -h, --help   show this help message and exit
"""

import argparse
import os

from PIL import Image, ExifTags

from tqdm import tqdm


def add_watermark(path, file, output, watermark):
    """
    Places an watermark on the bottom right side of an picture.
    
    :param path: The path to the input folder
    :param file: The input image file
    :param output: The path to the output folder
    :param watermark: The pillow image file containing the picture
    :return: None
    """
    img = Image.open(path + file)
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation': break
    exif = dict(img._getexif().items())

    if exif[orientation] == 3:
        img = img.rotate(180, expand=True)
    elif exif[orientation] == 6:
        img = img.rotate(270, expand=True)
    elif exif[orientation] == 8:
        img = img.rotate(90, expand=True)
    width, height = img.size
    width1, height1 = watermark.size
    img.paste(watermark, (width - width1, height - height1), watermark)
    img.save(output + str(file) + ".jpg", quality=80, optimize=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str,
                        help="Path to the input folder")
    parser.add_argument("path_output", type=str,
                        help="Path to the output folder")
    parser.add_argument("watermark", type=str,
                        help="Path to the watermark image")
    args = parser.parse_args()

    print("Stijn Goethals (c) 2017")
    print("step 1 of 2: Initialization")
    path = args.path
    path_output = args.path_output
    watermark = Image.open(args.watermark)

    # Check of input folder exist
    if not os.path.exists(path):
        print("Input folder doesn't exist!")
        exit(-1)
    if not os.path.exists(path_output):
        print("Output folder doesn't exist!")
        exit(-2)

    # Check of output folder exist
    if not os.path.exists("output"):
        os.makedirs("output")

    print("step 2 of 2: Placing watermark and resize")
    for file in tqdm(os.listdir(path)):
        add_watermark(path, file, path_output, watermark)
    exit(1)
