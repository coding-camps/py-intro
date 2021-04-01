## 三、元素操作

### 3.1 切片和索引


```
import numpy as np

arr = np.arange(10)
print(arr)
print(arr[1])
```

    [0 1 2 3 4 5 6 7 8 9]
    1



```
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


```
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



```
print(arr[2], type(arr[2]))
print(arr[2][1], type(arr[2][1]))
```

    [6 7 8] <class 'numpy.ndarray'>
    7 <class 'numpy.int64'>



```
print(arr[2:])
print(arr[:2])
```

    [[ 6  7  8]
     [ 9 10 11]
     [12 13 14]]
    [[0 1 2]
     [3 4 5]]


切片还可以包含省略号“...”，来使选择元组的长度和数组的维度相同。如果在行位置使用省略号，它将返回包含行中元素的ndarray


```
arr = np.arange(1, 16)
arr.shape = (5, 3)
print(arr)
```

    [[ 1  2  3]
     [ 4  5  6]
     [ 7  8  9]
     [10 11 12]
     [13 14 15]]



```
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



```
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


```
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


```
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


```
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


```
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



```
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


```
# 形状相同
import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
c = a + b
print(c)
```

    [11 22 33]



```
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



```
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


```
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


```
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


```
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


```
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


```
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


```
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
