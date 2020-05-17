#1.https://www.datacamp.com/community/tutorials/decorators-python#comments
class printing:
    def __init__(self,name):
        self.name=name
        
    def print_name(self):
        print("Entered user name is:",self.name)
obj=printing("KING")
obj.print_name()
#if i just call the object itself what happens#obj()
#shows error


#2.we can call using built-in __call__ maethod to call the function directly
class printing:
    def __init__(self,name):
        self.name=name
        
    def __call__(self):
        print("Entered user name is:",self.name)
obj=printing("KING")
obj()
#3.class decorator
class Decorator:
    def __init__(self,func):
        self.func= func
    def __call__(self):
        str1=self.func()
        return str1.upper()
@Decorator
def greet():
    return "good night"
print(greet())


#4.
class Check_div:
    def __init__(self,func):
        self.func=func
    def __call__(self,*args,**kwargs):
        list1=[]
        list1= args[1:]
        for i in list1:
            if i==0:
                return "You can't divide with zero:"
        else:
            return self.func(*args,**kwargs)
@Check_div
def div(a,b):
    return a/b
@Check_div
def div1(a,b,c):
    return a/b/c
print(div(10,0))
print(div1(19,3,4))
