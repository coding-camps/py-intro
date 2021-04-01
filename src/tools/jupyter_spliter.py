# -*- coding: utf-8 -*-
import os

import nbformat


def read_ipynb(ipynb_file, sub_folder_name):
    # 读取原始Notebook文件
    with open(ipynb_file, 'r', encoding='utf-8') as f:
        origin_notebook = nbformat.read(f, as_version=4)
    print(origin_notebook.metadata)

    # 分割Notebook的逻辑
    new_notebooks = []
    current_notebook = nbformat.v4.new_notebook()
    new_notebooks.append(current_notebook)
    for cell in origin_notebook.cells:
        if cell.cell_type == 'markdown' and cell.source.startswith('## '):
            current_notebook = nbformat.v4.new_notebook()
            new_notebooks.append(current_notebook)
        current_notebook.cells.append(cell)

    # 控制台输出
    for i, new_notebook in enumerate(new_notebooks):
        print(i, "-" * 100)
        print(new_notebook.metadata)
        print(len(new_notebook.cells))
        for cell in new_notebook.cells:
            print(cell)

    # 将Notebook写入新文件
    origin_name = os.path.basename(ipynb_file).split('.')
    prefix_name = origin_name[0]
    suffix_name = origin_name[-1]
    sub_path = os.path.join(os.path.dirname(ipynb_file), sub_folder_name)
    os.mkdir(sub_path)
    for i, nb in enumerate(new_notebooks):
        with open(os.path.join(sub_path, f'{prefix_name}-{i + 1}.{suffix_name}'), 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)


def info(ipynb_file):
    # 读取原始Notebook文件
    with open(ipynb_file, 'r', encoding='utf-8') as f:
        origin_notebook = nbformat.read(f, as_version=4)
    print(origin_notebook.metadata)


if __name__ == '__main__':
    ipynb_file = r'../libs/01-numpy.ipynb'
    sub_folder_name = 'numpy2'
    read_ipynb(ipynb_file, sub_folder_name)
    # info(r'../libs/numpy/01-numpy-1.ipynb')
    # info(r'../libs/numpy/01-numpy-2.ipynb')
    # info(r'../libs/01-numpy.ipynb')
