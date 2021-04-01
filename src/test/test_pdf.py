# -*- coding: utf-8 -*-
import os

from utils.pdf_file import *

if __name__ == '__main__':
    '''
    root_path = r'/Users/cosmos/Downloads/ebook-test'
    file_cjx = os.path.join(root_path, r'数学分析-陈纪修E3上_含目录.pdf')
    file_sjh = os.path.join(root_path, r'史济怀上(清晰).pdf')
    file_cjx_out = os.path.join(root_path, r'数学分析-陈纪修E3上_含目录-out.pdf')
    file_sjh_out = os.path.join(root_path, r'史济怀上(清晰)-out.pdf')
    '''

    '''
    # read_outline_items(file_cjx)
    # read_page_labels(file_cjx)
    # read_page_labels(file_sjh)
    '''

    '''
    label_idxs = (1, 14, 18)

    bookmarks = [
        {
            "title": "第一章：实数与数列极限",
            "page_number": 18,
            "sub_marks": [
                {
                    "title": "1.1-实数",
                    "page_number": 18,
                }, {
                    "title": "1.2-收敛数列",
                    "page_number": 25,
                }, {
                    "title": "1.3-收敛性质",
                    "page_number": 30,
                }
            ]
        }, {
            "title": "第二章：函数第连续性",
            "page_number": 72,
            "sub_marks": [
                {
                    "title": "2.1 集合之映射",
                    "page_number": 72,
                }, {
                    "title": "2.2 集合之实力",
                    "page_number": 76,
                }
            ]
        }
    ]

    write_labels(file_sjh, file_sjh_out, label_idxs, bookmarks)
    # read_outline_items(file_sjh_out)
    '''

    pdf_path = r'/Users/cosmos/WorkSpace/books-mine/Advanced-Algebra-Blog-xie/articles/'
    save_pics(os.path.join(pdf_path, 'tikz-立体几何.pdf'), os.path.join(pdf_path, 'pics'))
