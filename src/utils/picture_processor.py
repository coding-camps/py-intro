# -*- coding: utf-8 -*-
import cv2
from PIL import Image
from matplotlib import pyplot as plt

def view2(pic_path):
    image = cv2.imread(pic_path)
    # print(type(image),len(image))
    cv2.namedWindow("image")

    def on_left_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"clicked left: ({x}, {y})")

    cv2.setMouseCallback("image", on_left_click)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cut_img1(pic_path):
    pic = Image.open(pic_path)
    box = (211, 0, 2130, 1080)
    pic2 = pic.crop(box)
    # pic2.show()
    print(type(pic2))
    return pic2


def cut_img2(pic_path):
    image = cv2.imread(pic_path)
    image2 = image[0:1080, 211:2130]
    # cv2.imshow("image", image2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return image2

def cut_img_v1(img_file):
    def on_click(event):
        print(f"clicked on ({event.x}, {event.y})")
    with open(img_file, 'rb') as img:
        pass

