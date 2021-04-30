# -*- encoding: utf-8 -*-

import os
from os import path
from pathlib import Path
from typing import Tuple, List


def list_files(root_path) -> List[str]:
    """
    广度优先搜索，查找指定目录下所有文件，并返回。
    返回形式：[(filepath, filename), ...]
    :param root_path:
    :return:
    """
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


def count_files_and_dirs(root_path: str) -> Tuple[int, int]:
    """
    统计指定目录及其子目录中的文件和文件夹数量。
    :param root_path:
    :return:
    """
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
    return cnt_dir, cnt_file


def copy_text_file(src, des) -> None:
    """
    将文本文件按行从源目录复制到指定位置。
    :param src: 文本文件源位置
    :param des: 文件目标位置
    :return: 无
    """
    # with (open(src, 'r'), open(des, 'w')) as (src_file, des_file):
    with open(src, 'r') as src_file, open(des, 'w') as des_file:
        src_lines = src_file.readlines()
        des_file.writelines(src_lines)


def walk_and_will_del(root: str, pattern: str, will_del: bool = False) -> int:
    """
    根据指定的文件匹配模式，遍历指定目录下的所有文件和子文件夹，并根据指定的标记决定是否删除文件。
    并打印指定的匹配文件。
    :param root: 需要处理的指定目录
    :param pattern: 指定的文件匹配模式
    :param will_del: 是否删除的标记
    :return: 匹配的文件数量
    """
    # 遍历
    ptn_files = Path(root).glob(pattern)
    prn_file_cnt = 0
    for ptn_file in ptn_files:
        prn_file_cnt += 1
        # 打印匹配的文件夹信息
        print(f"{prn_file_cnt:4d}: {ptn_file.relative_to(root)}")
        # 删除文件
        if will_del and ptn_file.exists():
            ptn_file.unlink()
    print(f"specific path: {root}")
    return prn_file_cnt


def cls_mac_temp(root_path: str, will_del: bool = False) -> None:
    """
    清理指定目录中macOS的临时文件（如： .DS_Store 和 ._xxx）。
    :param root_path: 需要处理的匹配目录
    :param will_del: 是否删除的标记
    :return: 无返回值
    """
    cnt1 = walk_and_will_del(root_path, "**/._*", will_del)
    cnt2 = walk_and_will_del(root_path, "**/.DS_Store", will_del)
    print(f"total temp files: {cnt1} + {cnt2} = {cnt1 + cnt2}")


def prepare_filename_suffix(new_filename, new_path, target_file):
    """
    根据指定文件名检查是否存在，如果不存在则返回原文件名，如果存在则返回增加数字后缀的新文件名。
    :param new_filename:
    :param new_path:
    :param target_file:
    :return:
    """
    if not os.path.isfile(target_file):
        raise Exception("target file path must be a file: " + target_file)
    if new_path is None:
        new_path = os.path.dirname(target_file)
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    if new_filename is None:
        index = 1
        base_filename, file_ext = (os.path.basename(target_file).split('.'))
        file_ext = '.' + file_ext
        temp_filename = base_filename + "-" + str(index) + file_ext
        while os.path.exists(os.path.join(new_path, temp_filename)):
            index += 1
            temp_filename = base_filename + "-" + str(index) + file_ext
        new_filename = temp_filename
    output_file = os.path.join(new_path, new_filename)
    print("output file", "=>", output_file)
    return output_file
