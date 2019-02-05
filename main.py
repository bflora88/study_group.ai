import cv2
import numpy as np
import argparse


# given a path, returns an image into a numpy array in BGR format 
def read_img(img_path):
    img = cv2.imread(img_path)
    return img


# displays the given image in a window    
def show_img(img):
    cv2.imshow("test img", img)
    # keeps the window open until any key is pressed, or after 20 secs
    cv2.waitKey(10000)

    
# transform the input image from BGR format to L
def bgr_to_gray(bgr_img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)/255.0
    return gray



def main(args):
    print('img path: {}'.format(args.img_path))
    img = read_img(args.img_path)
    show_img(img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Playground for implementing old school computer vision algos")
    parser.add_argument("--img_path", type=str, default="./imgs/lena.png", help="Path to the test img")
    
    args = parser.parse_args()
    main(args)
