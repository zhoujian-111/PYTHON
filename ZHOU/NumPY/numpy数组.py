#安装numpy     命令  pip install numpy
#numpy 通常以np别名导入
import numpy
import numpy as np
arr = numpy.array([1,2,3,4,5])
print(arr)

#检查numpy版本
import numpy as np
print(np.__version__)

#创建numpy ndarray对象
import numpy as np
arr = np.array([1,2.,3,4,5])
print(arr)
print(type(arr))

#一维数组1-D
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

#二维数组
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

#numpy数组提供了ndim属性
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#访问数组元素，索引从0开始，arr【0】为第一个元素
#负索引，从尾开始访问数组
#裁切数组时包括开始索引，不包括结束索引
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#裁切数组中索引4到结尾的元素
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

#裁切开头到索引4的元素
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

#step确定裁切步长
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])   #从1到5中，返回相隔的元素
