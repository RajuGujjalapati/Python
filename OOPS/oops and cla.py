'''class A:
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
print(res)
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
#print(obj2.empname)
#stores input info. =method.
#object goes and calls inside func., but normal func. could't.
#__int__ acts as constructor.It stores the data in the object.
#object is an dynamic program or real-time programming.'''

class Z:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.d=x+y
    def add(self):
        return self.d
    def change(self,z):
        self.y=z
a=Z(6,8)
b=Z(3,5)
c=Z(5,5)
res=a.add()
print(res)
print(b.add())
b.change(7)
print(b.y)
print(b.add())
class A(Z):
    
