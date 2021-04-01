# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def images_combine(img_paths: list, save_name='combined.img'):
    ''' 水平方向合并图片 '''
    imgs = []
    for img in img_paths:
        imgs.append(Image.open(img))
    width = sum([img.size[0] for img in imgs])
    height = max([img.size[1] for img in imgs])
    joint = Image.new('RGB', (width, height))
    for idx, img in enumerate(imgs):
        loc_width = sum([img_sublist.size[0] for img_sublist in imgs[:idx]])
        joint.paste(img, (loc_width, 0))
    joint.save(save_name)


def warp(pic1, pic2, src_loc, dest_loc, save_path=None):
    '''
    对图像做投影变换，将pic1中的部分或全部图片，经投影变换，贴到目的地图片。
    :param pic1: 投影变换源图片
    :param pic2: 投影变换像图片
    :param src_loc: 投影变换源点点
    :param dest_loc: 投影变换像的点
    :param save_path: 图片报错位置
    :return: 无
    '''
    img1 = cv2.imread(pic1)
    height, width, vx = img1.shape
    print("img1", img1.shape, type(img1), img1.dtype)
    cv2.imshow("img1", img1)

    image = cv2.imread(pic2)
    img2 = image[0:1080, 211:2130]
    h, w, v = img2.shape
    print("img2", img2.shape, type(img2), img2.dtype)
    cv2.imshow("img2", img2)

    # 计算投影变换矩阵
    m = cv2.getPerspectiveTransform(src_loc, dest_loc)
    # 投影变换
    r = cv2.warpPerspective(img2, m, (width, height))
    print("r", r.shape, type(r), r.dtype)
    cv2.imshow("r", r)

    # mask
    mask = r == np.zeros(r.shape, r.dtype)
    mask = np.ma.array(np.ones(r.shape, r.dtype), mask=mask) * 255
    print("mask", mask.shape, type(mask), mask.dtype)
    cv2.imshow("mask", mask)

    iz = cv2.bitwise_or(img1, mask) + r
    cv2.imshow("iz", iz)

    if save_path is not None:
        cv2.imwrite(save_path, iz)
    # mx = cv2.bitwise_or(img1, r)
    # mx = cv2.bitwise_or(mx, r)
    # # cv2.imshow("mx", mx)
    #
    # # mx = mx.bitwise_not()
    #
    # # cv2.imshow("rt", rt)

    # maskx = np.ones(img1.shape, img1.dtype)
    # maskx = maskx[50:-50, 50:-50, :]
    # r = r[50:-50, 50:-50, :]
    # jz = cv2.seamlessClone(r, img1, maskx, (int(height/2)-50, int(width/2)-50), cv2.MIXED_CLONE)
    # cv2.imshow("jz", jz)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def view1(src):
    pic = Image.open(src)
    w, h = pic.size
    pic.close()

    plt.plot(w, h)
    img = plt.imread(src)
    plt.imshow(img)
    plt.show()


def view2(pic_path):
    image = cv2.imread(pic_path)
    cv2.imshow("image", image)
    print(type(image))
    print(len(image))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    template = r'../../pics/template-1.jpg'
    view2(template)


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


def warp0(pic1, pic2):
    img1 = cv2.imread(pic1)
    height, width, vx = img1.shape
    print("img1", img1.shape, type(img1), img1.dtype)
    cv2.imshow("img1", img1)

    img2 = cut_img2(pic2)
    h, w, v = img2.shape
    print("img2", img2.shape, type(img2), img2.dtype)
    cv2.imshow("img2", img2)

    # 投影变换对应的点
    src = np.array([[0, 0], [w, 0], [0, h], [w, h]], np.float32)
    dst = np.array([[-20, 1017], [102, 452], [396, 1089], [437, 573]], np.float32)
    # 计算投影变换矩阵
    p = cv2.getPerspectiveTransform(src, dst)
    # 投影变换
    r = cv2.warpPerspective(img2, p, (width, height))
    print("r", r.shape, type(r), r.dtype)
    cv2.imshow("r", r)

    # TODO mask
    mask = np.ceil(r / (r + 1)) * 255
    mask = mask.astype(img1.dtype)
    print("mask", mask.shape, type(mask), mask.dtype)
    cv2.imshow("mask", mask)

    img1x = cv2.bitwise_or(img1, mask)
    cv2.imshow("img1x", img1x)

    # rx = cv2.bitwise_not(r)
    img1y = cv2.bitwise_xor(img1x, r)
    img1y = img1y + r * 2
    cv2.imshow("img1y", img1y)

    # cv2.imwrite("ok.jpg", img1y)

    # cv2.bitwise_or

    iz = img1x + r
    cv2.imshow("iz", iz)

    # mx = cv2.bitwise_or(img1, r)
    # mx = cv2.bitwise_or(mx, r)
    # # cv2.imshow("mx", mx)
    #
    # # mx = mx.bitwise_not()
    #
    # # cv2.imshow("rt", rt)

    # maskx = np.ones(img1.shape, img1.dtype)
    # maskx = maskx[50:-50, 50:-50, :]
    # r = r[50:-50, 50:-50, :]
    # jz = cv2.seamlessClone(r, img1, maskx, (int(height/2)-50, int(width/2)-50), cv2.MIXED_CLONE)
    # cv2.imshow("jz", jz)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
