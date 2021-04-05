# -*- encoding: utf-8 -*-

import os
import pypdf
from datetime import datetime

def mod_ctime(pdf_file, pdf_nfile, new_ctime):
    with open(pdf_file, 'rb') as file:
        reader = pypdf.PdfReader(file)
        writer = pypdf.PdfWriter()

        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])

            writer.add_metadata({
                '/Title': '',
                '/CreationDate': new_ctime,
                '/ModDate': new_ctime,
                '/Producer': "ProducerX",
                '/Creator': "CreatorX",
            })

            with open(pdf_nfile, 'wb') as new_file:
                writer.write(new_file)


if __name__ == '__main__':
    # pdf_file = r'/Users/cosmos/EBooks/zl/ziliao.pdf'
    # pdf_nfile = r'/Users/cosmos/EBooks/zl/ziliao-new.pdf'
    pdf_file = r''
    pdf_nfile = r''
    new_ctime = datetime(2025,6, 1, 10,8,6)
    utc_time = "+08'00'"  # UTC time optional
    print(new_ctime.strftime(f"D\072%Y%m%d%H%M%S{utc_time}"))
    new_ctime = new_ctime.strftime(f"D\072%Y%m%d%H%M%S{utc_time}")
    mod_ctime(pdf_file, pdf_nfile, new_ctime)
