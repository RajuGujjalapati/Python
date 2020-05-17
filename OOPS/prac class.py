class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print("hello this is:"+self.name)
p1=person("john",23)
p1.myfun()
print(p1.name)
#print(p1.name)
#print(p1.age)
    

#2.
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(mysillyobject):
    print("Hello my name is " + p1.name)

p1 = Person("John", 36)
p1.myfunc() 
