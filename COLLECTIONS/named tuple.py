'''Named tuples are basically easy-to-create, lightweight object types.
Named tuple instances can be referenced using object-like variable
dereferencing or the standard tuple syntax. They can be used similarly
to struct or other common record types, except that they are immutable
'''
from collections import namedtuple
a=namedtuple('course','name,subject,king')#we can define values by removing ',' also.
#course is the object
#may be 'a' is the class
s=a('ml','python','new')
print(s)
s1=a._make(['AI','python','don'])#Make the namedtuple from the list of values.
print(s1)

###############################

pt1=(1.2,1.4)
pt2=(2.4,1.5)
from math import sqrt
line_length=sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
print(line_length)
##or we can use named tuple####


point=namedtuple('point','x y')
pt1=point(1.2,4.3)
pt2=point(2.3,32.4)
lin_len=sqrt((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)
print(lin_len)
