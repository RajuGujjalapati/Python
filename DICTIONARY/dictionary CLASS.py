d1={'B':200,'C':300,'D':400,'A':500}
res=len(d1)
print(res)
res=d1.items()
print(d1)
res=d1.values()
print(res)
for x,y in d1.items():
    print(x,y)
    #want to del
    #key value
del d1['C']
print(d1)
#d1.clear()
#print(d1)
#del d1
#print(d1)
#print(d1['x'])
res=d1.get('B',"novalue")
print(res)
print(d1)
res=d1.setdefault('x',5500)
print(res)
print(d1)
d2={'x':5500,'y':6000}
d2.update(d1)
print(d1)
print(d2)
d3={}
d3.update(d1)
d3.update(d2)
print(d1)
print(d2)
print(d3)
d3=d2.copy()
print(d3)
del d3
print(d3)

