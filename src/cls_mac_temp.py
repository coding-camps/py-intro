# -*-coding:utf-8-*-

import os
from os import path

def cls_mac_temp(root_path:str):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.startswith('.'):
                temp_file = path.join(root, file)
                print(temp_file)
                os.remove(temp_file)
        # for dir in dirs:
        #     if dir.startswith('._'):
        #         print(os.path.join(root, dir))




if __name__ == '__main__':
    root = r"F:\some_dir"
    cls_mac_temp(root)
