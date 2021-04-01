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


```
# 保存到文件
import numpy as np

x = np.array([[10, 10], [1, 2], [3, 4]])
np.save("numpy-io-1.npy", x)
print(x.dtype, x)
```

    int64 [[10 10]
     [ 1  2]
     [ 3  4]]



```
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


```
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



```
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



```
# 保存到文件
import numpy as np

x = np.array([100, 200, 300])
print(f'x = {x}')
np.savetxt("numpy-io-3.txt", x, fmt='%d', delimiter=',')
```

    x = [100 200 300]



```
# 从文件中加载
import numpy as np

y = np.loadtxt('numpy-io-3.txt', dtype=int, delimiter=',')
print(f'y = {y}')
```

    y = [100 200 300]

