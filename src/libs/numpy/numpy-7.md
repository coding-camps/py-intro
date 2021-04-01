## 六、拷贝

### 6.1 赋值

简单的赋值不会创建数组对象的副本。相反，它使用原始数组的相同id0来访问它。idl返回 Python 对象的通用标识符，类似于C中的指针。

一个数组的任何变化都反映在另一个数组上。例如，一个数组的形状改变也会改变另一个数组的形状。


```
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


```
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


```
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


```
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


```


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



```

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

