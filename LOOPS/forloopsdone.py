data=(1,2)
i=55
j=2323
for i in data:
    for j in data:
        for k in data:
            print("i is:",i)
            print("j is",j)
            print("k is:",k)
    
#"i" holds first value and then "j" prints all these values 
x=9
for i in range(1,11):
    print("%iX%i=%i"%(x,i,x*i))
###3.
values=[1,5,10,15,20]
my_len=len(values)
for i in range(my_len):
    print(i,values[i]**2)
##4.
data="Helloworld!"
num=1
for i in data:
    print("heres the letter"+ str(num) +"of it:"  ,i)
    num+=1
#5.
my_str="python"
x=0
for i in my_str:
    x+=1
    print(my_str[0:x])
for i in my_str:
    x-=1
    print(my_str[0:x])
#6.
