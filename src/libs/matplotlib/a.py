# -*- coding: utf-8 -*-
# 导入库
import matplotlib.pyplot as plt
import numpy as np

# 处理中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 生成数据
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
line_sin = plt.plot(x, y1, label="正弦函数 sin(x)")
line_cos = plt.plot(x, y2, label="余弦函数 cos(x)", linestyle='--')

# 图形标记
plt.xlabel('x 轴')
plt.ylabel('y 轴')
plt.title('sin & cos 函数')
# plt.legend([line_sin, line_cos],  ['sin(x)','cos(x)'], loc = 'best')
# plt.legend(handles=[line_sin, line_cos])
plt.legend()

# 显示图形
plt.show()
