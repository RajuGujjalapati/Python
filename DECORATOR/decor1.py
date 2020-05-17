1.
def function1():
    print("Hi iam function1")
def function2(func):
    print("Hi i am function 2 calling function1")
    func()
function2(function1)
2.
def str_upper(func):
    def inner():
        str1=func()    
        return str1.upper()
    return inner
def print_str():
    return "good morning"
print(print_str())
d=str_upper(print_str)
print(d())
3.
def str_upper(func):
    def inner():     
        str1=func()    
        return str1.upper()
    return inner
@str_upper 
def print_str():
    return "good morning"
print(print_str())
