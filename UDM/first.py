#module:collection of functions
print("loading first module")
def createfiles(*files):#variable length arguments
    for x in files:
        fvar=open(x,'w')
        fvar.close()
        print("created",x)
def reversestr(x):
    return x[::-1]
def F1():
    print("hello")
def F2():
    print("welcome")
    
