speed=[99,3,32,23,23,424,43,2,4]
import numpy
x=numpy.mean(speed)
print(x)
#################
y=sum(speed)

find_len=len(speed)
res=y/find_len
print(res)
##########
total=0
for i in speed:
    total=total+i
    
     
    
#speed+=speed[i]
print(total/find_len)
