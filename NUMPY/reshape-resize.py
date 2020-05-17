#re-shape
import numpy as np
a=np.arange(1,11)
b=a.reshape((5,2))
print(b)
b1=a.reshape((5,2),order='F')
print(b1)
c=a.reshape((2,5))
print(c)
#(or)we can use below method also
b2=np.reshape(a,(5,2,1))
print(b2)
##########re-size
b3=np.resize(a,(3,7))#it gives new array, but it won't alter standard array
print(b3)
#to alter original array use the below code
a.resize((5,2))
