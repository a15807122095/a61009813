import numpy as np
"""
数组的创建
"""
a = np.array([1,2,3,4,5])  # 打印 [1 2 3 4 5]
b = np.array(range(1,6))   # 打印 [1 2 3 4 5]
# 数组的常用表示方法
c= np.arange(1,6)          # 打印 [1 2 3 4 5]
# np.arange([start,] stop[, step,], dtype=None)

# 指定数组的数据类型
a1 = np.array([1,0,1,0],dtype=np.bool)
print(a1, 'type:', a1.dtype)   # 打印 [ True False  True False] type: bool

# 修改数组的数据类型
a2 = a.astype(np.int8)
print(a2, 'type:', a2.dtype)

# 修改浮点型小数数组
b1 = np.array(
    [0.0485436, 0.26320629, 0.68795641, 0.75986325, 0.96843121]
)
b2 = np.round(b1, 2)
print(b2)

"""
数组的形状
"""
a3 = np.array([[1,2,3,4,5], [4,5,6,7,8]])
# 修改数组的形状
a4 = a3.reshape(5,2)
print(a3,'shape:',a3.shape)
print(a4,'shape:',a4.shape)
a5 = a3.flatten() # 将多维数组降至一维数组


"""
数组的计算
"""
# 数组和数的计算
a6 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a6*3)

# 数组和数组的计算




"""
数组的索引和切片
"""
a7 = np.array([
    [0,1,2,3,4,5],
    [10,11,12,13,14,15],
    [20,21,22,23,24,25],
    [30,31,32,33,34,35],
    [40,41,42,43,44,45]
])

print(a7[1], type(a7[1]))        # 取行  [10 11 12 13 14 15] <class 'numpy.ndarray'>
print(a7[:,1], type(a7[:,1]))    # 取列  [ 1 11 21 31 41] <class 'numpy.ndarray'>
print(a7[1:3], type(a7[1:3]))    # 取多行 [[10 11 12 13 14 15] [20 21 22 23 24 25]] <class 'numpy.ndarray'>
print(a7[:,2:4])                 # 取多列 [[ 2  3] [12 13] [22 23] [32 33] [42 43]]
print(a7[[1,3],:])               # 指定第1,3行的所有列
print(a7[:,[2,4]])               # 指定所有列的2,4行


"""
数组中数值的修改
"""
a8 = np.array([
    [0,1,2,3,4,5],
    [10,11,12,13,14,15],
    [20,21,22,23,24,25],
    [30,31,32,33,34,35],
    [40,41,42,43,44,45]
])
a8[:,2:4] = 1
print(a8)


"""
数组的三元运算符
"""
a9 = np.arange(24).reshape((4,6))
a10 = np.where(a9<10,3,7)  # 将索引小于10的数值更换为3，不满足的更换为7
print(a10)

