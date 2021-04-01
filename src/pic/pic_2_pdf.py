# -*- encoding: utf-8 -*-
import os
from os import path

from PIL import Image

if __name__ == '__main__':
    root_dir = r'/Users/cosmos/Pictures/xx博览会资料05'
    pdf_name = r'xx' + r'苏州微奈-三辊机.pdf'

    _, _, files = next(os.walk(root_dir))
    img_files = []
    for file in files:
        print(file, len(files))
        # 删除 mac 或 windows 缓存文件（Thumbs.db）
        if '.DS_Store' == file or file.lower().endswith(".db"):
            continue
        if file.lower().endswith('.pdf'):
            continue
        img_file = path.join(root_dir, file)
        img_files.append(img_file)
    img_files.sort()

    pdf_path = path.join(root_dir, pdf_name)

    images1 = []
    # for img_file in img_files:
    #     print(img_file)
    #     with Image.open(img_file) as img:
    #         img_data = img.tobytes()
    #         img_data_no_exif = Image.frombytes(img.mode, img.size, img_data)
    #         images1.append(img_data_no_exif.convert('RGB'))

    images1 = [Image.open(img).convert('RGB') for img in img_files]

    images1[0].save(pdf_path, save_all=True, append_images=images1[1:])
    print("ok")
