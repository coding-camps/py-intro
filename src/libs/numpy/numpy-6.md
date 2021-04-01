## 五、函数

### 5.1 字符串函数

字符串函数用于对dtype为numpy.string_或numpy.unicode_的数组执行向量化字符串操作
基于python内置库中的标准字符串函数，在字符数组类（numpy.char）中定义

#### add()
对两个数组的元素进行字符串连接


```
import numpy as np

print(np.char.add(['sunck'], [' good']))
print(np.char.add(['sunck', 'kaige'], [' good', ' nice']))
```

    ['sunck good']
    ['sunck good' 'kaige nice']


#### multiply()
多重连接字符串


```
import numpy as np

print(np.char.multiply("Hello ", 3))
```

    Hello Hello Hello 


#### center()

将字符串居中，并使用指定字符在左侧和右侧进行填充


```
import numpy as np

print(np.char.center(['nice', 'good'], 10, fillchar='*'))
```

    ['***nice***' '***good***']


#### capitalize()
将字符串第一个字母转换为大写


```
import numpy as np

print(np.char.capitalize(['hello world!', 'tom is a good man.']))
```

    ['Hello world!' 'Tom is a good man.']


#### title()
将字符串的每个单词的第一个字母转换为大写。


```
import numpy as np

print(np.char.title(['hello world!', 'tom is a good man.']))
```

    ['Hello World!' 'Tom Is A Good Man.']


#### lower()

数组元素转化为小写


```
import numpy as np

print(np.char.lower(['Hello world!', 'Tom is a GOOD man.']))
```

    ['hello world!' 'tom is a good man.']


#### upper()

数组元素转化为大写


```
import numpy as np

print(np.char.upper(['Hello world!', 'Tom is a GOOD man.']))
```

    ['HELLO WORLD!' 'TOM IS A GOOD MAN.']


#### split()

根据指定分割符对字符串进行分割，并返回数组列表。


```
import numpy as np

print(np.char.split(['Hello world!', 'Tom is a GOOD man.']))
```

    [list(['Hello', 'world!']) list(['Tom', 'is', 'a', 'GOOD', 'man.'])]


#### splitlines()
返回元素中的行列表，以换行符分割。


```
import numpy as np

print(np.char.splitlines(['Hello world!', 'Tom is a\nGOOD\nman.']))
```

    [list(['Hello world!']) list(['Tom is a', 'GOOD', 'man.'])]


#### strip()
移除元素开头或结尾处的特定字符或空格。


```
import numpy as np

print(np.char.strip(['***Hello * World~! * **'], "*"))
print(np.char.strip(['***Hello * World~! * **'], "* "))
print(np.char.strip(['   Hello world!', 'Tom is a GOOD man.    ']))
```

    ['Hello * World~! * ']
    ['Hello * World~!']
    ['Hello world!' 'Tom is a GOOD man.']


#### join()
通过分割符来连接数组中的元素。


```
import numpy as np

print(np.char.join('-', ['Hello', 'World']))
print(np.char.join(['-', ':'], [['Hello', 'World'], ['nice', 'good']]))
```

    ['H-e-l-l-o' 'W-o-r-l-d']
    [['H-e-l-l-o' 'W:o:r:l:d']
     ['n-i-c-e' 'g:o:o:d']]


#### replace()
使用新字符串替换字符串中的所有子字符串。


```
import numpy as np

print(np.char.replace(['Tom is a nice cat.', 'Jerry is a nice mouse.'], 'nice', 'good'))
```

    ['Tom is a good cat.' 'Jerry is a good mouse.']


#### encode()
编码，数组元素依次调用 str.encode()


```
import numpy as np

print(np.char.encode(['Tom', 'Jerry'], 'utf-8'))
```

    [b'Tom' b'Jerry']


#### decode()
解码，数组元素依次调用 str.decode()


```
import numpy as np

a = np.char.encode(['Tom', 'Jerry'], 'utf-8')
print(np.char.decode(a, 'utf-8'))
```

    ['Tom' 'Jerry']


### 5.2 数学函数

#### 标准三角函数 sin(), cos(), tan()


```
import numpy as np

a = np.array([0, 30, 45, 60, 90])
print(np.sin(a * np.pi / 180))
print(np.cos(a * np.pi / 180))
print(np.tan(a * np.pi / 180))
```

    [0.         0.5        0.70710678 0.8660254  1.        ]
    [1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01
     6.12323400e-17]
    [0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00
     1.63312394e+16]


#### 反三角函数 arcsin(), arccos(), arctan()


```
import numpy as np

a = np.array([0, 30, 45, 60, 90])

fsin = np.sin(a * np.pi / 180)
afsin = np.arcsin(fsin)
dfsin = np.degrees(afsin)
print(afsin)
print(dfsin)

fcos = np.cos(a * np.pi / 180)
afcos = np.arccos(fcos)
dfcos = np.degrees(afcos)
print(afcos)
print(dfcos)

ftan = np.tan(a * np.pi / 180)
aftan = np.arctan(ftan)
dftan = np.degrees(aftan)
print(aftan)
print(dftan)
```

    [0.         0.52359878 0.78539816 1.04719755 1.57079633]
    [ 0. 30. 45. 60. 90.]
    [0.         0.52359878 0.78539816 1.04719755 1.57079633]
    [ 0. 30. 45. 60. 90.]
    [0.         0.52359878 0.78539816 1.04719755 1.57079633]
    [ 0. 30. 45. 60. 90.]



```
# 以上代码的简化
import numpy as np


def test_fun(np_fun, np_arc_fun, angles):
    fun = np_fun(angles * np.pi / 180)
    afun = np_arc_fun(fun)
    dfun = np.degrees(afun)
    print(afun)
    print(dfun)


a = np.array([0, 30, 45, 60, 90])
test_fun(np.sin, np.arcsin, a)
test_fun(np.cos, np.arccos, a)
test_fun(np.tan, np.arctan, a)
```

    [0.         0.52359878 0.78539816 1.04719755 1.57079633]
    [ 0. 30. 45. 60. 90.]
    [0.         0.52359878 0.78539816 1.04719755 1.57079633]
    [ 0. 30. 45. 60. 90.]
    [0.         0.52359878 0.78539816 1.04719755 1.57079633]
    [ 0. 30. 45. 60. 90.]


#### 弧度和角度转换函数 degrees(), red2deg(), radians, deg2rad()


```
#### 弧度制转换为角度制 degrees() rad2deg()
import numpy as np

angles_radian = np.array([0, 1 / 6, 1 / 4, 1 / 3, 1 / 2]) * np.pi
print(angles_radian)
print(np.degrees(angles_radian))
print(np.rad2deg(angles_radian))

print()

#### 角度制转换为弧度制 radians() deg2rad()
import numpy as np

angles_degree = [0, 30, 45, 60, 90]
print(angles_degree)
print(np.radians(angles_radian))
print(np.radians(angles_radian) / np.pi * 180)
print(np.deg2rad(angles_radian))
print(np.deg2rad(angles_radian) / np.pi * 180)
```

    [0.         0.52359878 0.78539816 1.04719755 1.57079633]
    [ 0. 30. 45. 60. 90.]
    [ 0. 30. 45. 60. 90.]
    
    [0, 30, 45, 60, 90]
    [0.         0.00913852 0.01370778 0.01827705 0.02741557]
    [0.         0.52359878 0.78539816 1.04719755 1.57079633]
    [0.         0.00913852 0.01370778 0.01827705 0.02741557]
    [0.         0.52359878 0.78539816 1.04719755 1.57079633]


#### 四舍五入函数 around()
作用：返回指定数字的四舍五入值
原型：`numpy.around(a, decimals=0)`
- a 数组
- decimals 舍入的小数位数，默认值为0，如果为负，整数将四舍五入到小数点左侧的位置


```
import numpy as np

x = np.array([1.0, 1.5, 3.456, 1234, 0.12345, 345.34, ])
print(f'x =\n{x}')
print(np.around(x))
print(np.around(x, decimals=1))
print(np.around(x, decimals=-1))
```

    x =
    [1.0000e+00 1.5000e+00 3.4560e+00 1.2340e+03 1.2345e-01 3.4534e+02]
    [1.000e+00 2.000e+00 3.000e+00 1.234e+03 0.000e+00 3.450e+02]
    [1.000e+00 1.500e+00 3.500e+00 1.234e+03 1.000e-01 3.453e+02]
    [   0.    0.    0. 1230.    0.  350.]


#### 向下取整 floor()
作用：向下取整，返回不大于输入值的最大整数，即标量x的下限是最大的值，使得i<=x。
注意在python中，向下取整总是从0舍入。


```
import numpy as np

x = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(f'x =\n{x}')
print(np.floor(x))
```

    x =
    [-1.7  1.5 -0.2  0.6 10. ]
    [-2.  1. -1.  0. 10.]


#### 向上取整 ceil()
作用：向上取整，返回输入值的上限。即，标量x的上限是最小的整数，使得i>=x


```
import numpy as np

x = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(f'x =\n{x}')
print(np.ceil(x))
```

    x =
    [-1.7  1.5 -0.2  0.6 10. ]
    [-1.  2. -0.  1. 10.]


### 5.3 算术函数

#### `add()`, `subtract()`, `multiply()`, `divide()`
作用：加减乘除四则运算，支持广播运算


```
import numpy as np

x = np.arange(6, dtype='f').reshape(2, 3)
print(f'x =\n{x}')
y = np.array([10, 10, 10])
print(f'y =\n{y}')

print("和：\n", np.add(x, y), x + y)
print("差：\n", np.subtract(x, y), x - y)
print("积：\n", np.multiply(x, y), x * y)
print("商：\n", np.divide(x, y), x / y)
```

    x =
    [[0. 1. 2.]
     [3. 4. 5.]]
    y =
    [10 10 10]
    和：
     [[10. 11. 12.]
     [13. 14. 15.]] [[10. 11. 12.]
     [13. 14. 15.]]
    差：
     [[-10.  -9.  -8.]
     [ -7.  -6.  -5.]] [[-10.  -9.  -8.]
     [ -7.  -6.  -5.]]
    积：
     [[ 0. 10. 20.]
     [30. 40. 50.]] [[ 0. 10. 20.]
     [30. 40. 50.]]
    商：
     [[0.  0.1 0.2]
     [0.3 0.4 0.5]] [[0.  0.1 0.2]
     [0.3 0.4 0.5]]


#### `reciprocal()`
作用：返回参数逐个元素的倒数


```
import numpy as np

x = np.array([0.1, 0.5, 1, 5, 10])
print(f'x =\n{x}')
print(np.reciprocal(x))
print(1 / x)
```

    x =
    [ 0.1  0.5  1.   5.  10. ]
    [10.   2.   1.   0.2  0.1]
    [10.   2.   1.   0.2  0.1]


#### `power()`
作用：将第一个输入数组中的元素作为底数，计算它与第二个输入数组中的元素的幂。


```
import numpy as np

x = np.array([10, 10, 10])
print(f'x ={x}')
y = np.arange(6, dtype='i').reshape(2, 3)
print(f'y={y}')
print(np.power(x, y))
```

    x =[10 10 10]
    y=[[0 1 2]
     [3 4 5]]
    [[     1     10    100]
     [  1000  10000 100000]]


#### `mod()`, `remainder()`
作用：计算输入数组中相应元素相除后的余数
取模运算


```
import numpy as np

x = np.array([10, 10, 10])
print(f'x ={x}')
y = np.arange(6, dtype='i').reshape(2, 3) + 1
print(f'y={y}')

print(np.mod(x, y))
print(np.remainder(x, y))
```

    x =[10 10 10]
    y=[[1 2 3]
     [4 5 6]]
    [[0 0 1]
     [2 0 4]]
    [[0 0 1]
     [2 0 4]]


### 5.4 统计函数

#### `amax()`, `amin()`
作用：计算数组中的元素沿着指定轴的最大值、最小值
第二个参数`axis`：表示轴。0 列，1 行


```
import numpy as np

x = np.random.randint(1, 11, 6).reshape(2, 3)
print(f'x ={x}')

print(np.amax(x, axis=0))
print(np.amax(x, 1))

print(np.amin(x, 0))
print(np.amin(x, 1))
```

    x =[[ 8  9  9]
     [ 9 10 10]]
    [ 9 10 10]
    [ 9 10]
    [8 9 9]
    [8 9]


#### `ptp()`

作用：计算数组中元素最大值与最小值（最大值-最小值）。

参数：第二个参数表示轴，0 列，1 行，没有第二个参数时表示同时整个数组，即同时包含行与列。


```
import numpy as np

x = np.random.randint(1, 11, 6).reshape(2, 3)
print(f'x ={x}')
print(np.ptp(x))
# print(np.ptp(x, axis=0))
# print(np.ptp(x, axis=1))
print(np.ptp(x, 0))
print(np.ptp(x, 1))
```

    x =[[ 7 10  7]
     [ 1  1  4]]
    9
    [6 9 3]
    [3 3]


#### `percentile()`

原型：`numpy.percentile(a, p, axis)`

作用：百分位数是统计中使用的度量，表示小于这个值的观察值的百分比。

| 参数   | 说明                |
|------|-------------------|
| a    | 输入数组              |
| p    | 要计算的百分位数，在0~100之间 |
| axis | 沿着它计算百分位数的轴       |

说明：第p个百分位数是这样一个值，它使得至少有p%的数据项小于或等于这个值，且至少有（100-p）% 的数据项大于或等于这个值

例子：高等院校的入学考试成绩经常以百分位数的形式报告。比如，假设某个考生在入学考试中的语文部分的原始分数为54分。相对于参加同一考试的其他学生来说，他的成绩如何并不容易知道。但是如果原始分数54分恰好对应的是第70百分位数，我们就能知道大约70%的学生的考分比他低，而约30%的学生考分比他高。这里的P=70


```
import numpy as np

x = np.arange(6, dtype='f').reshape(2, 3) + 1
print(f'x ={x}')

print(np.percentile(x, 50))
print(np.percentile(x, 50, axis=0))
print(np.percentile(x, 50, 1))
```

    x =[[1. 2. 3.]
     [4. 5. 6.]]
    3.5
    [2.5 3.5 4.5]
    [2. 5.]


#### `median()`

作用：计算数组中元素的中位数。如果提供了轴，则沿着轴进行计算。


```
import numpy as np

x = np.random.randint(1, 11, 6).reshape(2, 3)
print(f'x ={x}')

print(np.median(x))
print(np.median(x, axis=0))
print(np.median(x, 1))
```

    x =[[ 1 10  3]
     [ 3  5  9]]
    4.0
    [2.  7.5 6. ]
    [3. 5.]


#### `mean()`

作用：计算数组中元素的算数平均值。如果提供了轴，则沿着轴进行计算。


```
import numpy as np

x = np.arange(1, 7).reshape(2, 3)
print(f'x ={x}')

print(np.mean(x))
print(np.mean(x, axis=0))
print(np.mean(x, 1))
```

    x =[[1 2 3]
     [4 5 6]]
    3.5
    [2.5 3.5 4.5]
    [2. 5.]



```
# 一维数组
import numpy as np

x = np.array([1, 2, 3, 4])
w = np.array([4, 3, 2, 1])

print(f'x = {x}')
print(f'w = {w}')
```

#### `average()`

作用：根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值，可以接受一个轴参数。如果没有指定轴，则数组会被展开。

- 加权平均值：将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数

  例如：考虑数组［1,2,3,4］和相应的权重［4,3.2,1］，通过将相应元素的乘积相加，并将和除以权重的和，来计算加权平均值。
  加权平均值=（14+23+32+41）/（4+3+2+1）

- 如果参数`returned`设为`true`，则返回值包含权重的和


```
# 一维数组
import numpy as np

x = np.array([1, 2, 3, 4])
w = np.array([4, 3, 2, 1])

print(f'x = {x}')
print(f'w = {w}')
print(np.average(x))
print(np.average(x, weights=w))
print(np.average(x, weights=w, returned=True))
```

    x = [1 2 3 4]
    w = [4 3 2 1]
    2.5
    2.0
    (2.0, 10.0)



```
# 多维数组
import numpy as np

x = np.arange(1, 7).reshape(2, 3)
w = np.array([1, 2, 3])
print(f'x = {x}')
print(f'w = {w}')
print(np.average(x, axis=1, weights=w))
print(np.dot(x[0, :], w) / np.sum(w), np.dot(x[1, :], w) / np.sum(w))
```

    x = [[1 2 3]
     [4 5 6]]
    w = [1 2 3]
    [2.33333333 5.33333333]
    2.3333333333333335 5.333333333333333


#### 标准差`std()`

标准差是一组数据平均值分散程度的一种度量

标准差是方养的算术平方根

公式: `std = sqrt (mean ((x - x.mean ()) **2))`

说明：如果数组是［1，2，3，4］，则其平均值为2.5。因此，差的平方是［2.25,0.25,0.25,2.25］，并且其平均值的平方根除以 4，即sqrt（5/4），结果为
1.1180339887498949



```
import numpy as np

x = np.array([1, 2, 3, 4])
print(np.std(x))
print(np.sqrt(np.mean((x - np.mean(x)) ** 2)))
```

    1.118033988749895
    1.118033988749895


#### 方差`var()`

统计中的方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数，即 mean（（×- x.mean（）** 2）。换句话说，标准差是方差的平方根




```
import numpy as np

x = np.array([1, 2, 3, 4])
print(np.var(x))
print(np.mean((x - np.mean(x)) ** 2))
```

    1.25
    1.25


### 5.5 排序函数

| 名称   | name        | 速度     | 最坏情况           | 工作空间           | 稳定性  |
|------|-------------|--------|----------------|----------------|------|
| 快速排序 | `quicksort` | 1      | $O(n^2)$       | 0              | 否    |
| 归并排序 | `mergesort` | 2      | $O(n*\log{n})$ | $-\frac{n}{2}$ | 是    |
| 堆排序  | `heapsort`  | 3      | $O(n*\log{n})$ | 0              | 否    |

#### `sort()`

原型：`sort(a, axis, kind, order)`

功能：返回输入数组的排序副本

- `a`：要排序的数组
- `axis`：沿着排序的轴，`axis=0`按列，`axis=1`按行。若没有则会展开，并沿着最后的轴排序
- `kind`：排序算法，默认为`quicksort`
- `order`：如果数组包含字段，则是要排序的字段



```
import numpy as np

x = np.random.randint(1, 11, 12).reshape(3, 4)
print(x)
print(np.sort(x))
# print(f'x = {x}')
print(np.sort(x, axis=0))
```

    [[ 2  7  4 10]
     [ 7  9  6  2]
     [ 2  2  7  3]]
    [[ 2  4  7 10]
     [ 2  6  7  9]
     [ 2  2  3  7]]
    [[ 2  2  4  2]
     [ 2  7  6  3]
     [ 7  9  7 10]]



```
import numpy as np

dt = np.dtype([('name', 'S10'), ('age', int)])
y = np.array([('sunwukong', 600), ('shahesheng', 100), ('zhubajie', 300), ('tangseng', 1000)], dtype=dt)
print(y)
print(np.sort(y, order='age'))
```

    [(b'sunwukong',  600) (b'shahesheng',  100) (b'zhubajie',  300)
     (b'tangseng', 1000)]
    [(b'shahesheng',  100) (b'zhubajie',  300) (b'sunwukong',  600)
     (b'tangseng', 1000)]


#### `argsort()`

作用：对输入数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。这个索引数组用于构造排序后的数组。


```
import numpy as np

x = np.array([3, 8, 6])
print(x)
index_x = np.argsort(x)
print(index_x)
print(x[index_x])
print([x[idx] for idx in index_x])
```

    [3 8 6]
    [0 2 1]
    [3 6 8]
    [3, 6, 8]



```
import numpy as np

a = [1, 5, 1, 4, 3, 4, 4]
b = [9, 4, 0, 4, 0, 2, 1]

print([(i, a[i], b[i]) for i in np.argsort(a)])
clist = [i for i in zip(a, b)]
print(clist)
c = np.array(clist, dtype=np.dtype([('x', int), ('y', int)]))
print(c)
print(np.argsort(c))
print(np.argsort(c, order=('x', 'y')))
```

    [(0, 1, 9), (2, 1, 0), (4, 3, 0), (3, 4, 4), (5, 4, 2), (6, 4, 1), (1, 5, 4)]
    [(1, 9), (5, 4), (1, 0), (4, 4), (3, 0), (4, 2), (4, 1)]
    [(1, 9) (5, 4) (1, 0) (4, 4) (3, 0) (4, 2) (4, 1)]
    [2 0 4 6 5 3 1]
    [2 0 4 6 5 3 1]


#### `lexsort()`

作用：使用键序列执行间接排序。键可以看作是电子表格中的一列。该函数返回一个索引数组，使用它可以获得排序数据。

注意：最后一个键恰好是 sort 的主键

- 多级排序，以最后一列为主，剩余的也是以剩余的最后一列为主
- 多级排序是指对一个数组或矩阵进行多次排序操作，每次排序操作都依据不同的排序key进行排序。在numpy中可以使用多个key来实现多级排序。
- numpy中的lexsort()函数用于将指定多个数组的元素根据指定排序key进行排序并返回排序后的索引值。其中lex的含义是lexical sort(字典排序)。
- 当输入一个矩阵时，默认排序最后一行的数据，前面的行都是辅助行。

参考：https://blog.csdn.net/Flag_ing/article/details/124185378


```
import numpy as np

name = ['tangseng', 'sunwukong', 'zhubajie', 'shawujing']
scores_maths = [10, 9, 9, 9]
scores_english = [10, 9, 9, 8]
scores_chinese = [10, 8, 9, 9]
indices = np.lexsort((scores_chinese, scores_english, scores_maths))
print(indices)
# indices = indices[::-1]
# print(indices)
for idx in indices:
    print(name[idx], scores_maths[idx], scores_english[idx], scores_chinese[idx])
```

    [3 1 2 0]
    shawujing 9 8 9
    sunwukong 9 9 8
    zhubajie 9 9 9
    tangseng 10 10 10



```
import numpy as np

a = [5, 3, 6]
b = [5, 3, 3]
print(f'a = {a}')
print(f'b = {b}')
idx = np.lexsort((a, b))
print(idx)
print([f'{a[i]}-{b[i]}' for i in idx])

c = np.asarray([a, b])
print(f'c = {c}')
idy = np.lexsort(c)
print(idy)
# print(c[0, :], c[1, :])

np.testing.assert_equal(idx, idy)
```

    a = [5, 3, 6]
    b = [5, 3, 3]
    [1 2 0]
    ['3-3', '6-3', '5-5']
    c = [[5 3 6]
     [5 3 3]]
    [1 2 0]



```
import numpy as np

a = np.array([[3, 3, 5],
              [3, 6, 9],
              [6, 8, 5]])
print('*' * 10, 'a')
print(a)
print(np.lexsort(a))
# print(np.lexsort(a, axis=0))
# print(np.lexsort((a[:, 0], a[:, 1], a[:, 2])))
print(np.lexsort((a[0, :], a[1, :], a[2, :])))

b = np.array([[3, 3, 8],
              [6, 9, 7],
              [3, 3, 5]])
print('*' * 10, 'b')
print(b)
print(np.lexsort(b))
# print(np.lexsort(b, axis=0))
print(np.lexsort((b[0, :], b[1, :], b[2, :])))
```

    ********** a
    [[3 3 5]
     [3 6 9]
     [6 8 5]]
    [2 0 1]
    [2 0 1]
    ********** b
    [[3 3 8]
     [6 9 7]
     [3 3 5]]
    [0 1 2]
    [0 1 2]



```
import numpy as np

c = np.array([[3, 3, 8],
              [6, 9, 7],
              [3, 3, 5]])

print(c)
ind_1 = np.lexsort(c)
ind_2 = np.lexsort((c[0, :], c[1, :], c[2, :]))
print(ind_1)
print(ind_2)
np.testing.assert_equal(ind_1, ind_2)
```

    [[3 3 8]
     [6 9 7]
     [3 3 5]]
    [0 1 2]
    [0 1 2]


#### `msort(a)`

已经删除

作用：数组按第一个轴排序，返回排序后的数组副本

说明：np.msort（a） 相等于 np.sort（a, axis=0）

numpy 1.24.0 Deprecated

The numpy.msort function is deprecated. Use np.sort(a, axis=0) instead. 参考 https://github.com/numpy/numpy/pull/22456

numpy 1.24.3 Removed

TYP: Remove some stray type-check-only imports of msort 参考 https://github.com/numpy/numpy/pull/23345

#### `sort_complex(a)`

作用：对复数按照先实部后虚部的顺序进行排序。


```
import numpy as np

real_part = [3, 3, 6, 8, 6, 8]
imag_part = [3, 1, 8, 6, 5, 9]
c = [rp + ip * 1j for rp, ip in zip(real_part, imag_part)]
c_sort = np.sort_complex(c)

print(real_part)
print(imag_part)
print(c)
print(c_sort.tolist())
print(c[0].real, c[0].imag)
```

    [3, 3, 6, 8, 6, 8]
    [3, 1, 8, 6, 5, 9]
    [(3+3j), (3+1j), (6+8j), (8+6j), (6+5j), (8+9j)]
    [(3+1j), (3+3j), (6+5j), (6+8j), (8+6j), (8+9j)]
    3.0 3.0


#### `partition(a, kth[, axis, kind, order])`

指定一个数，对数组进行分区


```
import numpy as np

a = np.array([5, 3, 1, 4, 8, 2, 7, 6, 9])

# 将数组 a 中所有元素（包括重复元素）从小到大排列，3 表示的是排序数组索引为 3 的数字，比该数字小的排在该数字前面，比该数字大的排在该数字的后面
ap1 = np.partition(a, 3)
ap2 = np.partition(a, (3, 6))

print(a)
print(ap1)
print(ap2)
```

    [5 3 1 4 8 2 7 6 9]
    [1 2 3 4 5 6 7 8 9]
    [1 2 3 4 5 6 7 8 9]


#### argpartition(a, kth[, axis, kind, order])

可以通过关键字 kind 指定算法沿着指定轴对数组进行分区


```
import numpy as np

arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])
print(arr)
print(np.sort(arr))
isort = np.argpartition(arr, 2)
print(isort)
print(arr[isort])
isort = np.argpartition(arr, -2)
print(isort)
print(arr[isort])
```

    [ 46  57  23  39   1  10   0 120]
    [  0   1  10  23  39  46  57 120]
    [6 4 5 2 3 0 1 7]
    [  0   1  10  23  39  46  57 120]
    [6 4 5 2 3 0 1 7]
    [  0   1  10  23  39  46  57 120]



```

```

### 5.6 搜索函数

#### max(), min()

沿指定轴返回最大值或最小值。


```
import numpy as np

x = np.array([30, 10, 15, 13, 38, 80])
print(x)
print(np.max(x), np.min(x))
```

    [30 10 15 13 38 80]
    80 10



```
import numpy as np

x = np.array([30, 10, 15, 13, 38, 80])
x = x.reshape(2, 3)
print(x)
print(np.max(x), np.min(x))
print(np.max(x, axis=0), np.max(x, axis=1))
print(np.min(x, axis=0), np.min(x, axis=1))
```

    [[30 10 15]
     [13 38 80]]
    80 10
    [30 38 80] [30 80]
    [13 10 15] [10 13]


#### argmax(), argmin()

沿给定轴返回最大和最小元素的索引


```
import numpy as np

x = np.array([30, 10, 15, 13, 38, 80])
x = x.reshape(2, 3)
print(x)
print(np.argmax(x), np.argmin(x))
print(np.argmax(x, axis=0), np.argmax(x, axis=1))
print(np.argmin(x, axis=0), np.argmin(x, axis=1))
```

    [[30 10 15]
     [13 38 80]]
    5 1
    [0 1 1] [0 2]
    [1 0 0] [1 0]


#### nonzero()

函数返回输入数组中非零元素的索引


```
import numpy as np

x = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
print(x)
idxs = np.nonzero(x)
print(idxs)
idxs_x = idxs[0]
idxs_y = idxs[1]

print(x[idxs_x[1]][idxs_y[1]])
```

    [[30 40  0]
     [ 0 20 10]
     [50  0 60]]
    (array([0, 0, 1, 1, 2, 2]), array([0, 1, 1, 2, 0, 2]))
    40


#### where()

返回输入数组中满足给定条件的元素的索引


```
import numpy as np

x = np.arange(9.).reshape(3, 3)
print('我们的数组是：')
print(x)
print('大于 3 的元素的索引：')
y = np.where(x > 3)
print(y)
print('使用这些索引来获取满足条件的元素：')
print(x[y])
```

    我们的数组是：
    [[0. 1. 2.]
     [3. 4. 5.]
     [6. 7. 8.]]
    大于 3 的元素的索引：
    (array([1, 1, 2, 2, 2]), array([1, 2, 0, 1, 2]))
    使用这些索引来获取满足条件的元素：
    [4. 5. 6. 7. 8.]


#### extract()

根据某个条件从数组中抽取元素，返回满条件的元素


```
import numpy as np

x = np.arange(9.).reshape(3, 3)
print('我们的数组是：')
print(x)
# 定义条件, 选择偶数元素
condition = np.mod(x, 2) == 0
print('按元素的条件值：')
print(condition)
print('使用条件提取元素：')
print(np.extract(condition, x))
```

    我们的数组是：
    [[0. 1. 2.]
     [3. 4. 5.]
     [6. 7. 8.]]
    按元素的条件值：
    [[ True False  True]
     [False  True False]
     [ True False  True]]
    使用条件提取元素：
    [0. 2. 4. 6. 8.]

