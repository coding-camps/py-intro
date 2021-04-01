# NumPy教程

## 一、初识NumPy

### 1.1 NumPy简介

- 官网 https://numpy.org/
- 参考 numpy ： https://zhuanlan.zhihu.com/p/342141335
- 参考教程1：https://www.runoob.com/numpy/numpy-tutorial.html
- 参考教程2：https://geek-docs.com/numpy/numpy-top-tutorials/1000100_numpy_index.html


```python
import numpy as np

print(np.__version__)
print(np.version)
print(np.version.version)
print(np.version.full_version)
```

    1.26.4
    <module 'numpy.version' from '/Users/cosmos/WorkSpace/_configs/py-envs/py312-all/lib/python3.12/site-packages/numpy/version.py'>
    1.26.4
    1.26.4


### 1.2 ndarray对象简介

#### 简介
- 下标从0开始
- 是同类型元素的数组
- 每个元素都有相同的大小

#### 属性
- `dtype` 元素数据类型
- `shape` 形状，一个元组
- `stride` 跨度元组，从当前维度前进到下一元素需要跨过的字节数

## 二、数组的基本使用

### 2.1 numpy数据类型



#### 数据类型
dtype类型的实例
- bool_
- int_ 默认的整数类型
- intc
- intp
- int8
- int16
- int32
- int64
- uint8
- uint16
- uint32
- uint64
- float_
- float16
- float32
- float64
- complex_
- complex64
- complex128
每个内建类型都有唯一定义它的字符代码
- b
- i
- u
- f
- c
- m
- M
- O
- S,a
- U
- V

#### 数据类型 dtype
原型：`nump.dtype(object, align, copy)`


```python
import numpy as np

dt1 = np.dtype(np.int32)
dt2 = np.dtype('i4')
dt3 = np.dtype('<i4')

print('dt1 - ', dt1, type(dt1))
print('dt2 - ', dt2, type(dt2))
print('dt3 - ', dt3, type(dt3))

# 结构化数据类型
stu = np.dtype([('name', 'S20'), ('age', 'i4'), ('marks', 'f4')])
print('stu - ', stu, type(stu))
```

    dt1 -  int32 <class 'numpy.dtypes.Int32DType'>
    dt2 -  int32 <class 'numpy.dtypes.Int32DType'>
    dt3 -  int32 <class 'numpy.dtypes.Int32DType'>
    stu -  [('name', 'S20'), ('age', '<i4'), ('marks', '<f4')] <class 'numpy.dtypes.VoidDType'>



### 2.2 创建数组对象 ndarray


原型：`numpy.array(object, dtype=None, copy=True, order=None, subook=False, ndmin=0)`
原型：`numpy.asarray(a, dtype=None, order=None)`


```python
import numpy as np

# 一维数组
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3.6, 4, 5])
print(type(arr1), arr1.shape, arr1.dtype, arr1)
print(type(arr2), arr2.shape, arr2.dtype, arr2)

# 多维数组
arr1 = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
arr2 = np.array([1, 2, 3, 4, 5, 6], ndmin=2)
print(type(arr1), arr1.shape, arr1.dtype, arr1)
print(type(arr2), arr2.shape, arr2.dtype, arr2)

# 结构化数据类型
stu = np.dtype([('name', 'S20'), ('age', 'i4'), ('marks', 'f4')])
print('stu - ', stu, type(stu))

stu_arr = np.array([('Jim', 10, 99.9), ('Joy', 90, 98.9)], dtype=stu)
print('students -', type(stu_arr), stu_arr.shape, stu_arr.dtype, stu_arr)
```

    <class 'numpy.ndarray'> (5,) int64 [1 2 3 4 5]
    <class 'numpy.ndarray'> (5,) float64 [1.  2.  3.6 4.  5. ]
    <class 'numpy.ndarray'> (2, 3) float32 [[1. 2. 3.]
     [4. 5. 6.]]
    <class 'numpy.ndarray'> (1, 6) int64 [[1 2 3 4 5 6]]
    stu -  [('name', 'S20'), ('age', '<i4'), ('marks', '<f4')] <class 'numpy.dtypes.VoidDType'>
    students - <class 'numpy.ndarray'> (2,) [('name', 'S20'), ('age', '<i4'), ('marks', '<f4')] [(b'Jim', 10, 99.9) (b'Joy', 90, 98.9)]



```python
import numpy as np

arr1 = np.asarray([1, 2, 3, 4, 5])
arr2 = np.asarray((1, 2, 3, 4, 5))
arr3 = np.asarray([(1, 2, 3), (4, 5)], dtype=object)

print(type(arr1), arr1.shape, arr1.dtype, arr1)
print(type(arr2), arr2.shape, arr2.dtype, arr2)
print(type(arr3), arr3.shape, arr3.dtype, arr3)
# arr3问题：https://blog.csdn.net/m0_53127772/article/details/132492224
# https://geek-docs.com/numpy/numpy-tutorials/how-to-fix-valueerror-setting-an-array-element-with-a-sequence.html
```

    <class 'numpy.ndarray'> (5,) int64 [1 2 3 4 5]
    <class 'numpy.ndarray'> (5,) int64 [1 2 3 4 5]
    <class 'numpy.ndarray'> (2,) object [(1, 2, 3) (4, 5)]


#### 特殊函数类型1
未初始化数组：`numpy.empty(shape, dtype=None, order=None)`  
以0填充数组：`numpy.zeros(shape, dtype=None, order=None)`  
以1填充数组：`numpy.ones(shape, dtype=None, order=None)`  
以指定元素填充数组：`numpy.full(shape, fill_value, dtype=None, order=None)`  
对角线元素为1其他元素为0的数组（类似单位矩阵）：`numpy.eye(N, M=None, k=0, dtype=float, order=None)`  
某个范围内的列表数组(左闭右开)：`numpy.arange([start,] stop[, step,], dtype=None)`



```python
# 未初始化数组
arr1 = np.empty([2, 3], dtype=np.intp)

print(arr1, type(arr1), arr1.shape, arr1.dtype)

# 以0填充数
arr2 = np.zeros([2, 3], dtype=np.intp)
arr3 = np.zeros([2, 3], dtype=[('x', 'i4'), ('y', 'f')])  # 使用了结构化类型

print(arr2, type(arr2), arr2.shape, arr2.dtype)
print(arr3, type(arr3), arr3.shape, arr3.dtype)

# 以 1 填充
arr2 = np.ones([2, 3], dtype=np.intp)
arr3 = np.ones([2, 3], dtype=[('x', 'i4'), ('y', 'f')])  # 使用了结构化类型

print(arr2, type(arr2), arr2.shape, arr2.dtype)
print(arr3, type(arr3), arr3.shape, arr3.dtype)

# 以指定元素填充数组
arr1 = np.full([2, 3], 1024)
print(arr1, type(arr1), arr1.shape, arr1.dtype)

# 对角线元素为1其他元素为0的数组（类似单位矩阵）
arr1 = np.eye(3, dtype=int)
arr2 = np.eye(3, 5, dtype=np.uint8)

print(arr1, type(arr1), arr1.shape, arr1.dtype)
print(arr2, type(arr2), arr2.shape, arr2.dtype)

# 某个范围内的列表数组(左闭右开)
arr1 = np.arange(10)
arr2 = np.arange(10, 20)
arr3 = np.arange(10, 20, 2)
arr4 = np.arange(10, 20, 2, 'f4')
print(arr1, type(arr1), arr1.shape, arr1.dtype)
print(arr2, type(arr2), arr2.shape, arr2.dtype)
print(arr3, type(arr3), arr3.shape, arr3.dtype)
print(arr4, type(arr4), arr4.shape, arr4.dtype)
```

    [[1 2 3]
     [4 5 6]] <class 'numpy.ndarray'> (2, 3) int64
    [[0 0 0]
     [0 0 0]] <class 'numpy.ndarray'> (2, 3) int64
    [[(0, 0.) (0, 0.) (0, 0.)]
     [(0, 0.) (0, 0.) (0, 0.)]] <class 'numpy.ndarray'> (2, 3) [('x', '<i4'), ('y', '<f4')]
    [[1 1 1]
     [1 1 1]] <class 'numpy.ndarray'> (2, 3) int64
    [[(1, 1.) (1, 1.) (1, 1.)]
     [(1, 1.) (1, 1.) (1, 1.)]] <class 'numpy.ndarray'> (2, 3) [('x', '<i4'), ('y', '<f4')]
    [[1024 1024 1024]
     [1024 1024 1024]] <class 'numpy.ndarray'> (2, 3) int64
    [[1 0 0]
     [0 1 0]
     [0 0 1]] <class 'numpy.ndarray'> (3, 3) int64
    [[1 0 0 0 0]
     [0 1 0 0 0]
     [0 0 1 0 0]] <class 'numpy.ndarray'> (3, 5) uint8
    [0 1 2 3 4 5 6 7 8 9] <class 'numpy.ndarray'> (10,) int64
    [10 11 12 13 14 15 16 17 18 19] <class 'numpy.ndarray'> (10,) int64
    [10 12 14 16 18] <class 'numpy.ndarray'> (5,) int64
    [10. 12. 14. 16. 18.] <class 'numpy.ndarray'> (5,) float32


#### 特殊函数类型2
以流形式创建动态数组：`numpy.frombuffer(buffer, dtype=float, count=-1, offset=0)`

> buffer是字符串的时候，python3默认str是Unicode类型，所以要转成bytesstring在原str前加上b。

以可迭代对象创建动态数组：`numpy.fromiter(iterable, dtype, count=-1)`

等差数列的一维数组：`numpy.linspace(start, stop, num=50, endpoint=True, restep=False, dtype=None)`

等比数列的一维数组：`numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)`


```python
import numpy as np

# 以流形式创建动态数组
arr1 = np.frombuffer(b"Hello world~!", dtype='S1', count=5, offset=2)
arr2 = np.frombuffer(b'ABCDEF', dtype='S3')
arr3 = np.frombuffer(b'123456789', dtype=np.uint8)

print(arr1, type(arr1), arr1.shape, arr1.dtype)
print(arr2, type(arr2), arr2.shape, arr2.dtype)
print(arr3, type(arr3), arr3.shape, arr3.dtype)

# 以可迭代对象创建动态数组
arr1 = np.fromiter(iter([1, 2, 3, 4, 5, 6]), dtype=np.float32)
arr2 = np.fromiter(iter([1, 2, 3, 4, 5, 6]), dtype=np.int8)
print(arr1, type(arr1), arr1.shape, arr1.dtype)
print(arr2, type(arr2), arr2.shape, arr2.dtype)

# 等差数列的一维数组

arr1 = np.linspace(1, 10, 10, dtype=np.uint8)
arr2 = np.linspace(1, 10, 20, dtype=np.float32)
print(arr1, type(arr1), arr1.shape, arr1.dtype)
print(arr2, type(arr2), arr2.shape, arr2.dtype)

# 等比数列的一维数组
arr1 = np.logspace(1, 10, 10, dtype='i4', base=2)
print(arr1, type(arr1), arr1.shape, arr1.dtype)
```

    [b'l' b'l' b'o' b' ' b'w'] <class 'numpy.ndarray'> (5,) |S1
    [b'ABC' b'DEF'] <class 'numpy.ndarray'> (2,) |S3
    [49 50 51 52 53 54 55 56 57] <class 'numpy.ndarray'> (9,) uint8
    [1. 2. 3. 4. 5. 6.] <class 'numpy.ndarray'> (6,) float32
    [1 2 3 4 5 6] <class 'numpy.ndarray'> (6,) int8
    [ 1  2  3  4  5  6  7  8  9 10] <class 'numpy.ndarray'> (10,) uint8
    [ 1.         1.4736842  1.9473684  2.4210527  2.8947368  3.368421
      3.8421052  4.3157897  4.7894735  5.263158   5.736842   6.2105265
      6.6842103  7.1578946  7.631579   8.105263   8.578947   9.052631
      9.526316  10.       ] <class 'numpy.ndarray'> (20,) float32
    [   2    4    8   16   32   64  128  256  512 1024] <class 'numpy.ndarray'> (10,) int32


#### 随机数
生成[0,1)之间的随机数：`numpy.random.rand(d0, d1, ..., dn)`
生成[0,1)之间的随机数：`numpy.random.random(size=None)`
生成随机整数：`numpy.random.randint(low, high=None, size=None, dtype=None)`
返回标准正态分布N(0,1)的一个或一组样本：`numpy.random.randn(d0, d1, ..., dn)`
生成高斯分布的概率密度随机数：`numpy.random.normal(loc=0.0, scale=1.0, size=None)`


```python
import numpy as np

# 生成0到1之间的随机数
print(np.random.rand())
# 生成0到1之间的随机数，有3个元素的一维数组
print(np.random.rand(3))
# 生成0到1之间的随机数，二维数组
print(np.random.rand(3, 2))
# 生成0到1之间的随机数，多维数组
print(np.random.rand(2, 3, 4))

# 生成[0,1)之间的随机数
print(np.random.random())
print(np.random.random(5))
```

    0.4467061619964898
    [7.93744669e-01 7.23233300e-01 1.06325496e-04]
    [[0.56373954 0.82853137]
     [0.00237099 0.31578816]
     [0.71153581 0.32637162]]
    [[[0.42255226 0.4188268  0.86855082 0.10833073]
      [0.57361827 0.60220959 0.07127345 0.30465275]
      [0.4713651  0.42877537 0.76396001 0.23942578]]
    
     [[0.59326935 0.21598771 0.32855583 0.06827275]
      [0.72565378 0.61223991 0.11700494 0.6873665 ]
      [0.14501862 0.96252832 0.77727822 0.90335003]]]
    0.7843792250906823
    [0.50868687 0.13197066 0.22981003 0.61674587 0.76894367]



```python
# 生成随机整数
print(np.random.randint(10))
print(np.random.randint(0, 10, 5))
```

    8
    [8 8 0 6 1]



```python
# 返回标准正态分布N(0,1)的一个或一组样本
print(np.random.randn())
print(np.random.randn(2))
print(np.random.randn(2, 3))
```

    0.8810603641789418
    [ 0.35262675 -1.10266781]
    [[ 0.29848657 -0.38834993  0.36441861]
     [-1.02179129  0.50777643  1.83670195]]



```python
# 生成高斯分布的概率密度随机数
print(np.random.normal())
print(np.random.normal(loc=1, scale=2, size=5))
```

    -1.1460308867811968
    [0.88005893 2.6173731  2.19524246 2.84205078 3.4007643 ]


### 2.3 numpy数组与python列表的对比


```python
import random
import time
import numpy as np

li = []
for i in range(1000_0000):
    li.append(random.random())

# python版本随机数求和
t1 = time.time()
ret = sum(li)
t2 = time.time()
print(f'耗时：{t2 - t1}')
print(ret)

# numpy版本随机数求和
lix = np.array(li)
t1 = time.time()
retx = np.sum(lix)
t2 = time.time()
print(f'耗时：{t2 - t1}')
print(retx)
```

    耗时：0.1020209789276123
    5000740.93584
    耗时：0.008448123931884766
    5000740.93583952


### 2.4 ndarray数组属性

维数称为秩(rank)
轴（axis），维度（dimensions）
- ndim 秩，即轴的数量或维度的数量
- shape 维度
- size 元素总数
- dtype 元素的类型
- itemsize 每个元素的大小，以字节为单位
- flags 内存信息
- real 实部
- image 虚部
- data 实际数组的缓冲区



```python
# dim, shape
arr = np.arange(24)
print(arr, arr.ndim, arr.shape)
arrx = arr.reshape(2, 3, 4)
print(arrx, arrx.ndim, arrx.shape)
# size, dtype, itemsize
print(arrx.size, arrx.dtype, arrx.itemsize)
print(np.array([1, 2, 3], dtype='i1').itemsize)
```

    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23] 1 (24,)
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
    
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]] 3 (2, 3, 4)
    24 int64 8
    1



```python
# flags
'''
  C_CONTIGUOUS : 数据在一个单一的C风格的连续段中
  F_CONTIGUOUS : 数据在一个单一的Fortran风格的连续段中
  OWNDATA : 数据拥有它所使用的内存或从另一个对象中借用它
  WRITEABLE : 数据区域可以被写入，该值设制为False，则数据为只读
  ALIGNED : 数据和所有元素都适当地对齐到硬件上
  WRITEBACKIFCOPY : 是其他数组的副本，释放时原数组的内容将被更新
'''
arr = np.array([1, 2, 3], dtype='i1')
print(arr.flags)

# real
# image
# data
```

      C_CONTIGUOUS : True
      F_CONTIGUOUS : True
      OWNDATA : True
      WRITEABLE : True
      ALIGNED : True
      WRITEBACKIFCOPY : False


## 三、元素操作

### 3.1 切片和索引


```python
import numpy as np

arr = np.arange(10)
print(arr)
print(arr[1])
```

    [0 1 2 3 4 5 6 7 8 9]
    1



```python
s = slice(2, 7, 2)
print(arr[s])
print(arr[2:7:2])  # start : stop : step
print(arr[2:])
print(arr[2:7])
```

    [2 4 6]
    [2 4 6]
    [2 3 4 5 6 7 8 9]
    [2 3 4 5 6]


#### 冒号“:”的解释
- [index] 如果只放置一个参数，将返回与该索引相对应的单个元素。
- [start:] 表示从该索引开始以后的所有项都被提取
- [start: stop:] 表示从start（包含）到stop（不包含）的左闭右开区间内的索引对应的项目
- 多维数组同样适用上述方法


```python
import numpy as np

arr = np.arange(15)
arr.shape = (5, 3)
print(arr)
```

    [[ 0  1  2]
     [ 3  4  5]
     [ 6  7  8]
     [ 9 10 11]
     [12 13 14]]



```python
print(arr[2], type(arr[2]))
print(arr[2][1], type(arr[2][1]))
```

    [6 7 8] <class 'numpy.ndarray'>
    7 <class 'numpy.int64'>



```python
print(arr[2:])
print(arr[:2])
```

    [[ 6  7  8]
     [ 9 10 11]
     [12 13 14]]
    [[0 1 2]
     [3 4 5]]


切片还可以包含省略号“...”，来使选择元组的长度和数组的维度相同。如果在行位置使用省略号，它将返回包含行中元素的ndarray


```python
arr = np.arange(1, 16)
arr.shape = (5, 3)
print(arr)
```

    [[ 1  2  3]
     [ 4  5  6]
     [ 7  8  9]
     [10 11 12]
     [13 14 15]]



```python
# 第2列元素
print(arr[..., 1])
# 第2列及剩下的所有元素
print(arr[..., 1:])
```

    [ 2  5  8 11 14]
    [[ 2  3]
     [ 5  6]
     [ 8  9]
     [11 12]
     [14 15]]



```python
# 第2行元素
print(arr[1, ...])
# 第2行及剩下的所有元素
print(arr[1:, ...])
```

    [4 5 6]
    [[ 4  5  6]
     [ 7  8  9]
     [10 11 12]
     [13 14 15]]


### 3.2 高级索引

#### 整数数组索引

- 获取数组(0,0), (1,1), (2,1)位置处的索引




```python
import numpy as np

arr = np.arange(1, 10).reshape(3, 3)
print(arr)
print(arr[[0, 1, 2], [0, 1, 0]])
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [1 5 7]


- 行索引是[0,0]和[3,3]，列索引是[0,2]和[0,2]


```python
import numpy as np

arr = np.arange(1, 10).reshape(3, 3)
print(arr)

rows = np.array([[0, 0], [2, 2]])
cols = np.array([[0, 2], [0, 2]])
print(arr[rows, cols])
print(arr[np.array([0, 0, 2, 2]), np.array([0, 2, 0, 2])])
print(arr[np.array([[0], [0], [2], [2]]), np.array([[0], [2], [0], [2]])])
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [[1 3]
     [7 9]]
    [1 3 7 9]
    [[1]
     [3]
     [7]
     [9]]


- 借助切片（:）或(...)与索引数组组合


```python
import numpy as np

arr = np.arange(1, 26).reshape(5, 5)
print(arr)
print(arr[1:3, 1:3])
print(arr[1:3, [1, 2]])
print(arr[..., 1:3])
```

    [[ 1  2  3  4  5]
     [ 6  7  8  9 10]
     [11 12 13 14 15]
     [16 17 18 19 20]
     [21 22 23 24 25]]
    [[ 7  8]
     [12 13]]
    [[ 7  8]
     [12 13]]
    [[ 2  3]
     [ 7  8]
     [12 13]
     [17 18]
     [22 23]]



#### 布尔索引

- 布尔索引通过布尔运算（比如：比较运算符）来获取符合指定条件的元素的数组


```python
# 大于5的元素
import numpy as np

arr = np.arange(1, 10).reshape(3, 3)
print(arr)
print(arr[arr > 5])
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [6 7 8 9]



```python
# 使用 ~ (取补运算符)来过滤NaN
import numpy as np

arr = np.array([np.nan, 1, 2, 3, np.nan, 5])
print(arr)
print(arr[~np.isnan(arr)])
```

    [nan  1.  2.  3. nan  5.]
    [1. 2. 3. 5.]


### 3.3 广播

是numpy对不同形状（shape）的数组进行数值计算的方式，对数组的算术运算通常在相应的元素上进行。

如果两个数组`a`与`b`形状相同，即`a.shape==b.shape`那么`a+b`的结果就是`a`与`b`对应位置相加。要求维数相同，且各维度的长度相同。
如果两个数组的维数不同，则一般元素到元素的操作是不可能的。然而，Numpy中仍然可以对形状不相似的数组进行操作，因为它具备广播功能。
广播功能使得较小的数组会广播到较大数组的大小，以便使得它们的形状可兼容。

**广播规则**：
- 让所有输入数组向其中形状最长的数组看齐，形状中不足的部分都通过在前面加1补齐。
- 输出数组的形状是输入数组形状的各个维度上的最大值。
- 如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为1时，这个数组能够进行计算，否则出错。
- 当输入数组的某个维度的长度为1时，沿着此维度运算时都用此维度上的第一组值。

**简单理解**：
对两个数组，分别比较它们的每个维度，若其中一个数组没有当前维度则忽略，满足
- 数组形状相同
- 当前维度的值相同
- 当前维度的值有一个是1
若条件不满足，则抛出异常“ValueError: frames are not aligned”

##### General Broadcasting Rules

When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing (i.e. rightmost) dimension and works its way left. Two dimensions are compatible when
当对两个数组进行操作时，NumPy会按元素比较它们的形状。它从尾部（即最右侧）尺寸开始，然后向左移动。当

- they are equal, or
- 它们是相等的，或者

- one of them is 1.
- 其中一个是1。

If these conditions are not met, a ValueError: operands could not be broadcast together exception is thrown, indicating that the arrays have incompatible shapes.
如果不满足这些条件，将引发ValueError: operands could not be broadcast together (ValueError:操作数不能一起广播异常)，表明数组具有不兼容的形状。

Input arrays do not need to have the same number of dimensions. The resulting array will have the same number of dimensions as the input array with the greatest number of dimensions, where the size of each dimension is the largest size of the corresponding dimension among the input arrays. Note that missing dimensions are assumed to have size one.
输入数组不需要具有相同数量的维度。得到的数组将具有与具有最大维度数的输入数组相同的维度数，其中每个维度的大小是输入数组中对应维度的最大大小。请注意，缺失的尺寸假定为1号。


```python
# 形状相同
import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
c = a + b
print(c)
```

    [11 22 33]



```python
# 形状不同
import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b1 = np.array([10, ])
b2 = np.array([10, 20, 30])
b3 = np.array([10, 20, 30]).reshape(3, 1)
print('a =\n', a)
print('b1 =\n', b1)
print('b2 =\n', b2)
print('b3 =\n', b3)
print('-')
print('a+b1 = \n', a + b1)
print('a+b2 =\n', a + b2)
print('a+b3 =\n', a + b3)
```

    a =
     [[1 2 3]
     [4 5 6]
     [7 8 9]]
    b1 =
     [10]
    b2 =
     [10 20 30]
    b3 =
     [[10]
     [20]
     [30]]
    -
    a+b1 = 
     [[11 12 13]
     [14 15 16]
     [17 18 19]]
    a+b2 =
     [[11 22 33]
     [14 25 36]
     [17 28 39]]
    a+b3 =
     [[11 12 13]
     [24 25 26]
     [37 38 39]]



```python
# 案例解释
import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b2 = np.array([10, 20, 30])
bb2 = np.tile(b2, (3, 1))
print('a =\n', a)
print('b2 =\n', b2)
print('bb2 =\n', bb2)
print("a + bb2 =\n", a + bb2)
```

    a =
     [[1 2 3]
     [4 5 6]
     [7 8 9]]
    b2 =
     [10 20 30]
    bb2 =
     [[10 20 30]
     [10 20 30]
     [10 20 30]]
    a + bb2 =
     [[11 22 33]
     [14 25 36]
     [17 28 39]]


### 3.4 迭代

#### numpy.nditer基本使用

它是一个有效的多维迭代器对象，可以用在数组上进行迭代。数组的每个元素可使用 Python的标准Iterator接口来访问。

不是使用标准C或Fortran顺序，选择的顺序是和数组内存是一致的，这样做是为了提升访问的效率，默认是行序优先（row-major order，或者说是 C-order）

反映了默认情况下只需访问每个元素，而无需考虑特定顺序。

可以通过迭代上述数组的转置来看这一点，并与以C顺序访问的数组转置的copy方式做对比。

`a`和`a.T`的遍历顺序是一样的，也就是它们在内存中的存储顺序也是一样的，但`a.T.copy(order='c')`的遍历结果是不同的，那是因为它和前两种的存储方式是不一样的，默认是按行访问。


```python
import numpy as np

a = np.arange(6)
print('a =\n', a)

b = a.reshape(2, 3)
print('b =\n', b)
for x in np.nditer(b):
    print(x, end=',')
print()

c = b.T
print('c =\n', c)
for x in np.nditer(c):
    print(x, end=',')
print()

d = b.T.copy(order='C')
print('d =\n', d)
for x in np.nditer(d):
    print(x, end=',')
print()

e = np.array([[0, 3], [1, 4], [2, 5]])

print('e =\n', e)
for x in np.nditer(e):
    print(x, end=',')
print()

f = b.T.copy()
print('f =\n', f)
for x in np.nditer(f):
    print(x, end=',')
print()
```

    a =
     [0 1 2 3 4 5]
    b =
     [[0 1 2]
     [3 4 5]]
    0,1,2,3,4,5,
    c =
     [[0 3]
     [1 4]
     [2 5]]
    0,1,2,3,4,5,
    d =
     [[0 3]
     [1 4]
     [2 5]]
    0,3,1,4,2,5,
    e =
     [[0 3]
     [1 4]
     [2 5]]
    0,3,1,4,2,5,
    f =
     [[0 3]
     [1 4]
     [2 5]]
    0,3,1,4,2,5,


#### 控制遍历顺序

- Fortran order 列序优先 `for x in np.nditer(a, order='F')`
- C order 行序优先 `for x in np.nditer(a.T, order='C')`


```python
import numpy as np

a = np.arange(6)
a = a.reshape(2, 3)
print('a = \n', a)

b = a.T
print('b = \n', b)

# C order
c = b.copy(order='C')
print('c =\n', c)
for x in np.nditer(c):
    print(x, end=', ')
print()

# Fortran order
d = b.copy(order='F')
print('d =\n', d)
for x in np.nditer(d):
    print(x, end=', ')
print()
```

    a = 
     [[0 1 2]
     [3 4 5]]
    b = 
     [[0 3]
     [1 4]
     [2 5]]
    c =
     [[0 3]
     [1 4]
     [2 5]]
    0, 3, 1, 4, 2, 5, 
    d =
     [[0 3]
     [1 4]
     [2 5]]
    0, 1, 2, 3, 4, 5, 


##### 显式设制

强制nditer对象使用某种顺序


```python
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
print('a = ')
print(a)

# C order
print('C order ->')
for x in np.nditer(a, order='C'):
    print(x, end=', ')
print()

# F order
print('F order ->')
for x in np.nditer(a, order='F'):
    print(x, end=', ')
print()
```

    a = 
    [[1 2 3]
     [4 5 6]]
    C order ->
    1, 2, 3, 4, 5, 6, 
    F order ->
    1, 4, 2, 5, 3, 6, 


##### 修改数组内容


```python
lx = np.array([1, 2, 3])
for x in np.nditer(lx, op_flags=['readwrite']):
    x[...] = x * 10
print(lx)
```

    [10 20 30]


##### 外部循环
`nditer`类的构造器拥有flags参数，它可以接受下列值：
- c_index 可以跟踪C顺序的索引
- f_index 可以跟踪Fortran顺序的索引
- multi-index 每次迭代可以跟踪一种索引类型
- external_loop 给出的值是具有多个值的一维数组，而不是零维数组


```python
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
print('a=')
print(a)
print('\nc_index => ')
for x in np.nditer(a, flags=['c_index']):
    print(x, end=', ')

print('\n\nf_index => ')
for x in np.nditer(a, flags=['f_index']):
    print(x, end=', ')

print('\n\nmulti_index => ')
for x in np.nditer(a, flags=['multi_index']):
    print(x, end=', ')

print('\n\nexternal_loop => ')
for x in np.nditer(a, flags=['external_loop']):
    print(x, end=', ')

print('\n\nexternal_loop C => ')
for x in np.nditer(a, flags=['external_loop'], order='C'):
    print(x, end=', ')

print('\n\nexternal_loop F => ')
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, end=', ')

```

    a=
    [[1 2 3]
     [4 5 6]]
    
    c_index => 
    1, 2, 3, 4, 5, 6, 
    
    f_index => 
    1, 2, 3, 4, 5, 6, 
    
    multi_index => 
    1, 2, 3, 4, 5, 6, 
    
    external_loop => 
    [1 2 3 4 5 6], 
    
    external_loop C => 
    [1 2 3 4 5 6], 
    
    external_loop F => 
    [1 4], [2 5], [3 6], 

##### 广播迭代
如果两个数组是可广播的，nditer组合对象能够同时迭代它们。假设数组a的维度是3x4，数组b的维度是1x4，则使用以下类型的迭代器（数组b被广播到数组a的大小）


```python
import numpy as np

a = np.arange(1, 13).reshape(3, 4)
print('a =')
print(a)

b = np.arange(1, 5).reshape(1, 4)
print('b =')
print(b)

c = np.arange(1, 4).reshape(3, 1)
print('c =')
print(c)

d = np.arange(1, 2).reshape(1, 1)
print('d =')
print(d)
print()

print('iter [a, b] C ->')
for x, y in np.nditer([a, b], order='C'):
    print(f'{x}:{y}', end=', ')
print()

print('iter [a, b] F ->')
for x, y in np.nditer([a, b], order='F'):
    print(f'{x}:{y}', end=', ')
print()

print('\n iter [a, c] C ->')
for x, y in np.nditer([a, c]):
    print(f'{x}:{y}', end=', ')

print('\n iter [a, c] F ->')
for x, y in np.nditer([a, c], order='F'):
    print(f'{x}:{y}', end=', ')
print()

print('\n iter [a, d] C ->')
for x, y in np.nditer([a, d]):
    print(f'{x}:{y}', end=', ')

print('\n iter [a, d] F ->')
for x, y in np.nditer([a, d], order='F'):
    print(f'{x}:{y}', end=', ')
```

    a =
    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]]
    b =
    [[1 2 3 4]]
    c =
    [[1]
     [2]
     [3]]
    d =
    [[1]]
    
    iter [a, b] C ->
    1:1, 2:2, 3:3, 4:4, 5:1, 6:2, 7:3, 8:4, 9:1, 10:2, 11:3, 12:4, 
    iter [a, b] F ->
    1:1, 5:1, 9:1, 2:2, 6:2, 10:2, 3:3, 7:3, 11:3, 4:4, 8:4, 12:4, 
    
     iter [a, c] C ->
    1:1, 2:1, 3:1, 4:1, 5:2, 6:2, 7:2, 8:2, 9:3, 10:3, 11:3, 12:3, 
     iter [a, c] F ->
    1:1, 5:2, 9:3, 2:1, 6:2, 10:3, 3:1, 7:2, 11:3, 4:1, 8:2, 12:3, 
    
     iter [a, d] C ->
    1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 
     iter [a, d] F ->
    1:1, 5:1, 9:1, 2:1, 6:1, 10:1, 3:1, 7:1, 11:1, 4:1, 8:1, 12:1, 

## 四、数组操作

### 4.1 修改数组形状

##### reshape

原型：reshape(shape, order='c')
作用：不改变数组的条件下修改形状
参数：
- shape 形状，整型的元组或列表
- order 'C' 按行，'F' 按列，'A' 原顺序，'k' 元素在内存中的出现顺序


```python
import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print('a =')
print(a)

b = a.reshape(2, 3)
print('b = ')
print(b)

c = a.reshape((2, 3), order='k')
print('c =')
print(c)

print('original a =')
print(a)
```

    a =
    [[1 2]
     [3 4]
     [5 6]]
    b = 
    [[1 2 3]
     [4 5 6]]



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[1], line 11
          8 print('b = ')
          9 print(b)
    ---> 11 c = a.reshape((2, 3), order='k')
         12 print('c =')
         13 print(c)


    ValueError: order 'K' is not permitted for reshaping


#### flat 属性
一个数组元素迭代器


```python
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
print('a =')
print(a)

for x in a.flat:
    print(x, end=', ')
```

    a =
    [[1 2 3]
     [4 5 6]]
    1, 2, 3, 4, 5, 6, 

#### flatten()

原型：`flatten(order='C')`
作用：展并数组并拷贝一份，顺序通常是“C风格”
注意：修改返回的数组不会对原数组产生影响


```python
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
print('a =')
print(a)

b = a.flatten()
print('b =')
print(b)

c = a.flatten('F')
print('c =')
print(c)

b[0] = 100
print('b = (updated)')
print(b)

print('a = (after b is updated)')
print(a)
```

    a =
    [[1 2 3]
     [4 5 6]]
    b =
    [1 2 3 4 5 6]
    c =
    [1 4 2 5 3 6]
    b = (updated)
    [100   2   3   4   5   6]
    a = (after b is updated)
    [[1 2 3]
     [4 5 6]]


#### ravel()

原型：numpy.ravel(order='C')
作用：展平的数组元素，顺序通常是“C风格”，返回的是数组视图（view，类似C++的引用）
注意：修改返回的数组会影响原数组，这个规则对于“F风格”的情况不适用。


```python
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
print('a =')
print(a)

b = a.ravel()
print('b =')
print(b)

b[0] = 100
print('b = (updated)')
print(b)

print('a = (after b is updated)')
print(a)

c = a.ravel(order='F')
print('c =')
print(c)

c[1] = 200
print('c = (updated)')
print(c)

print('a = (after b & c is updated)')
print(a)
```

    a =
    [[1 2 3]
     [4 5 6]]
    b =
    [1 2 3 4 5 6]
    b = (updated)
    [100   2   3   4   5   6]
    a = (after b is updated)
    [[100   2   3]
     [  4   5   6]]
    c =
    [100   4   2   5   3   6]
    c = (updated)
    [100 200   2   5   3   6]
    a = (after b & c is updated)
    [[100   2   3]
     [  4   5   6]]


### 4.2 翻转数组

#### transpose()

原型：numpy.transpose(a, axes=None)
作用：对换数组的维度
注意：修改会影响原数组
参数：
- a 要操作的数组
- axes 整数列表，对应维度，通常所有维度都会对换


```python
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
print('a =\n', a)

b = np.transpose(a)
print('b =\n', b)

b[0][0] = 100
print('b =\n', b)
print('a =\n', a)
```

    a =
     [[1 2 3]
     [4 5 6]]
    b =
     [[1 4]
     [2 5]
     [3 6]]
    b =
     [[100   4]
     [  2   5]
     [  3   6]]
    a =
     [[100   2   3]
     [  4   5   6]]


#### ndarray.T
类似 numpy.transpose()


```python
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
print('a =\n', a)

b = a.T
print('b =\n', b)

b[0][0] = 100
print('b =\n', b)
print('a =\n', a)
```

    a =
     [[1 2 3]
     [4 5 6]]
    b =
     [[1 4]
     [2 5]
     [3 6]]
    b =
     [[100   4]
     [  2   5]
     [  3   6]]
    a =
     [[100   2   3]
     [  4   5   6]]


#### rollaxis()
原型：numpy.rollaxis(a, axis, start=0)
作用：向后滚动特定的轴到一个特定位置
参数：
- a 要操作的数组
- axis 要向后滚动的轴，其他轴的相对位置不会改变
- start 会滚动到特定位置。默认为0，表示完整的滚动。


```python
# 2个维度的案例
import numpy as np

a = np.arange(6).reshape(2, 3)
print(f'a: {a.shape} =\n{a}\n')

b = np.rollaxis(a, 1)
print(f'b: {b.shape} =\n{b}\n')

b[0][0] = 100
print(f'a: {a.shape} =\n{a}\n')
```

    a: (2, 3) =
    [[0 1 2]
     [3 4 5]]
    
    b: (3, 2) =
    [[0 3]
     [1 4]
     [2 5]]
    
    a: (2, 3) =
    [[100   1   2]
     [  3   4   5]]



```python
# 3个维度的案例
import numpy as np

a = np.arange(24).reshape(2, 3, 4)
print(f'a: {a.shape} =\n{a}\n')

# 将轴2滚动到轴0
b = np.rollaxis(a, 2)
print(f'b: {b.shape} =\n{b}\n')

c = np.rollaxis(a, 2, start=1)
print(f'c: {c.shape} =\n{c}\n')
```

    a: (2, 3, 4) =
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
    
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
    
    b: (4, 2, 3) =
    [[[ 0  4  8]
      [12 16 20]]
    
     [[ 1  5  9]
      [13 17 21]]
    
     [[ 2  6 10]
      [14 18 22]]
    
     [[ 3  7 11]
      [15 19 23]]]
    
    c: (2, 4, 3) =
    [[[ 0  4  8]
      [ 1  5  9]
      [ 2  6 10]
      [ 3  7 11]]
    
     [[12 16 20]
      [13 17 21]
      [14 18 22]
      [15 19 23]]]


#### swapaxes()

原型：numpy.swapaxes(a, axis1, axis2)
作用：交换数组的两个轴
参数：
- a 要操作的数组
- axis1 对应第一个轴的整数
- axis2 对应第二个轴的整数


```python
import numpy as np

a = np.arange(24).reshape(2, 3, 4)
print(f'a: {a.shape} =\n{a}\n')

b = np.swapaxes(a, 1, 2)
print(f'b: {b.shape} =\n{b}\n')

b[0][0][0] = 100
print(f'b: {b.shape} =\n{b}\n')
print(f'a: {a.shape} =\n{a}\n')
```

    a: (2, 3, 4) =
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
    
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
    
    b: (2, 4, 3) =
    [[[ 0  4  8]
      [ 1  5  9]
      [ 2  6 10]
      [ 3  7 11]]
    
     [[12 16 20]
      [13 17 21]
      [14 18 22]
      [15 19 23]]]
    
    b: (2, 4, 3) =
    [[[100   4   8]
      [  1   5   9]
      [  2   6  10]
      [  3   7  11]]
    
     [[ 12  16  20]
      [ 13  17  21]
      [ 14  18  22]
      [ 15  19  23]]]
    
    a: (2, 3, 4) =
    [[[100   1   2   3]
      [  4   5   6   7]
      [  8   9  10  11]]
    
     [[ 12  13  14  15]
      [ 16  17  18  19]
      [ 20  21  22  23]]]


### 4.3 修改数组维度

#### 1 `broadcast()`

用于模拟广播的对象，它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。


```python
import numpy as np

x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
print(f'x =\n{x}\n')
print(f'y =\n{y}\n')

b = np.broadcast(x, y)
print(f'b =\n{b}\n')

r, c = b.iters
print(type(r), type(c))
print(next(r), next(c))
print(next(r), next(c))
# print(next(r), next(c))
# print(next(r), next(c))
# print(next(r), next(c))
# print(next(r), next(c))
# print(next(r), next(c))
# print(next(r), next(c))
# print(next(r), next(c))


b = np.broadcast(x, y)
print(f'b.shape = {b.shape}\n')
c = np.empty(b.shape)
c.flat = [u + v for (u, v) in b]
print(f'c = \n{c}\n')
print(f'x + y = (manualy)\n')
print(x + y)
```

    x =
    [[1]
     [2]
     [3]]
    
    y =
    [4 5 6]
    
    b =
    <numpy.broadcast object at 0x7fb28ca70220>
    
    <class 'numpy.flatiter'> <class 'numpy.flatiter'>
    1 4
    1 5
    b.shape = (3, 3)
    
    c = 
    [[5. 6. 7.]
     [6. 7. 8.]
     [7. 8. 9.]]
    
    x + y = (manualy)
    
    [[5 6 7]
     [6 7 8]
     [7 8 9]]


#### 2 `broadcast_to()`

原型：nupy.broadcast_to(array, shape, subok=False)
作用：将数组广播到新形状。它在原始数组上返回只读视图。它通常不连续。如果新形状不符合NumPy的广播机制，该函数可能会抛出ValueError。
参数：
- array 待修改的数组
- shape 修改后的形状


```python
import numpy as np

a = np.arange(3).reshape(1, 3)
print(f'a =\n{a}\n')

b = np.broadcast_to(a, (2, 3))
print(f'b = \n{b}\n')
```

    a =
    [[0 1 2]]
    
    b = 
    [[0 1 2]
     [0 1 2]]


#### 3 `expand_dims()`

原型：numpy.expand_dims(arr, axis=None)
作用：通过在指定位置插入新的轴来扩展数组形状
参数：
- arr 输入数组
- axis 新轴插入的位置


```python
import numpy as np

x = np.arange(6).reshape(2, 3)
print(f'x: {x.shape}/{x.ndim} =\n{x}\n')

y = np.expand_dims(x, 2)
print(f'y: {y.shape}/{y.ndim} =\n{y}')
```

    x: (2, 3)/2 =
    [[0 1 2]
     [3 4 5]]
    
    y: (2, 3, 1)/3 =
    [[[0]
      [1]
      [2]]
    
     [[3]
      [4]
      [5]]]
    x: (2, 3)/2 =
    [[0 1 2]
     [3 4 5]]


#### 4 squeeze()

原型：numpy.squeeze(arr, axis)
作用：从给定数组的形状中删除一维的条目
参数：
- arr 输入数组
- axis 删除轴的位置

注意：只删除长度为1的维度，否则会报错


```python
import numpy as np

x = np.arange(1, 25).reshape(1, 1, 2, 1, 1, 3, 4, 1)
print(f'x: {x.shape}/{x.ndim} =\n{x}\n')

y = np.squeeze(x)
print(f'y: {y.shape}/{y.ndim} =\n{y}\n')

z = np.squeeze(x, axis=7)
print(f'z: {z.shape}/{z.ndim} =\n{z}')
```

    x: (1, 1, 2, 1, 1, 3, 4, 1)/8 =
    [[[[[[[[ 1]
           [ 2]
           [ 3]
           [ 4]]
    
          [[ 5]
           [ 6]
           [ 7]
           [ 8]]
    
          [[ 9]
           [10]
           [11]
           [12]]]]]
    
    
    
    
       [[[[[13]
           [14]
           [15]
           [16]]
    
          [[17]
           [18]
           [19]
           [20]]
    
          [[21]
           [22]
           [23]
           [24]]]]]]]]
    
    y: (2, 3, 4)/3 =
    [[[ 1  2  3  4]
      [ 5  6  7  8]
      [ 9 10 11 12]]
    
     [[13 14 15 16]
      [17 18 19 20]
      [21 22 23 24]]]
    
    z: (1, 1, 2, 1, 1, 3, 4)/7 =
    [[[[[[[ 1  2  3  4]
          [ 5  6  7  8]
          [ 9 10 11 12]]]]
    
    
    
       [[[[13 14 15 16]
          [17 18 19 20]
          [21 22 23 24]]]]]]]


### 4.4 连接数组

#### 1 concatenate()

原型：numpy.concatenate((a1, a2, ...), axis)
作用：沿指定轴连接相同形状的两个或多个数组
参数：
- (a1, a2, ...) 相同类型的数组
- axis 指定的轴，沿着该轴连接数组，默认为0


```python
import numpy as np

a1 = np.arange(1, 7).reshape(2, 3)
a2 = np.arange(7, 10).reshape(1, 3)
a3 = np.arange(11, 17).reshape(2, 3)

print(f'a1 =\n{a1}')
print(f'a2 =\n{a2}')
print(f'a3 =\n{a3}\n')

a12 = np.concatenate((a1, a2))
print(f'a12 = \n{a12}\n')

a13 = np.concatenate((a1, a3), axis=1)
print(f'a13 = \n{a13}')
```

    a1 =
    [[1 2 3]
     [4 5 6]]
    a2 =
    [[7 8 9]]
    a3 =
    [[11 12 13]
     [14 15 16]]
    
    a12 = 
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    
    a13 = 
    [[ 1  2  3 11 12 13]
     [ 4  5  6 14 15 16]]


#### 2 stack()
原型：numpy.stack(arrays, axis)
作用：沿着新轴连接数组序列
参数：
- 相同形状的数组序列
- 数组中的轴，输入数组沿着它来堆叠


```python
import numpy as np

a1 = np.arange(11, 15).reshape(2, 2)
a2 = np.arange(21, 25).reshape(2, 2)
a3 = np.arange(31, 35).reshape(2, 2)
print(f'a1: {a1.shape}/{a1.ndim} =\n{a1}')
print(f'a2: {a2.shape}/{a2.ndim} =\n{a2}')
print(f'a3: {a3.shape}/{a3.ndim} =\n{a3}\n')

x0 = np.stack((a1, a2, a3), 0)
print(f'x0: {x0.shape}/{x0.ndim} =\n{x0}\n')

x1 = np.stack((a1, a2, a3), 1)
print(f'x1: {x1.shape}/{x1.ndim} =\n{x1}\n')

x2 = np.stack((a1, a2, a3), 2)
print(f'x2: {x2.shape}/{x2.ndim} =\n{x2}')
```

    a1: (2, 2)/2 =
    [[11 12]
     [13 14]]
    a2: (2, 2)/2 =
    [[21 22]
     [23 24]]
    a3: (2, 2)/2 =
    [[31 32]
     [33 34]]
    
    x0: (3, 2, 2)/3 =
    [[[11 12]
      [13 14]]
    
     [[21 22]
      [23 24]]
    
     [[31 32]
      [33 34]]]
    
    x1: (2, 3, 2)/3 =
    [[[11 12]
      [21 22]
      [31 32]]
    
     [[13 14]
      [23 24]
      [33 34]]]
    
    x2: (2, 2, 3)/3 =
    [[[11 21 31]
      [12 22 32]]
    
     [[13 23 33]
      [14 24 34]]]


#### 3 hstack() 和 vstack()

是 numpy.stack() 的变体，通过水平或垂直堆叠来生成数组。


```python
import numpy as np

a1 = np.arange(11, 15).reshape(2, 2)
a2 = np.arange(21, 25).reshape(2, 2)
print(f'a1: {a1.shape}/{a1.ndim} =\n{a1}')
print(f'a2: {a2.shape}/{a2.ndim} =\n{a2}\n')

x0 = np.hstack((a1, a2))
print(f'x0: {x0.shape}/{x0.ndim} =\n{x0}\n')

x1 = np.vstack((a1, a2))
print(f'x1: {x1.shape}/{x1.ndim} =\n{x1}\n')
```

    a1: (2, 2)/2 =
    [[11 12]
     [13 14]]
    a2: (2, 2)/2 =
    [[21 22]
     [23 24]]
    
    x0: (2, 4)/2 =
    [[11 12 21 22]
     [13 14 23 24]]
    
    x1: (4, 2)/2 =
    [[11 12]
     [13 14]
     [21 22]
     [23 24]]


### 4.5 分割数组

#### 1 split()

原型：numpy.split(ary, indices_or_sections, axis=0)
作用：沿指定的轴将数组分割为子数组
参数：
- ary 被分割的数组
- indices_or_sections 如果是一个整数，用该整数平均切分；如果是一个数组，为沿轴切分的位置（左开右闭）
- axis 沿哪个维度进行切分，默认为0，横行切分


```python
import numpy as np

a = np.arange(1, 11)
print(f'a = {a}')

print()
b = np.split(a, 2)
for i, x in enumerate(b):
    print(f'sub-array[{i}] =', x)

print()
b = np.split(a, [2, 5])
for i, x in enumerate(b):
    print(f'sub-array[{i}] =', x)
```

    a = [ 1  2  3  4  5  6  7  8  9 10]
    
    sub-array[0] = [1 2 3 4 5]
    sub-array[1] = [ 6  7  8  9 10]
    
    sub-array[0] = [1 2]
    sub-array[1] = [3 4 5]
    sub-array[2] = [ 6  7  8  9 10]



```python
import numpy as np

a = np.arange(1, 37).reshape(2, 3, 6)
print(f'a: {a.shape}/{a.ndim} =\n{a}\n')

print(f'split by axis 2 divided 2\n')
b = np.split(a, 2, 2)
for i, x in enumerate(b):
    print(f'sub-array[{i}]: {x.shape}/{x.ndim}=')
    print(x)
print()

print(f'split by axis 2 divided by array\n')
b = np.split(a, [1, 2, 5], 2)
for i, x in enumerate(b):
    print(f'sub-array[{i}]: {x.shape}/{x.ndim}=')
    print(x)
print()
```

    a: (2, 3, 6)/3 =
    [[[ 1  2  3  4  5  6]
      [ 7  8  9 10 11 12]
      [13 14 15 16 17 18]]
    
     [[19 20 21 22 23 24]
      [25 26 27 28 29 30]
      [31 32 33 34 35 36]]]
    
    split by axis 2 divided 2
    
    sub-array[0]: (2, 3, 3)/3=
    [[[ 1  2  3]
      [ 7  8  9]
      [13 14 15]]
    
     [[19 20 21]
      [25 26 27]
      [31 32 33]]]
    sub-array[1]: (2, 3, 3)/3=
    [[[ 4  5  6]
      [10 11 12]
      [16 17 18]]
    
     [[22 23 24]
      [28 29 30]
      [34 35 36]]]
    
    split by axis 2 divided by array
    
    sub-array[0]: (2, 3, 1)/3=
    [[[ 1]
      [ 7]
      [13]]
    
     [[19]
      [25]
      [31]]]
    sub-array[1]: (2, 3, 1)/3=
    [[[ 2]
      [ 8]
      [14]]
    
     [[20]
      [26]
      [32]]]
    sub-array[2]: (2, 3, 3)/3=
    [[[ 3  4  5]
      [ 9 10 11]
      [15 16 17]]
    
     [[21 22 23]
      [27 28 29]
      [33 34 35]]]
    sub-array[3]: (2, 3, 1)/3=
    [[[ 6]
      [12]
      [18]]
    
     [[24]
      [30]
      [36]]]


#### 2 hsplit()

split() 的变体，水平分割数组，通过指定要返回的相同形状的数组数量来拆分数组。


```python
import numpy as np

a = np.arange(1, 13).reshape(2, 6)
print(f'a = \n{a}')

b = np.hsplit(a, 2)
for i, x in enumerate(b):
    print(f'sub-array[{i}] =\n{x}')
```

    a = 
    [[ 1  2  3  4  5  6]
     [ 7  8  9 10 11 12]]
    sub-array[0] =
    [[1 2 3]
     [7 8 9]]
    sub-array[1] =
    [[ 4  5  6]
     [10 11 12]]


#### 3 vsplit()

split() 的变体，垂直分割数组，用法同 hsplit()


```python
import numpy as np

a = np.arange(1, 13).reshape(2, 6)
print(f'a = \n{a}')

b = np.vsplit(a, 2)
for i, x in enumerate(b):
    print(f'sub-array[{i}] =\n{x}')
```

    a = 
    [[ 1  2  3  4  5  6]
     [ 7  8  9 10 11 12]]
    sub-array[0] =
    [[1 2 3 4 5 6]]
    sub-array[1] =
    [[ 7  8  9 10 11 12]]


### 4.6 数组元素的添加与删除

#### 1 resize()

原型：numpy.resize(arr, shape)
作用：返回指定大小的新数组
参数：
- arr 要修改大小的数组
- shape 返回数组的新形状


```python
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
print(f'a =\n{a}')

b = np.resize(a, (3, 2))
print(f'b =\n{b}')
print(f'a =\n{a}')

c = np.resize(a, (3, 3))
print(f'c =\n{c}')
c = np.resize(a, (3, 5))
print(f'c =\n{c}')
```

    a =
    [[1 2 3]
     [4 5 6]]
    b =
    [[1 2]
     [3 4]
     [5 6]]
    a =
    [[1 2 3]
     [4 5 6]]
    c =
    [[1 2 3]
     [4 5 6]
     [1 2 3]]
    c =
    [[1 2 3 4 5]
     [6 1 2 3 4]
     [5 6 1 2 3]]


#### 2 append()

原型：numpy.append(arr, values, axis=None)
作用：
- 在数组的末尾添加值
- 追加操作会分配整个数组，并把原来的数组复制到新数组中
- 输入数组的维度必须匹配，否则报 ValueError
参数：
- arr 输入数组
- values 要向arr添加的值，需要和arr形状相同（除了要添加的轴）
- axis 默认为None，横行加成，返回总是为一维数组。当axis有定义是，分别为0或1的时候。为0时，列数要相同。为1时，行数要相同，数组加在右边。


```python
import numpy as np

x = np.arange(1, 7).reshape(2, 3)
print(f'x =\n{x}')

z0 = np.append(x, [10, 20, 30])
print(f'z0 =\n{z0}')

z1 = np.append(x, [[10, 20, 30]], axis=0)
print(f'z1 =\n{z1}')
z2 = np.append(x, [[10, 20, 30], [40, 50, 60]], axis=1)
print(f'z1 =\n{z2}')
```

    x =
    [[1 2 3]
     [4 5 6]]
    z0 =
    [ 1  2  3  4  5  6 10 20 30]
    z1 =
    [[ 1  2  3]
     [ 4  5  6]
     [10 20 30]]
    z1 =
    [[ 1  2  3 10 20 30]
     [ 4  5  6 40 50 60]]


#### 3 insert()

原型：numpy.insert(arr, obj, values, axis)
作用：在指定索引前，沿指定轴在输入数组中插入值。
注意：如果值的类型转换为要插入，则它与输入数组不同。插入没有原地的，会返回一个新数组。如果未提供轴，则输入数组会被展开。
参数：
- arr 输入数组
- obj 在其之前插入值的索引
- values 要插入的值
- axis 沿着它输入的轴，如果未提供，则输入数组会被展开


```python
import numpy as np

x = np.arange(1, 7).reshape(2, 3)
print(f'x =\n{x}')

z0 = np.insert(x, 3, [11, 13])
print(f'z0 =\n{z0}')

z1 = np.insert(x, 1, [11, 12, 13], axis=0)
print(f'z1 =\n{z1}')

z2 = np.insert(x, (1, 2), [[10], [20]], axis=1)
print(f'z2 =\n{z2}')

# 发生广播行为
z3 = np.insert(x, (1, 2), [100], axis=1)
print(f'z3 =\n{z3}')
```

    x =
    [[1 2 3]
     [4 5 6]]
    z0 =
    [ 1  2  3 11 13  4  5  6]
    z1 =
    [[ 1  2  3]
     [11 12 13]
     [ 4  5  6]]
    z2 =
    [[ 1 10  2 10  3]
     [ 4 20  5 20  6]]
    z3 =
    [[  1 100   2 100   3]
     [  4 100   5 100   6]]


#### 4 delete()

原型：numpy.delete(arr, obj, axis)
作用：返回从输入数组中删除指定子数组之后的新数组。与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开。
参数：
- arr 输入数组
- obj 要删除的子数组的索引。可以是切片、整数或整数数组
- axis 沿指定数组删除。如果未提供，则输入数组会被展开。


```python
import numpy as np

x = np.arange(10, 22).reshape(3, 4)
print(f'x =\n{x}\n')

y = np.delete(x, [4, 11])
print(f'y =\n{y}\n')

z = np.delete(x, 1, axis=0)
print(f'z =\n{z}\n')

zz = np.delete(x, 2, axis=1)
print(f'zz =\n{zz}')
```

    x =
    [[10 11 12 13]
     [14 15 16 17]
     [18 19 20 21]]
    
    y =
    [10 11 12 13 15 16 17 18 19 20]
    
    z =
    [[10 11 12 13]
     [18 19 20 21]]
    
    zz =
    [[10 11 13]
     [14 15 17]
     [18 19 21]]


#### 5 unique()

原型：numpy.unique(arr, return_index, return_inverse, return_counts)
作用：去除数组中的重复元素，并以排序后的数组返回
参数：
- arr 输入数组，如果不是一维数组则会展开
- return_index 如果为True，  则返回新列表在旧列表中的位置（下标），并以列表形式存储
- return_inverse 如果为True，则返回旧列表在新列表中的位置（下标），并以列表形式存储
- return_counts 如果为True，则返回去重数组中的元素在原数组中的出现次数


```python
import numpy as np

x = np.array([1, 5, 3, 2, 3, 3, 4, 5])

print(f'x = {x}')

a = np.unique(x)
print(f'a = {a}')

b = np.unique(x, return_index=True, return_inverse=True, return_counts=True)
print(f'b = {b[0]}\nidx:{b[1]}\nivs:{b[2]}\ncnt:{b[3]}')
```

    x = [1 5 3 2 3 3 4 5]
    a = [1 2 3 4 5]
    b = [1 2 3 4 5]
    idx:[0 3 2 6 1]
    ivs:[0 4 2 1 2 2 3 4]
    cnt:[1 1 3 1 2]


## 五、函数

### 5.1 字符串函数

字符串函数用于对dtype为numpy.string_或numpy.unicode_的数组执行向量化字符串操作
基于python内置库中的标准字符串函数，在字符数组类（numpy.char）中定义

#### add()
对两个数组的元素进行字符串连接


```python
import numpy as np

print(np.char.add(['sunck'], [' good']))
print(np.char.add(['sunck', 'kaige'], [' good', ' nice']))
```

    ['sunck good']
    ['sunck good' 'kaige nice']


#### multiply()
多重连接字符串


```python
import numpy as np

print(np.char.multiply("Hello ", 3))
```

    Hello Hello Hello 


#### center()

将字符串居中，并使用指定字符在左侧和右侧进行填充


```python
import numpy as np

print(np.char.center(['nice', 'good'], 10, fillchar='*'))
```

    ['***nice***' '***good***']


#### capitalize()
将字符串第一个字母转换为大写


```python
import numpy as np

print(np.char.capitalize(['hello world!', 'tom is a good man.']))
```

    ['Hello world!' 'Tom is a good man.']


#### title()
将字符串的每个单词的第一个字母转换为大写。


```python
import numpy as np

print(np.char.title(['hello world!', 'tom is a good man.']))
```

    ['Hello World!' 'Tom Is A Good Man.']


#### lower()

数组元素转化为小写


```python
import numpy as np

print(np.char.lower(['Hello world!', 'Tom is a GOOD man.']))
```

    ['hello world!' 'tom is a good man.']


#### upper()

数组元素转化为大写


```python
import numpy as np

print(np.char.upper(['Hello world!', 'Tom is a GOOD man.']))
```

    ['HELLO WORLD!' 'TOM IS A GOOD MAN.']


#### split()

根据指定分割符对字符串进行分割，并返回数组列表。


```python
import numpy as np

print(np.char.split(['Hello world!', 'Tom is a GOOD man.']))
```

    [list(['Hello', 'world!']) list(['Tom', 'is', 'a', 'GOOD', 'man.'])]


#### splitlines()
返回元素中的行列表，以换行符分割。


```python
import numpy as np

print(np.char.splitlines(['Hello world!', 'Tom is a\nGOOD\nman.']))
```

    [list(['Hello world!']) list(['Tom is a', 'GOOD', 'man.'])]


#### strip()
移除元素开头或结尾处的特定字符或空格。


```python
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


```python
import numpy as np

print(np.char.join('-', ['Hello', 'World']))
print(np.char.join(['-', ':'], [['Hello', 'World'], ['nice', 'good']]))
```

    ['H-e-l-l-o' 'W-o-r-l-d']
    [['H-e-l-l-o' 'W:o:r:l:d']
     ['n-i-c-e' 'g:o:o:d']]


#### replace()
使用新字符串替换字符串中的所有子字符串。


```python
import numpy as np

print(np.char.replace(['Tom is a nice cat.', 'Jerry is a nice mouse.'], 'nice', 'good'))
```

    ['Tom is a good cat.' 'Jerry is a good mouse.']


#### encode()
编码，数组元素依次调用 str.encode()


```python
import numpy as np

print(np.char.encode(['Tom', 'Jerry'], 'utf-8'))
```

    [b'Tom' b'Jerry']


#### decode()
解码，数组元素依次调用 str.decode()


```python
import numpy as np

a = np.char.encode(['Tom', 'Jerry'], 'utf-8')
print(np.char.decode(a, 'utf-8'))
```

    ['Tom' 'Jerry']


### 5.2 数学函数

#### 标准三角函数 sin(), cos(), tan()


```python
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


```python
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



```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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



```python
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


```python
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



```python
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



```python
import numpy as np

x = np.array([1, 2, 3, 4])
print(np.std(x))
print(np.sqrt(np.mean((x - np.mean(x)) ** 2)))
```

    1.118033988749895
    1.118033988749895


#### 方差`var()`

统计中的方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数，即 mean（（×- x.mean（）** 2）。换句话说，标准差是方差的平方根




```python
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



```python
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



```python
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


```python
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



```python
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


```python
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



```python
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



```python
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



```python
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


```python
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


```python
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


```python
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



```python

```

### 5.6 搜索函数

#### max(), min()

沿指定轴返回最大值或最小值。


```python
import numpy as np

x = np.array([30, 10, 15, 13, 38, 80])
print(x)
print(np.max(x), np.min(x))
```

    [30 10 15 13 38 80]
    80 10



```python
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


```python
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


```python
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


```python
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


```python
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


## 六、拷贝

### 6.1 赋值

简单的赋值不会创建数组对象的副本。相反，它使用原始数组的相同id0来访问它。idl返回 Python 对象的通用标识符，类似于C中的指针。

一个数组的任何变化都反映在另一个数组上。例如，一个数组的形状改变也会改变另一个数组的形状。


```python
import numpy as np

x = np.arange(1, 7).reshape(2, 3)
print(f'x = \n {x}')
print(f'id(x) = {id(x)}')
y = x
print(f'y = \n {y}')
print(f'id(y) = {id(y)}')

y.shape = (3, 2)

print(f'x = \n {x}')
print(f'id(x) = {id(x)}')

print(f'y = \n {y}')
print(f'id(y) = {id(y)}')
```

    x = 
     [[1 2 3]
     [4 5 6]]
    id(x) = 4568592048
    y = 
     [[1 2 3]
     [4 5 6]]
    id(y) = 4568592048
    x = 
     [[1 2]
     [3 4]
     [5 6]]
    id(x) = 4568592048
    y = 
     [[1 2]
     [3 4]
     [5 6]]
    id(y) = 4568592048


### 6.2 视图

又可称为浅拷贝，是数据的一个别称或引用，通过该别称或引用亦便可访问、操作原有数据，但原有数据不会产生拷贝。对视图进行修改，它会影响到原始数据，物理内存在同一位
置。

发生情况1：numpy的切片操作返回原数据的视图，修改数据会影响到原始数组


```python
import numpy as np

x = np.arange(1, 7)
print(f'x = {x}')
y = x[3:]
print(f'y = {y}')

y[1] = 100
print(f'x = {x}')
print(f'y = {y}')

print(id(x), id(y), id(x[0:]))
```

    x = [1 2 3 4 5 6]
    y = [4 5 6]
    x = [  1   2   3   4 100   6]
    y = [  4 100   6]
    4568592048 4567187344 4563199888


发生情况2：调用 ndarray 的 view（）函数产生一个视图

创建一个新的数组对象，该方法创建的新数组的维数更改不会更改原始数据的维数


```python
import numpy as np

x = np.arange(1, 7).reshape(2, 3)
print(f'x = \n{x}')
y = x.view()
print(f'y = \n{y}')
print(f'id(x) = {id(x)}, id(y) = {id(y)}')

y[1][0] = 100
print(f'x = \n{x}')
print(f'y = \n{y}')
print(f'id(x) = {id(x)}, id(y) = {id(y)}')

y.shape = (3, 2)
print(f'x = \n{x}')
print(f'y = \n{y}')
print(f'id(x) = {id(x)}, id(y) = {id(y)}')
```

    x = 
    [[1 2 3]
     [4 5 6]]
    y = 
    [[1 2 3]
     [4 5 6]]
    id(x) = 4567187344, id(y) = 4565945680
    x = 
    [[  1   2   3]
     [100   5   6]]
    y = 
    [[  1   2   3]
     [100   5   6]]
    id(x) = 4567187344, id(y) = 4565945680
    x = 
    [[  1   2   3]
     [100   5   6]]
    y = 
    [[  1   2]
     [  3 100]
     [  5   6]]
    id(x) = 4567187344, id(y) = 4565945680


### 6.3 副本

又可称为深拷贝，是一个数据的完整的拷贝，如果我们对副本进行修改，它不会影响到原始数据，物理内存不在同一位置

发生情况1：调用 ndarray 的 copy（）函数产生一个副本

作用：创建一个副本

说明：对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置


```python
import numpy as np

x = np.arange(1, 7).reshape(2, 3)
print(f'x = \n{x}')
print(f'id(x) = {id(x)}')

y = x.copy()
print(f'y = \n{y}')
print(f'id(y) = {id(y)}')

y[0][0] = 100
print(f'x = \n{x}')
print(f'y = \n{y}')
print(f'id(x) = {id(x)}, id(y) = {id(y)}')
```

    x = 
    [[1 2 3]
     [4 5 6]]
    id(x) = 4579375216
    y = 
    [[1 2 3]
     [4 5 6]]
    id(y) = 4579373392
    x = 
    [[1 2 3]
     [4 5 6]]
    y = 
    [[100   2   3]
     [  4   5   6]]
    id(x) = 4579375216, id(y) = 4579373392


发生情况2：序列的切片操作，调用deepCopy()函数


```python


# x = np.arange(1, 7)
x = [1, 2, 3, 4, 5, 6]

print(f'x = {x}')
print(f'id(x) = {id(x)}')

y = x[3:]
print(f'y = {y}')
print(f'id(y) = {id(y)}')

y[-1] = 100

print(f'x = {x}')
print(f'y = {y}')
print(f'id(x) = {id(x)}, id(y) = {id(y)}')
```

    x = [1, 2, 3, 4, 5, 6]
    id(x) = 4578797824
    y = [4, 5, 6]
    id(y) = 4578994176
    x = [1, 2, 3, 4, 5, 6]
    y = [4, 5, 100]
    id(x) = 4578797824, id(y) = 4578994176



```python

import copy

# x = np.arange(1, 7)
x = [1, 2, 3, 4, 5, 6]

print(f'id(x) = {id(x)}, x = {x}')

y = copy.deepcopy(x)
print(f'id(y) = {id(y)}, y = {y}')

y[-1] = 100
print(f'id(x) = {id(x)}, x = {x}')
print(f'id(y) = {id(y)}, y = {y}')
```

    id(x) = 4565453824, x = [1, 2, 3, 4, 5, 6]
    id(y) = 4578442944, y = [1, 2, 3, 4, 5, 6]
    id(x) = 4565453824, x = [1, 2, 3, 4, 5, 6]
    id(y) = 4578442944, y = [1, 2, 3, 4, 5, 100]


## 七、I/O函数

numpy可读写磁盘上的文本数据或二进制文件

numpy为ndarray对象引入了一个简单的文件格式：npy

npy文件用于存储重建ndarray所需的数据、图形、dype和其他信息

##### 常用IO函数

| IO函数                  | 作用                                               |
|:----------------------|-------------------------------------------------:|
| load()和save()         | 读写文件数据数组的两个主要函数，默认时数组以未压缩的原始二进制格式保存在扩展名为.npy的文件中 |
| savez()               | 用于将多个数组写入文件，默认时数组以未压缩的原始二进制格式保存在扩展名为.npz的文件中     |
| loadtext()和savetext() | 处理正常的文本文件(.txt等)                                 |

#### numpy.save()
原型：numpy.save(file, arr, allow_pickle=True, fix_imports=True)
作用：将数组保存到以.npy为扩展名的文件中
- file 要保存的文件，扩展名为.npy,如果文件露肩末尾没有扩展名.npy，该扩展名会被自动加上
- arr 要保存的数组
- allow_pickle 可选，布尔值，允许使用Python pickles保存对象数组，pickle用于在保存到磁盘文件或从磁盘文件读取之前，对对象进行序列化和反序列化
- fix_imports 可选，为方便python2中读取python3保存的数据


```python
# 保存到文件
import numpy as np

x = np.array([[10, 10], [1, 2], [3, 4]])
np.save("numpy-io-1.npy", x)
print(x.dtype, x)
```

    int64 [[10 10]
     [ 1  2]
     [ 3  4]]



```python
# 从文件读取
import numpy as np

y = np.load("numpy-io-1.npy")
print(y.dtype, y)
```

    int64 [[10 10]
     [ 1  2]
     [ 3  4]]


#### numpy.savez() 

原型：numpy.savez(file, *args, **kwds)

作用：将多个数组保存到以 npz 为扩展名的文件中

| 参数   | 说明                                                          |
|------|-------------------------------------------------------------|
| file | 要保存的文件，扩展名为 npz，如果文件路径末尾没有扩展名.nPz，该扩展名会被自动加上                |
| args | 要保存的数组，可以使用关键字参数为数组起一个名字，非关键字参数传递 的数组会自动起名为 arr_0，art_1,... |
| kwds | 要保存的数组使用关键字名称 |


```python
# 保存到文件
import numpy as np

x = np.arange(1, 7)
y = np.arange(2, 6)
z = np.arange(3, 9)

print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')

np.savez("numpy-io-2.npz", x, y, sin_arr=z)   
```

    x = [1 2 3 4 5 6]
    y = [2 3 4 5]
    z = [3 4 5 6 7 8]



```python
# 从文件中加载
import numpy as np

ret = np.load('numpy-io-2.npz')

print(ret['arr_0'])
print(ret['arr_1'])
print(ret['sin_arr'])
```

    [1 2 3 4 5 6]
    [2 3 4 5]
    [3 4 5 6 7 8]


#### numpy.savetxt()

原型：
- numpy.savetxt(FILENAME, a, fmt="%d", delimiter=",")
- numpy.loadtxt(FILENAME, dtype=int, delimiter=" ")

参数 delimiter
说明 指定各类分隔符、针对特定的转换器函数、需要跳过的行数等



```python
# 保存到文件
import numpy as np

x = np.array([100, 200, 300])
print(f'x = {x}')
np.savetxt("numpy-io-3.txt", x, fmt='%d', delimiter=',')
```

    x = [100 200 300]



```python
# 从文件中加载
import numpy as np

y = np.loadtxt('numpy-io-3.txt', dtype=int, delimiter=',')
print(f'y = {y}')
```

    y = [100 200 300]

