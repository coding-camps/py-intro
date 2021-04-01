## 四、数组操作

### 4.1 修改数组形状

##### reshape

原型：reshape(shape, order='c')
作用：不改变数组的条件下修改形状
参数：
- shape 形状，整型的元组或列表
- order 'C' 按行，'F' 按列，'A' 原顺序，'k' 元素在内存中的出现顺序


```
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

    Cell In[74], line 11
          8 print('b = ')
          9 print(b)
    ---> 11 c = a.reshape((2, 3), order='k')
         12 print('c =')
         13 print(c)


    ValueError: order 'K' is not permitted for reshaping


#### flat 属性
一个数组元素迭代器


```
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


```
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


```
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


```
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


```
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


```
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



```
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


```
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


```
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


```
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


```
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


```
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


```
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


```
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


```
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


```
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



```
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


```
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


```
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


```
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

    a: (2, 3)/2/6 =
    [[1 2 3]
     [4 5 6]]
    b: (3, 2)/2/6 =
    [[1 2]
     [3 4]
     [5 6]]
    c: (3, 3)/2/9 =
    [[1 2 3]
     [4 5 6]
     [1 2 3]]
    c: (3, 5)/2/15 =
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


```
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


```
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


```
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


```
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

