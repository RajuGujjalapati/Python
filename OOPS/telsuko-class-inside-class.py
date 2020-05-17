class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name, self. rollno)
        self.lap.show1()#show1 calling 
    
    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8
        def show1(self):
            print(self.brand, self.cpu, self.ram)
s1=Student("raju",5)
s2=Student("priya",4)
print(s1.name)
print(s2.name)
print(s1.show())#prints s1 object 'raju 5 and hp i5 and 8 ' also'.
#because i am calling the 
lap1=Student.Laptop()
print(lap1.brand)
