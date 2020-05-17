L1=iter([1,2,5,7])
for x in L1:
    print(x)
for y in L1:
    print(y)
for z in L1:
    print(z)
    #string , list, dictionary,tuple.
    #iterators uses at one time unlike generators
mytuple=("apple","banana","orange")
mylit=iter(mytuple)
print(next(mylit))
print(next(mylit))
print(next(mylit))

mystr="banana"
myit=iter(mystr)
for i in myit:
    print((i))
for j in myit:
    print(j)

    
