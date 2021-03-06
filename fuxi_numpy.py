'''
2019-3-11
复习numpy
'''
import numpy as np
a=np.array([[1,2],[3,4]])
print(a)
print(a.ndim)
print(a.shape)
print(a.size)

b=np.array([1,2,3])
print(type(b))
print(b[0],b[1],b[2])
b[0]=8
print(b[0])
#其他创建数组的方法
c=np.zeros((2,2))
print(c)
d=np.ones((2,2))
print(d)
#创建单位矩阵
e=np.eye(2)
print(e)
#随机值
f=np.random.random((2,2))
print(f)
print('--------------数组索引-----------')
#创建一个二维数组,shape为(3,2)
a=np.array([[1,2],[3,4],[5,6]])
b=a[:1,1:2]
print(b)
#可以同时使用整型和切片语法来访问数组,这样做会产生比原数组低阶的新数组
row_r1=a[1,:]
row_r2=a[1:2,:]
print(row_r1,row_r1.shape)
print(row_r2,row_r2.shape)
#使用切片语法访问数组时,得到的总是原数组的一个子集
print(a[[0,1,2],[0,1,0]])
print(np.array([a[0,0],a[1,1],a[2,0]]))
print(a.dtype)
print('----------------数组计算--------------')
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
print(x+y)
print(np.add(x,y))
print(x-y)
print(np.subtract(x,y))
print(x*y)
print(np.multiply(x,y))
print(np.divide(x,y))
print(np.sqrt(x))
print('------------矩阵乘法--------------')
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
v=np.array([9,10])
w=np.array([11,12])
print(v.dot(w))
print(np.dot(v,w))
print(x.dot(v))
print(np.dot(x,v))
print(np.sum(x,axis=0))#按列相加
print(np.sum(x,axis=1))#按行相加
print(x.T)
