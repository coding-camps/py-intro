# -*- coding: utf-8 -*-
import os


def copy_text_file(src, des) -> None:
    '''
    复制文本文件。
    :param src: 文本文件源位置
    :param des: 文件目的位置
    :return: 无
    '''
    # with (open(src, 'r'), open(des, 'w')) as (src_file, des_file):
    with open(src, 'r') as src_file, open(des, 'w') as des_file:
        src_lines = src_file.readlines()
        des_file.writelines(src_lines)


def list_files(root_path):
    '''
    广度优先搜索，查找指定目录下所有文件，并返回。
    返回形式：[(filepath, filename), ...]
    '''
    dir_list = []
    file_list = []
    dir_list.append(root_path)
    while len(dir_list) != 0:
        dir_item = dir_list.pop()
        for item in os.listdir(dir_item):
            full_item = os.path.join(dir_item, item)
            if os.path.isdir(full_item):
                dir_list.append(full_item)
            else:
                file_list.append((dir_item, item))
    return file_list
