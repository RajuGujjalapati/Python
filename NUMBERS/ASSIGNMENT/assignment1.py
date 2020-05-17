def var(n):
    var=n[0]#value starts from here
    for i in range(1,len(n)):
        if(var<n[i]):
          var=n[i]
    print("max value is", var)
var([45,21,3233,334])###o/p is 3233
    
#######
n=(1,323,2333,212)
print(len(n))
##########
def var(n):
    var=n[0]
    for i in range(1,len(n)):
        if(var<n[i]):
          var=n[1]
    print("max value is", var)
var([45,21,3233,334])####o/p is 21 because n[1] uses 
#######
def var(n):
    var=n[0]
    for i in range(1,len(n)):
        if(var<n[i]):
          var=n[3]
    print("max value is", var)
var([45,21,3233,334])####o/p is 334
######
def var(n):
    var=n[0]
    for i in range(len(n)):
        if(var<n[i]):
          var=n[i]
    print("max value is", var)
var([45,21,3233,334])

