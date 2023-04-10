# Bitmap Image Rotator V1.0

A new adventure with binary data. This time, with no libraries and for the love of reinventing the wheel, I worked on a Python program that rotates a given bitmap (BMP) image by 90 degrees clockwise. The script reads the input image file, processes the pixel data to perform the rotation, and writes the rotated pixel data to a new BMP file named `output.bmp`.

<br>

## Features to add:

- Support different types of images
- Support different shapes, not just square images
- Support rotation in different directions and different angles, not just 90deg.
- Add features for colors manipulation such as black and white.

<br>

## Usage

```bash
python rotate.py <input_image>
```

Replace `<input_image>` with the path to the input BMP image file.

<br>

## Example

```bash
python rotate.py ./images/teapot.bmp
```

This command will read the `teapot.bmp` image file, rotate it by 90 degrees clockwise, and write the rotated image to a new file named output.bmp.

<br>

## Algorithm

The script performs the following steps:

1. Read the input BMP file and extract relevant header information such as width, height, and pixels data starting address.
2. Iterate through the pixel data and calculate the position of each pixel in the rotated image using a simple coordinate transformation.
3. Write the rotated pixel data to the output BMP file, preserving the original header information.

> **N.B: Please note that this script is designed for 24-bit BMP square images and might not work correctly with other formats.**
