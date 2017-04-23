# Watermark Picture

Places an watermark on the bottom right side of an picture.

## How to use

Execute the main.py file or use the function add_watermark

### main.py

usage: main.py [-h] path path_output watermark

#### positional arguments:
-  path         Path to the input folder
-  path_output  Path to the output folder
-  watermark    Path to the watermark image

#### optional arguments:
-  -h, --help   show this help message and exit
  
#### Return codes:
- 1: Success
- -1: Input folder doesn't exist
- -2: Output folder doesn't exist
### add_watermark
Places an watermark on the bottom right side of an picture.

- :param path: The path to the input folder
- :param file: The input image file
- :param output: The path to the output folder
- :param watermark: The pillow image file containing the picture
- :return: None