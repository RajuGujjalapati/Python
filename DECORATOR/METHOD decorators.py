def check_name(method):
    def inner(name_ref):
        
        if name_ref.name=="RAJU":
            print("Hey my name is also same!!!")
        else:
            method(name_ref)
    return inner
def another(func ):
    def ano(names):
        print(names.name.lower())
    return ano
class printing:
    def __init__(self,name):
        self.name=name
    
    @check_name
    @another
    
    def print_name(self):
        print(self.name)
obj=printing("KING")
obj.print_name()




#2.
def check_name(method):
    def inner(name_ref):
        if name_ref.name=="RAJU":
            print("Hey my name is also same!!!")
        else:
            method(name_ref)
    return inner

class printing:
    def __init__(self,name):
        self.name=name
    
    @check_name
    
    def print_name(self):
        print("Entered name is:",self.name)
obj=printing("RAJU")
obj.print_name()


#3.
 
