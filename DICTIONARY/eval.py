dictt=eval(input("Enter the dictionary values in {}:"))
#s=sum(dictt)
print(dictt)
print(type(dictt))
print(type(input))
#The eval() func. converts the strings as python expressions and returns the
#result as an integer
#In the above we are using the both keys and values.so we need to calculate the
#values not keys ..so by using the eval() it only takes the integer values not strings



#create a dict from keyboard and display the elements
x={}
print("How many elements:",end='')
n=int(input())
for i in range(n):
    print("enter the key value:",end='')
    k=input()
    v=input("ENter the value:")
    
    x.update({k:v})#append not working
print("the dict. value is:",x)
#the extending method

x={}
print("How many elements:",end='')
n=int(input())
for i in range(n):
    print("enter the key value:",end='')
    k=input()
    v=input("ENter the value:")
    
    x.update({k:v})#append not working
print("the dict. value is:",x)
for pname in x.keys():
     print(pname)
name=input('enter the name you want to check:')
runs=x.get(name,-1)
if runs==-1:#if we give the key names then it shows the value otherwise
    #it shows -1 value.
    print("he is not a player:")
else:
    print(runs)

