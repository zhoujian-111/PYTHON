#连接数组时候concatenate（）函数
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
print(arr)

#沿着行（axis=1）连接两个2D数组
import numpy as np
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr = np.concatenate((arr1,arr2),axis = 1)
print(arr)

#使用堆栈来连接数组
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

#沿行堆叠   arr = np.hstack((arr1,arr2))
#沿列堆叠   arr = np.vstack((arr1,arr2))
#沿高度deep堆叠   arr = np.dstack((arr1,arr2))
#拆分用split（）    数组我们用array_split()分割数组
#沿行  列  高度  用法与上面的类似




#搜索用where（）
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#有一个searchsorted（）的方法，该方法在数组中执行二进制搜索
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

#数组排序 sort（）
import numpy as np
arr = np.array([3,2,0,1])
print(np.sort(arr))

#数组过滤
#创建过滤器数组
#例题1：  创建一个仅返回大于62的值得过滤器数组
import numpy as np
arr = np.array([61,62,63,64,68])
#创建一个空列表
filter_arr = []
#遍历arr中的每一个元素
for element in arr:
    if element > 62:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
#直接从数组中创建   简化：：：：
import numpy as np
arr = np.array([61,62,63,64,65])
filter_arr = arr >62
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

#随机生成熟  random
#例子：   生成一个0-100的随机整数
from numpy import random
x = random.randint(100)
print(x)
#浮点数
from numpy import random
x = random.rand()
print(x)
#随机数组
from numpy import random
x = random.randint(100,size=(5))
print(x)
#生成3行2D数组
from numpy import random
x = random.randint(100, size=(3,5))
print(x)
