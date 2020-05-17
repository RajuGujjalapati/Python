import numpy as np
#1-d array
a=np.array([1,2,4,4,5,56,6,7,7])
print(a[0])
print(a[-1])
#2-d array
b=np.array([[1,2,3],[2,3,4]])
print(b)
print(b[1][2])
print(b[-1][-2])
#3-d array
c=[[[1,2,3,4],[5,6,7,8],[3,4,2,3]],[[2,3,4,1],[9,8,7,6],[6,5,4,4]]]
d=np.array(c)
print(d)
print(d.size)

print(d[-1][2][2])
#slicing
print(a[:4])
print(a[1::2])#taking step
print(b[0,1:])
print(b[0:,0:])
print(b[::,::2])
#3-d
print(d[:,:,:1])
print(d[:,1:2,1:3])
print(d[:,:,::2])
