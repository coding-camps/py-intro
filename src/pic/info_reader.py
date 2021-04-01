# -*- encoding: utf-8 -*-
import os, time
import sys
import exifread
import piexif
from PIL import Image
# from PIL.ExifTags import TAGS


def read_exif(file):
    with open(file, 'rb') as file_raw:
        exif_info = exifread.process_file(file_raw)
        print(type(exif_info))
        print(exif_info)

def read_size(file, new_file):
    img = Image.open(file)
    old_size = img.size
    img_new = Image.open(new_file)
    new_size = img_new.size
    print(f'old_size = {old_size}')
    print(f'new_size = {new_size}')


def clear_exif(file, new_file):
    image = Image.open(file)
    data = list(image.getdata())
    img_no_exif = Image.new(image.mode, image.size)
    img_no_exif.putdata(data)
    img_no_exif.save(new_file)
    return

def clear_exif_v2(file, new_file):
    with Image.open(file) as img:
        data = img.tobytes()
        img_no_exif = Image.frombytes(img.mode, img.size, data)
        img_no_exif.save(new_file)


def clear_exif_v3(file, new_file):
    # exif_dict = piexif.load(file)
    # exif_bytes = piexif.dump({"EXIF": piexif.ExifDict()})
    piexif.remove(file, new_file)
