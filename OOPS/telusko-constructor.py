class A:
    def __init__(self):
        print("class A constructor")
    def feautre1(self):
        print("feautre 1 in A")
    def feautre2(self):
        print("feautre 2 in A")
class B():
    def __init__(self):
        #super().__init__()
        print("class B constructor")
    
    def feautre3(self):
        print("feautre 3 in B")
    def feautre4(self):
        print("feautre 4 in B")
#b=B()#it still calls the 'A' constructor

#then if we add the __init__() method then it calls the B-__init__()
#NOt 'A' init
#*If we want to call the 'A' init then use super function.
#when we are calling 'B',first it will call the 'B' class and then it jumps to "A' clss.
class C(A,B):
    
    def __init__(self):
        super().__init__()
        print("In C init")
    def fuct(self):
        super().feautre3()
c=C()
c.fuct()#horay we are getting the method name.
#if we use super class then it will call the __init__ from left to right.
#(MRO)-Method Resolution Order.---left-to-right.
#The same for methods if we have the same method names , then it prints first method
#values ____like --left-right....

#here is the new one ...if we want to call the method then we can use super func
#below is the example
