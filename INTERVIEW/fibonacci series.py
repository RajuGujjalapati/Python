n=10
n1=0
n2=1
count=2#because we are already giving n1 and n2 values,
#so,we are strating the count number with 2.
print(n1,',',n2,end=',')
while count<n:
    res=n1+n2
    print(res,end=',')
    n1=n2
    n2=res
    count+=1
################
x,y=0,1
while y<=50:
    print(y)
    x,y=y,x+y
