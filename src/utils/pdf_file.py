# -*- coding: utf-8 -*-

import os

import pypdf
from pypdf import PdfReader, PdfWriter
from pypdf.constants import PageLabelStyle
from pypdf.generic import Fit


# 读取书签 outline
def read_outline_items(pdf_path):
    print()
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


# # 添加书签 outline
# def write_outline_items(pdf_from_path, pdf_to_path):
#     writer = PdfWriter()
#
#     with open(pdf_from_path, 'rb') as pdf_from_file:
#         reader = PdfReader(pdf_from_file)
#         for page, num in zip(reader.pages, range(reader.get_num_pages())):
#             writer.add_page(page)
#
#     writer.write(pdf_to_path)
#     writer.close()


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
    output_file = _check_and_prepare(new_filename, new_path, target_file)

    with open(target_file, 'rb') as target_pdf:
        reader = pypdf.PdfFileReader(target_pdf)
        page_total = reader.getNumPages()
        writer = pypdf.PdfFileWriter()
        for i in page_index_list:
            if 0 <= i <= page_total:
                writer.addPage(reader.getPage(i - 1))
            else:
                print("page index is out of scope:", i)
        with open(output_file, 'ab+') as outfile:
            writer.write(outfile)


def remove_pages(target_file: str, page_wil_remove_list: list, new_path: str = None, new_filename: str = None):
    output_file = _check_and_prepare(new_filename, new_path, target_file)

    with open(target_file, 'rb') as target_pdf:
        reader = pypdf.PdfFileReader(target_pdf)
        page_total = reader.getNumPages()
        writer = pypdf.PdfFileWriter()

        for i in range(1, page_total + 1):
            if i not in page_wil_remove_list:
                writer.addPage(reader.getPage(i - 1))
        with open(output_file, 'ab+') as outfile:
            writer.write(outfile)


def _check_and_prepare(new_filename, new_path, target_file):
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
