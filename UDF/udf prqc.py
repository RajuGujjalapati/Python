def my_func():
    print("hello from a function")
    #this wont give output beacuse it is defined andd not called
    #we are calling the func in next step
my_func()
#now it is executed
#2.
def my_func(fname):
    print(fname+"raju")
my_func("email")
my_func("gmail")
my_func("king")
#here we are caling the function, the fname returs parameters values as above
#3.
def my_func(country="norway"):
    print("I am from" + country)
my_func("sweden")
my_func("india")
my_func()#this fills the norway
my_func("Brazil")
#4.
def my_func(food):
    for x in food:
        print(x)
fruits=["mango","banana","apple"]
my_func(fruits)
#5.
def my_func(x):
    return 5*x
print(my_func(3))
print(my_func(5))
print(my_func(9))
