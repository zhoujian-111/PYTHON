#ufuncs 指的是“通用函数”（Universal Functions），它们是对 ndarray 对象进行操作的 NumPy 函数。
#where 布尔值数组或条件，用于定义应在何处进行操作。
#dtype 定义元素的返回类型。
#out 返回值应被复制到的输出数组。

#使两个列表相加
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z)
#与add（）一样
import numpy as np
x = [1,2,3,4,5]
y = [5,6,7,8,9]
z = np.add(x,y)
print(z)