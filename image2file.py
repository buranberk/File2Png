import cv2
import numpy as np
import argparse


def image2file(imagepath):
    image = cv2.imread(imagepath, cv2.IMREAD_UNCHANGED)
    filename = np.trim_zeros(image[-1].flatten(), "b").tobytes()
    image = image[:-1]
    image = image.flatten().tobytes()
    with open(filename, "wb") as f:
        f.write(image)


def main():
    parser = argparse.ArgumentParser(description='img2file')
    parser.add_argument('imgpath', help='Path of the image you wanna convert.')
    args = parser.parse_args()

    image2file(args.imgpath)


if __name__ == '__main__':
    main()
