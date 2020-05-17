a=[22,36,4,56,4,54,43,34,435,34,22,4,5,23,4455,5,1,2]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            temp=a[j]#4
            a[j]=a[i]#22
            a[i]=temp#4
print("printing sorted elements:")
for i in a:
    print(i)
######
print()
a=2
b=4
c=5
c=a
b=a
print(b)
print(a)
a=c
print(a)
print(b)
