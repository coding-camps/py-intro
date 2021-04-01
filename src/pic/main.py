# -*- encoding: utf-8 -*-
import os
from os import path

from PIL import Image

from info_reader import read_exif
from pic.info_reader import read_size, clear_exif_v2


def images_to_pdf(files: list, pdf_file: str):
    images = [Image.open(img).convert('RGB') for img in files]
    images[0].save(pdf_file, save_all=True, append_images=images[1:])
    print("ok")


if __name__ == '__main__':
    root_dir = r'/Users/cosmos/Pictures'
    dir1 = r"huading"
    dir2 = r"huading2"
    dir3 = r'huading3'
    pdf_name = r'sifang.pdf'

    dir1_path = path.join(root_dir, dir1)
    dir2_path = path.join(root_dir, dir2)
    pdf_path = path.join(root_dir, dir3)

    _, _, file_list = next(os.walk(dir1_path))
    if '.DS_Store' in file_list:
        file_list.remove('.DS_Store')
    for file in file_list:
        if file.lower().endswith(('.pdf')):
            file_list.remove(file)
            break
    file_list.sort()
    cnt = 0
    for file in file_list:
        file1_path = path.join(dir1_path, file)
        file2_path = path.join(dir2_path, file)
        cnt += 1
        print(cnt)
        read_exif(file1_path)
        clear_exif_v2(file1_path, file2_path)
        # read_exif(file2_path)
        # read_size(file1_path, file2_path)

    _, _, dir2_files = next(os.walk(dir2_path))
    if '.DS_Store' in dir2_files:
        dir2_files.remove('.DS_Store')
    for dir2_file in dir2_files:
        if dir2_file.lower().endswith(('.pdf')):
            dir2_files.remove(dir2_file)
            break
    dir2_files.sort()
    images = []
    for file in dir2_files:
        full_path = path.join(dir2_path, file)
        images.append(full_path)
    pdf_path = path.join(pdf_path, 'sifangx.pdf')
    print(pdf_path)
    images_to_pdf(images, pdf_path)
