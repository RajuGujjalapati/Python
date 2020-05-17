class Car:
    def __init__(self):
        self.__updating()
    def drive(self):
        print("driving")
    def __updating(self):
        print("updating software")
obj=Car()
obj.drive()
#obj.__updating()
#if we use above line, it shows error because we can't acces it outside of class
##############################
##private variables#########
'''private variables only modifies only inside the class method.
  we cant modify the private variables outside the class method'''
class Car:
    __maxspeed=0
    __name=""
    
    def __init__(self):
        self.__maxspeed=200#modifying to 200
        self.__name="supercar"
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed=speed
        print(self.__maxspeed)
        
obj=Car()
obj.drive()
obj.setspeed(100)
 
