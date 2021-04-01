## 一、初识NumPy

### 1.1 NumPy简介

#### 版本号


```
import numpy as np

print(np.__version__)
print(np.version.version)
print(np.version.full_version)
```

### 1.2 ndarray对象简介

#### 简介
- 下标从0开始
- 是同类型元素的数组
- 每个元素都有相同的大小

#### 属性
- `dtype` 元素数据类型
- `shape` 形状，一个元组
- `stride` 跨度元组，从当前维度前进到下一元素需要跨过的字节数
