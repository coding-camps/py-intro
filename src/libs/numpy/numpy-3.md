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


```
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


```
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



```
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



```
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


```
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


```
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



```
# 生成随机整数
print(np.random.randint(10))
print(np.random.randint(0, 10, 5))
```

    8
    [8 8 0 6 1]



```
# 返回标准正态分布N(0,1)的一个或一组样本
print(np.random.randn())
print(np.random.randn(2))
print(np.random.randn(2, 3))
```

    0.8810603641789418
    [ 0.35262675 -1.10266781]
    [[ 0.29848657 -0.38834993  0.36441861]
     [-1.02179129  0.50777643  1.83670195]]



```
# 生成高斯分布的概率密度随机数
print(np.random.normal())
print(np.random.normal(loc=1, scale=2, size=5))
```

    -1.1460308867811968
    [0.88005893 2.6173731  2.19524246 2.84205078 3.4007643 ]


### 2.3 numpy数组与python列表的对比


```
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



```
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



```
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

