# -*- coding: utf-8 -*-
import numpy as np

from utils.pics import warp

# import seaborn as sns

if __name__ == '__main__':
    # print(sns.get_data_home())
    # print(sns.get_dataset_names())

    pic1 = r'../pics/template-1.jpg'
    pic2 = r'../pics/paste-1.jpg'
    save_path = r'../../pics/ok.jpg'

    w = 1080
    h = 604
    src = np.array([[0, 0], [w, 0], [0, h], [w, h]], np.float32)
    dst = np.array([[-20, 1017], [102, 452], [396, 1089], [437, 573]], np.float32)
    warp(pic1, pic2, src, dst)
