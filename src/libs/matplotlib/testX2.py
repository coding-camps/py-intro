# coding = utf-8
import numpy as np
from matplotlib import pyplot as plt

myfont = {
    # "mathtext.fontset": 'stix',
    "family": "Songti SC",
    # "size": 12,
    "weight": "bold"
}

plt.rc("font", **myfont)
plt.rc("axes", unicode_minus=False)
plt.style.use("ggplot")

if __name__ == '__main__':
    fig = plt.figure()
    plt.title("二次函数$y=x^2$")
    plt.xlabel("$x$轴")
    plt.ylabel("$y$轴")
    plt.xlim(-10, 10)
    plt.ylim(-20, 100)
    x = np.arange(-10, 10, 0.01)
    y = [t ** 2 for t in x]
    plt.plot(x, y, color='blue', label='函数图像')
    plt.legend()
    # plt.rcParams['font.family'] = ['Songti SC']
    # plt.rcParams['font.sans-serif'] = ['Songti SC']
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.rcParams["mathtext.fontset"] = 'stix'
    # myfont = {
    #     "mathtext.fontset": 'stix',
    #     'font.family': 'Songti SC',
    #     'font.sans-serif': 'Songti SC',
    #     'axes.unicode_minus': False
    # }
    # plt.rcParams.update(myfont)
    plt.savefig("test-x1.png")
    plt.show()
