#i - 整数
#b - 布尔
#u - 无符号整数
#f - 浮点
#c - 复合浮点数
#m - timedelta
#M - datetime
#O - 对象
#S - 字符串
#U - unicode 字符串
#V - 固定的其他类型的内存块 ( void )
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

#定义整型int = i
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

#定义bool型
import numpy as np
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

#创建视图，更改视图并显示两个数组
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)

#base   每个 NumPy 数组都有一个属性 base，如果该数组拥有数据，则这个 base 属性返回 None。否则，base 属性将引用原始对象。
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)

#展平数组使用reshape（-1）
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

#迭代数组   迭代意味着遍历每一个元素
#迭代不同数据类型的数组使用op_dtypes
#NumPy 不会就地更改元素的数据类型（元素位于数组中），因此它需要一些其他空间来执行此操作，该额外空间称为 buffer，为了在 nditer() 中启用它，我们传参 flags=['buffered']。
import numpy as np
arr = np.array([1,2,3])
for x in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
    print(x)

#使用ndenumerate（）进行枚举迭代   枚举2D数组元素
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)