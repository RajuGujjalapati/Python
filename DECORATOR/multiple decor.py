def upper_d(func1):
    def inner():
        str1=func1()
        return str1.upper()
    return inner
def split_d(func2):
    def wrapper():
        str2=func2()
        return str2.split()
    return wrapper
@split_d
@upper_d
def ordinary():
    return "good morning"
print(ordinary())





#2.
import functools
def decorator(func):
    @functools.wraps(func)
    def inner():
        strl=func()
        return func().upper()
    return inner
@decorator
def greet():
    return "good evening"
print(greet.__name__)#It will prints the 'inner' - means it is hiding the data of
#original function(greet)
#to get the original function name import functools and follow as regards.
#it copy the orginal function name and prints
print(greet())
