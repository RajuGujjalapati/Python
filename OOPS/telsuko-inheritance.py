class A:
    def feautre1(self):
        print("feautre 1 in A")
    def feautre2(self):
        print("feautre 2 in A")
class B(A):
    def feautre3(self):
        print("feautre 3 in B")
    def feautre4(self):
        print("feautre 4 in B")
a=A()
class C(B):#multilevel inheritance
    def feautre5(self):
        print("feautre 5 in c")
class D(C,B,A):#multiple inheritance
    def feautre6(self):
        print("feautre 6 in D")
b=B()
#b.feautre3()
b.feautre4()
b.feautre1()
b.feautre2()
c=D()
c.feautre6()
c.feautre5()
c.feautre4()
c.feautre3()
