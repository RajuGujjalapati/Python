class B:
    addr="Banglore"
    def changeage(elf,newage):#here i am changed self to elf.
        elf.empage=newage
        return elf.empage
    def C1(x,y):
        res=x**y
        return res
    def _B1():
        print("Hello")
class A(B):
    count=0
    def __init__(self,name,age,sal):
        self.empname=name
        self.empage=age
        self.empsal=sal
        print(self.empname,self.empage,self.empsal)
        A.count+=1
    def displaysal(self):
        return self.empsal
    def changename(self,newname):
        self.empname=newname
    def C1(x,y):
        res=x+y
        return res
    def C2(x):
        return x.upper()
    def incrementsal(self,newsal):
        self.empsal+=newsal
        return self.empsal
obj1=A('san',33,5000)
obj2=A('tan',32,25000)
obj3=A('jai',32,50500)
print(obj1.empsal)
print(obj3.empname)
res=obj2.displaysal()
print(res,'asdfghjkl;')
print(obj3.empname)
obj3.changename('vikas')
print(obj3.empname)
res=A.C1(10,20)
print(res)
res=A.C2('sandy')
print(res)
print(obj1.empsal)
obj1.incrementsal(20000)
print(obj1.empsal)
print(A.count)
#A.B1()
res=A.C1(10,20)
print(res)
res=B.C1(10,20)
print(res)
A._B1()
