#python is providinfd se
import numpy as np
my_list=[[10,20,30],[23,35,56],[34,56,78]]
matrix=np.array(my_list)
print(matrix)
print("size:",matrix.size)
print("Datatype:",matrix.dtype)
print("Dimension:",matrix.ndim)
print("Shape:",matrix.shape)


x=np.ones((7,5))
print(x)
y=np.random.random((5,1,5))
print(y)
print()
print(x+y)
#advanced indexing.
a=np.arange(1,10)
index=np.array([1,4,5])
print(a[index])
print(a[[1,4,5]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b[[1,1,2],[0,2,1]])
#boolean indexing
print(a[a<0])

print(a[a>0]*2)#multiplies all the data
print(a[a>0]/2)
print(a[a>0]+2)
a1=np.array([1,2,3,4,5])
b1=np.array([1,4,5,6,9])
print(a1+b1)
