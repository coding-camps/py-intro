# -*- encoding: utf-8 -*-

import base64

from PIL import Image


def image_to_base64(img: str) -> bytes:
    """
    将图片转换为 Base64 格式字符串。
    :param img: 要转换的图片路径
    :return: 转换后的字符串
    """
    with open(img, 'rb') as img_file:
        img_str = base64.b64encode(img_file.read())
    return img_str


def base64_to_image(img_str: bytes, img_file: str = "./img-base64.jpg"):
    """
    将代表图片的 Base64 字符串转换为对应的图片。
    :param img_str: 代表图片的 Base64 字符串
    :param img_file: 转换后的图片路径和名称，默认为当前工作目录的 ./img-base64.jpg
    :return: 无返回值
    """
    img_data = base64.b64decode(img_str)
    with open(img_file, 'wb') as imgF:
        imgF.write(img_data)


def images_combine(img_paths: list, save_name='combined.img'):
    """
    水平方向合并图片。
    :param img_paths:
    :param save_name:
    :return:
    """
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
