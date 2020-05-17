#indexing
#slicing
import numpy
my_list=[[10,20,30],[40,50,60],[70,80,90]]
matrix=numpy.array(my_list)
print(matrix)
#[row_lwr:row_upp,col_low:col_upp]
res=matrix[:,:]
print(res)
print()
res=matrix[0:2,0:3]
res1=matrix[0:3,0:2]
print(res)
print()
print(res1)
