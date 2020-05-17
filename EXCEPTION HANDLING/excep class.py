var="today we have python class"
res="NA"
try:
    res=var.index('java',0,len(var))
except Exception as err:
    print("Hey! no java found in var")
    print(err)
print(res)
a=20
b=40
res=a+b
print(res)
print("complete")
#2.
"""print("file example")
try:
    fvar=open(r'ab.txt','r')
except Exception as err:
    print("i think no file ab.txt present lets create")
    fvar=open(r'ab.txt','w')
    fvar.close()
    print("create ab.txt")
    print(err)
print("complete")#If we run the program two tumes check"""
#3.
print("file example")
try:
    fvar=open(r'ab.txt','r')
except FileNotFoundError as err:
    print("i think no file abc.txtpresent lets create")
    fvar=open(r'ab.txt','w')
    fvar.close()
    print("create ab.txt")
    print(err)
except NameError as err:
    print("same issue in func name check it")
    print(err)
#If we run the program two times check
#after first add some data then run for 2nd time at the 2nd time the data will clear
finally:
    print("default block")
    #fvar.close()#whether the exception or not it will be executed
print("complete")


        

        
