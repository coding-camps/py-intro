# -*- coding: utf-8 -*-

import base64


def image2Base64Str(img):
    with open(img, 'rb') as imgFile:
        imgStr = base64.b64encode(imgFile.read())
    return imgStr;


def base64Str2Image(imgStr, imgFile="./imgstr.jpg"):
    imgData = base64.b64decode(imgStr)
    with open(imgFile, 'wb') as imgF:
        imgF.write(imgData)
