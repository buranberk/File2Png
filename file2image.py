import numpy as np
import cv2
import os
import argparse


def factorize(x):
    sqr = np.sqrt(x)
    sqr = int(np.ceil(sqr))
    return sqr, sqr


def file2image(filepath, imagepath=None):
    filename = os.path.basename(filepath)
    filesize = os.stat(filepath).st_size

    c = 4
    h, w = factorize(filesize/c)
    h += 1

    with open(filepath, "rb") as f:
        image = np.array(np.frombuffer(
            f.read(filesize), dtype=np.uint8))
        image = np.append(image, np.zeros((h*w*c-filesize)))
        image.resize((h, w, c))

        name = np.frombuffer(
            bytes(filename, encoding='utf-8'), dtype=np.uint8)
        name = np.append(name, np.zeros((w*c-len(name))))
        name.resize((w, c))
        image[-1] = name

    if imagepath is None:
        imagepath = filename.split(".")[0]

    cv2.imwrite(imagepath+".png", image)


def main():
    parser = argparse.ArgumentParser(description='file2img')
    parser.add_argument('filepath', help='Path of the file you wanna convert.')
    parser.add_argument("-i", '--imagepath',
                        help='Path of the image you wanna save.')
    args = parser.parse_args()

    file2image(args.filepath, args.imagepath)


if __name__ == '__main__':
    main()
