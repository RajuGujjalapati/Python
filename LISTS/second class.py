"""L1=[2,3,4,5]
L2=[3,9,5,6]
res=L1+L2
print(res)
res=L1*3
print(res)
#res=L1[]
print(res)
res= 5 in L1
print(res)
print(L1[1:4])"""

L1=[2,7,9,15,3,1.8,3,3,3,3]
res=len(L1)
print(res)
"""res=max(L1)
res=min(L1)
res=type(L1)
res=id(L1)"""
L1.append(20)
print(L1)
L1.extend([30,40,50])
print(L1)
L1.insert(2,50)
print(L1)
del L1[0]
print(L1)
del L1[-2:]
print(L1)
res=L1.pop(4)
print(L1)
L1.insert(4,3)
print(L1)
L1.remove(3)
print(L1)

res=L1.count(3)
while (res>0):
    L1.remove(3)
    res=res-1
    print(L1)
res=L1.index(15,0,len(L1))
print(res)
L1.sort()
print(L1)
L1.reverse()
print(L1)
L2=L1
print(L1)
print(L2)
del L1[0:2]
print(L1)
print(L2)
print(id(L1))
print(id(L2))
L2=L1.copy()
print(L1)
print(L2)
del L1[0:2]
print(L1)
print(L2)
