class Computer:
    def __init__(self,proc,ram):
        self.proc=proc
        self.ram=ram
    def config(self):
        print("config is", self.proc, self.ram)
com1=Computer('i5',16)
com2=Computer('ryzen 3',8)
print(com1,'\n',com2)
com1.config()#method calling
com2.config()#method calling
#constructor
#self
#EVERY CLASS HAS AN OBJECT,CLASS IS A BLUE PRINT OF OBJECT.
class Raju:
    
    def __init__(self):
        self.name="RAJU"
        self.age=22
    def update(self):
        self.age=30


c1=Raju()#heap memory
c2=Raju()#rAJU() IS A CONSTRUCTOR BY USING __INIT__ METHOD
print(id(c1))#THE SIZE OF THE MEMORY WII BE DEPENDS ION THE
#NUMBER/SIZE OF VARIABLES WE HAVE CREATED.

print(id(c2))
c1.name="mamatha"
c1.age=25
print(c1.name)
print(c2.name)
c1.update()
print(c1.age)
print(c2.age)


