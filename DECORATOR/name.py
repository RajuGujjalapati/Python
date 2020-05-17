class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@gmail.com'
        #self.first='raju'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
emp_1=Employee('john','smith')
emp_2=Employee('raju','bujji')
print(emp_1.first)

print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname())

print(emp_2.first)
print(emp_2.last)

