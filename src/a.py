# -*- coding: utf-8 -*-
# 导入库
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0,6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
plt.plot(x,y1, label="sin(x)")
plt.plot(x,y2, label="cos(x)", linestyle='--')

# 图形标记
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin & cos')
# plt.legend(['sin(x)','cos(x)'])
plt.legend()

# 显示图形
plt.show()
