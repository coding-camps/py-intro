# -*- encoding: utf-8 -*-

import os
from os import path


def remove_temp(files, root=None):
    if '.DS_Store' in files:
        files.remove('.DS_Store')
        os.remove(path.join(root, '.DS_Store'))


def walk_dir(root_dir):
    _, dirs, files = next(os.walk(root_dir))
    remove_temp(files, root_dir)

    temp_files = []
    for file in files:
        temp_files.append(path.join(root_dir, file))

    temp_dirs = []
    for dir in dirs:
        temp_dirs.append(path.join(root_dir, dir))

    return temp_files, temp_dirs


if __name__ == '__main__':
    dir = r'/Volumes/blank/ebooks-数学类—电子教材合集'

    pdf_files = []
    temp_dirs = []

    files, dirs = walk_dir(dir)
    pdf_files.extend(files)
    temp_dirs.extend(dirs)

    while len(temp_dirs) > 0:
        temp_dir = temp_dirs.pop()
        files, dirs = walk_dir(temp_dir)
        pdf_files.extend(files)
        temp_dirs.extend(dirs)

    counter = 0
    for file in pdf_files:
        counter += 1
        print(counter)

        new_name = path.basename(file).replace('》', '_').replace('《', '')
        new_file = path.join(path.dirname(file), new_name)

        print(file)
        print(new_file)

        os.rename(file, new_file)

    print(len(pdf_files))
