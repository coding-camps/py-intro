# -*- encoding: utf-8 -*-
import math

a = input("请输入a：")
b = input("请输入b：")
c = input("请输入c：")
# a, b, c = -1, 2, 3
print(f"输入的数据是：a={a}, b={b}, c={c}")
a = float(a)
b = float(b)
c = float(c)
delta = b**2 - 4*a*c
if delta >= 0:
    print(f"delta>=0: delta={delta}")
    kf_delta = math.sqrt(delta)
    x1 = (-b + kf_delta)/2*a
    x2 = (-b - kf_delta)/2*a
    print(f"方程的两个根是：x1={x1}, x2={x2}")
else:
    print(f"delta<0: delta={delta}")
