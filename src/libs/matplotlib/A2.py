# coding = utf-8
# coding = utf-8
import numpy as np
from matplotlib import pyplot as plt


myfont = {
    # "mathtext.fontset": 'stix',
    "family": "Songti SC",
    "size": 12,
    "weight": "bold"
}

plt.rc("font", **myfont)
plt.rc("axes", unicode_minus=False)
# plt.style.use("ggplot")

if __name__ == '__main__':
    fig = plt.figure()
    plt.title("Biaoti 二次函数$y=x^2$")
    plt.xlabel("$x$轴")
    plt.ylabel("$y$轴")
    plt.title("二次函数$y=x^2$")
    plt.xlabel("$x$轴Zhou")
    plt.ylabel("$y$轴Zhou", rotation=0)
    plt.xticks(rotation=45)
    plt.xlim(-10, 10)
    plt.ylim(-20, 100)
    x = np.arange(-10, 10, 0.01)
    y = [t**2 for t in x]
    plt.plot(x, y, color='blue', label='函数图像')
    # plt.savefig("A2.png")
    plt.show()

