import numpy as np
a=np.arange(1,5)
b=np.arange(6)
print(np.concatenate((a,b)))
c=np.zeros(10)
#the above is going to store the values of both 'a' and 'b'
print(np.concatenate((a,b),out=c))
print(c)
#'c' stores the 'a' and 'b' values.
#####2-d array#########
a1=np.array([[1,2],[3,4]])
b1=np.array([[5,6]])
print(np.concatenate((a1,b1)))
print(np.concatenate((a1,b1))) 
