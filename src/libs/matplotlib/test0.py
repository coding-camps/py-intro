# coding = utf-8
import numpy as np
from matplotlib import pyplot as plt

# plt.rcParams['font.family'] = ['Songti SC']
# plt.rcParams['font.sans-serif'] = ['Songti SC']


# from matplotlib import font_manager
# my_font = font_manager.FontProperties(fname='/System/Library/Fonts/Supplemental/Songti.ttc')

if __name__ == '__main__':
    fig = plt.figure()
    plt.title("二次函数$y=x^2$")
    plt.xlabel("$x$轴")
    plt.ylabel("$y$轴")
    # plt.title("二次函数$y=x^2$", fontproperties=my_font)
    # plt.xlabel("$x$轴", fontproperties=my_font)
    # plt.ylabel("$y$轴", fontproperties=my_font)
    plt.xlim(-10, 10)
    plt.ylim(-20, 100)
    x = np.arange(-10, 10, 0.01)
    y = [t**2 for t in x]
    plt.plot(x, y, color='blue', label='函数图像')
    plt.legend()
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.savefig("test-0.png")
    plt.show()
