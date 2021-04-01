# coding = utf-8
# import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib import font_manager
from matplotlib import rcParams
import os


# 载入宋体，注意修改文件目录
# /Users/cosmos/WorkSpace/coding-camps/py-intro/res/fonts/STHeiti Light.ttc
pathx = os.path.join(os.path.join(os.path.dirname(__file__)), r'../res/fonts/STHeiti Light.ttc')
real_path = os.path.abspath(pathx)
print(pathx)
print(real_path)
print(os.path.exists(real_path))
STHeiti = FontProperties(fname=real_path)
# font_manager.fontManager.addfont(STHeiti)
font_manager.fontManager.addfont(real_path)


# 全局设置字体及大小，设置公式字体即可
config = {
    # "mathtext.fontset":'stix',
    "mathtext.fontset":'cm',
    "font.family":'sans-serif',
    "font.sans-serif": ['STHeiti Light'],
    # 处理负号，即-号
    'axes.unicode_minus': False,
    "font.size": 12
}
if __name__ == '__main__':
    rcParams.update(config)

    x = np.linspace(0, 10, 1000)
    plt.figure(dpi=100)
    plt.plot(x, np.sin(x), label = u'宋-1')
    plt.plot(x, np.cos(x), label = u'宋-2')
    plt.legend()
    plt.title(u'宋体 TItle $y=sin(x)$')
    plt.xlabel(u'宋体 xlabel')
    plt.ylabel(u'宋体 ylabel')
    plt.text(3, 0.5, u'图像 TuXiang $y=x^2$')
    # plt.savefig('A0.png')
    plt.show()

