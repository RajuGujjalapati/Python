"""def f():
    print("HI")
#f()#hi
g=f
g()#first-class functions"""
#1.
print("1st function")
def outer():
    x=3
    def inner():
        y=3
        print(x)
    return inner()
outer()#o/p:-3
#2.
print("2nd function")
def outer():
    x=3
    def inner():
        print(x)
        
    return inner()
a=outer()
print(a)#o/p:-3,None
#None enduku ante inner() lo value ni return cheydaniki em aledu so, adi None ani chupistundi.
#3.
print("3rd one")
def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner()
a=outer()# here a is representing inner()
#ante inner() print avvadaniki oka print statement istunnam
#so, anduke manam ekkada inner ni 'a' represent chestundi antunnam
print(a)#o/p:-6
4.
#
def outer():
    x=3
    def inner():
        y=3
        result=x+y

        return result
    return inner
a=outer()#o/p:- <function outer.<locals>.inner at 0x037951D8>
#outer func anedi 'a' tho ikkada represent chestunna
#so, a anedi inner referense(return inner ki func.ee ledu kada, anduku manam 'a' tho
#inner ni represent chestunnam
#to know that
print(a.__name__)#prints inner.......
print(a)




#as per mana knowledge prakaram manama inner function in outer() tarwata ala piliste
#adi radu ,means error chupistundi kabbati...
#ikkkda main use adea manaku
5.
z=1
def outer():
    x=3
    print(x)
    def inner():
        y=3
        result=x+y+z#if you assign z value to new value(z=3), then it will going to print z as 3 not 1 because of its local scope
        

        return result
    return inner
a=outer()#a anedi inner ni represent chestundi
print(a())#closure

