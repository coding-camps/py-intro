# -*- encoding: utf-8 -*-

import os
from os import path

def cls_mac_temp(root_path):
    cnt_dir = 0
    cnt_file = 0
    for root, dirs, files in os.walk(root_path):
        print('root -> ', root)
        print("dir cnt ->", len(dirs))
        for dir in dirs:
            temp_path = path.join(root, dir)
            print(temp_path)
        print("file cnt ->", len(files))
        for file in files:
            temp_path = path.join(root, file)
            print(temp_path)
        print(end="\n")
        cnt_dir += len(dirs)
        cnt_file += len(files)
    print("total dir  ->", cnt_dir)
    print("total file ->", cnt_file)


if __name__ == '__main__':
    root = r"/Users/cosmos/Desktop/工作学习资料"
    root = r"/Users/cosmos/Desktop/微信文件"
    cls_mac_temp(root)
