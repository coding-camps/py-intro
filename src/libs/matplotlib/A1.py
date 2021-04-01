# coding = utf-8
import numpy as np
from matplotlib import pyplot as plt

my_fontdict = {"family": "STHeiti Light", "color": "r"}

if __name__ == '__main__':
    x = np.linspace(-10, 10, 1000)
    plt.figure(dpi=200)
    plt.plot(x, np.sin(x), label = u'宋体Songti-1')
    plt.plot(x, np.cos(x), label = u'宋体Songti-2')
    plt.legend()
    plt.title(u'宋体 TItle $y=sin(x)$')
    plt.xlabel(u'宋体 xlabel', fontdict = my_fontdict)
    plt.ylabel(u'宋体 ylabel')
    plt.text(3, 0.5, u'图像 TuXiang $y=x^2$')
    # plt.savefig('A1.png')
    plt.show()

