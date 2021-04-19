# -*- encoding: utf-8 -*-
import os
from datetime import datetime
from os import path

import subprocess

from PIL import Image

import mainx
from info_reader import clear_exif_v2, read_exif
from src.utils.datetime_utils import random_time_cmd
import atexit

def images_to_pdf(files: list, pdf_file: str):
    images = [Image.open(img).convert('RGB') for img in files]
    images[0].save(pdf_file, save_all=True, append_images=images[1:])
    print("image -> pdf : ok")


def mk_cmd_stat(filename: str) -> list[str]:
    return [f"stat -x {filename}"]


def mk_cmd_touch(filename: str, dtime: datetime) -> list[str]:
    dtinfo = f"{dtime.strftime('%Y%m%d%H%M%S')}"
    return [f"touch -mt {dtinfo}  {filename}"]


def mk_cmd_setfile(filename: str, dtime: datetime) -> list[str]:
    dtinfo = f"{dtime.month}/{dtime.day}/{dtime.strftime("%Y %H:%M:%S")}"
    return [
        f"setfile -d '{dtinfo}' {filename}",
        f"setfile -m '{dtinfo}' {filename}",
    ]

def create_new_filename(old_filename:str)->str:
    idx = old_filename.rfind(".")
    return f"x-{old_filename[:idx]}.{old_filename[idx+1:]}"

def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"exit remove file at exit: {file_path}")



if __name__ == '__main__':
    root_dir1 = r"/Users/cosmos/okj/资料2"
    root_dir2 = r"/Users/cosmos/okj/资料2-x"
    root_dir3 = r"/Users/cosmos/okj/资料2-y"
    pdf_name = r"ziliao2.pdf"
    pdf_new_name = r"ziliao2-ok.pdf"
    # daytime = datetime.strptime("2024-06-08 01:02:03", "%Y-%m-%d %H:%M:%S")

    # prepare file list
    _, _, file_list = next(os.walk(root_dir1))
    if '.DS_Store' in file_list:
        file_list.remove('.DS_Store')
    for file in file_list:
        if file.lower().endswith('.pdf'):
            file_list.remove(file)
    file_list.sort()
    file_cnt = len(file_list)
    # prepare random time
    # random_time = random_time_cmd(file_cnt, daytime)


    # clear exif info
    for i in range(file_cnt):
        file = file_list[i]
        file_new = create_new_filename(file)
        print()
        print(file, file_new)
        read_exif(path.join(root_dir1, file))
        clear_exif_v2(path.join(root_dir1, file), path.join(root_dir2, file))
        # remove at exit
        # atexit.register(remove_file, path.join(root_dir2, file_new))
        # update_file
        # if os.path.exists(path.join(root_dir2, file_new)):
        #     cmd1 = mk_cmd_stat(path.join(root_dir2, file_new))
        #     cmd2 = mk_cmd_setfile(path.join(root_dir2, file_new), random_time[i])
        #     cmd_list = cmd1 + cmd2
        #     mainx.safe_call(cmd_list)


    # update image file date and time
    # random_time = random_time_cmd(file_cnt, daytime)
    _, _, dir2_files = next(os.walk(root_dir2))
    if '.DS_Store' in dir2_files:
        dir2_files.remove('.DS_Store')
    dir2_files.sort()
    for i in range(len(dir2_files)):
        file = dir2_files[i]
        cwd = root_dir2
        cmd1 = mk_cmd_stat(file)
        # mainx.run_cmd(cmd1[0], cwd=cwd)
        # mainx.safe_run_cmds(cmd1, cwd=cwd)
        # dtime = random_time[i]
        # cmd2 = mk_cmd_setfile(file, dtime)
        # mainx.safe_run_cmds(cmd2, cwd=cwd)
        # mainx.run_cmd(cmd2[0], cwd=cwd)
        # mainx.run_cmd(cmd1[0], cwd=cwd)




    # prepare to make pdf file
    _, _, dir2_files = next(os.walk(root_dir2))
    if '.DS_Store' in dir2_files:
        dir2_files.remove('.DS_Store')
    for file in dir2_files:
        if file.lower().endswith('.pdf'):
            dir2_files.remove(file)
    dir2_files.sort()
    # make pdf file
    images = []
    for i in range(len(dir2_files)):
        file = dir2_files[i]
        full_path = path.join(root_dir2, file)
        images.append(full_path)
    pdf_path = path.join(root_dir3, pdf_name)
    print(pdf_path)
    images_to_pdf(images, pdf_path)

    # # update pdf date and file



