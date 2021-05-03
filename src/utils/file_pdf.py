# -*- encoding: utf-8 -*-
from datetime import datetime

import pypdf
from PIL import Image
from pypdf import PdfReader, PdfWriter
from pypdf.constants import PageLabelStyle
from pypdf.generic import Fit

from file_common import prepare_filename_suffix


# 读取书签 outline
def read_outline_items(pdf_path) -> None:
    """
    读取书签 outline 并在控制台输出。
    :param pdf_path: 指定的PDF文件路径
    :return: 无
    """
    print(pdf_path)
    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        outline_items = reader.outline
        for outline_item in outline_items:
            if isinstance(outline_item, list):
                for item in outline_item:
                    print('\t', item)
            else:
                print(outline_item)
                print('  | type:', type(outline_item))
                print('  | title:', outline_item.title)
                print('  | page:', outline_item.page)
                print('  | typ:', outline_item.typ, '-', type(outline_item.typ))
                print('  | color:', outline_item.color)
                print('  | outline_count', outline_item.outline_count)


# 添加书签 outline
def write_outline_items(pdf_from_path, pdf_to_path):
    writer = PdfWriter()

    with open(pdf_from_path, 'rb') as pdf_from_file:
        reader = PdfReader(pdf_from_file)
        for page, num in zip(reader.pages, range(reader.get_num_pages())):
            writer.add_page(page)

    writer.write(pdf_to_path)
    writer.close()


# 读取标签 label
def read_page_labels(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        labels = reader.page_labels
        for label in labels:
            print(label)


# 添加标签 label 和 bookmark
def write_labels(pdf_from_path, pdf_to_path, lable_idxs, bookmarks):
    writer = PdfWriter()
    with open(pdf_from_path, 'rb') as pdf_from_file:
        reader = PdfReader(pdf_from_file)
        for page in reader.pages:
            writer.add_page(page)
        writer.set_page_label(lable_idxs[0] - 1, lable_idxs[1] - 2, PageLabelStyle.UPPERCASE_LETTER)
        writer.set_page_label(lable_idxs[1] - 1, lable_idxs[2] - 2, PageLabelStyle.LOWERCASE_ROMAN)

    for bookmark in bookmarks:
        mark1 = writer.add_outline_item(title=bookmark['title'], page_number=bookmark['page_number'] - 1,
                                        color=(0, 0, 1), bold=True, fit=Fit.fit_horizontally(), is_open=False)
        for submark in bookmark['sub_marks']:
            writer.add_outline_item(title=submark['title'], page_number=submark['page_number'] - 1, parent=mark1,
                                    italic=True,
                                    fit=Fit.fit_horizontally())

    writer.write(pdf_to_path)
    writer.close()


# 保存图片
def save_pics(pdf_from, pics_to):
    with open(pdf_from, 'rb') as pdf_from_file:
        reader = PdfReader(pdf_from_file)
        for page_idx, page in enumerate(reader.pages):
            print(f'page={page_idx}')
            # for img_idx, img in enumerate(page.images):
            #     print(f'\timg={img_idx}')
            # img = page["/Annots"][0].get_object()["/AP"]["/N"]["/Resources"]["/XObject"]["/Im4"].decode_as_image()
            # img.show()
    pass


# page_picker
def page_picker(target_file: str, page_index_list: list, new_path: str = None, new_filename: str = None):
    output_file = prepare_filename_suffix(new_filename, new_path, target_file)

    with open(target_file, 'rb') as target_pdf:
        reader = pypdf.PdfReader(target_pdf)
        page_total = len(reader.pages)
        writer = pypdf.PdfWriter()
        for i in page_index_list:
            if 0 <= i <= page_total:
                writer.add_page(reader.pages[i - 1])
            else:
                print("page index is out of scope:", i)
        with open(output_file, 'ab+') as outfile:
            writer.write(outfile)


def remove_pages(target_file: str, page_wil_remove_list: list, new_path: str = None, new_filename: str = None):
    output_file = prepare_filename_suffix(new_filename, new_path, target_file)

    with open(target_file, 'rb') as target_pdf:
        reader = pypdf.PdfReader(target_pdf)
        page_total = len(reader.pages)
        writer = pypdf.PdfWriter()

        for i in range(1, page_total + 1):
            if i not in page_wil_remove_list:
                writer.add_page(reader.pages[i - 1])
        with open(output_file, 'ab+') as outfile:
            writer.write(outfile)


def modify_create_datetime(pdf_origin_file: str, pdf_new_file: str, new_create_time: datetime,
                           new_modify_time: datetime = None):
    """
    修改pdf文件的内部创建时间和修改时间。时间格式可通过下方的代码实现。

    datetime(2025,6, 1, 10,8,6).strftime(f"D\072%Y%m%d%H%M%S+08'00'")

    :param pdf_origin_file: 源 PDF 文件
    :param pdf_new_file:    新 PDF 文件
    :param new_create_time: PDF 文件内部创建时间
    :param new_modify_time: PDF 文件内部修改时间
    :return:
    """
    # 时间有关的参考代码
    # new_ctime = datetime(2025,6, 1, 10,8,6)
    # utc_time = "+08'00'"  # UTC time optional
    # print(new_ctime.strftime(f"D\072%Y%m%d%H%M%S{utc_time}"))
    # new_ctime = new_ctime.strftime(f"D\072%Y%m%d%H%M%S{utc_time}")
    # new_ctime = datetime(2025,6, 1, 10,8,6).strftime(f"D\072%Y%m%d%H%M%S+08'00'")
    # print(new_ctime)

    if new_modify_time is None:
        new_modify_time = new_create_time
    with open(pdf_origin_file, 'rb') as file:
        reader = pypdf.PdfReader(file)
        writer = pypdf.PdfWriter()

        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])

            writer.add_metadata({
                '/Title': '',
                '/CreationDate': new_create_time,
                '/ModDate': new_modify_time,
                '/Producer': "",
                '/Creator': "",
            })

            with open(pdf_new_file, 'wb') as new_file:
                writer.write(new_file)


def images_to_pdf(files: list, pdf_file: str):
    images = [Image.open(img).convert('RGB') for img in files]
    images[0].save(pdf_file, save_all=True, append_images=images[1:])
    print("image -> pdf : ok")
