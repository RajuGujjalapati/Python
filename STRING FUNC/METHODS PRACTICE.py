a="                          HELLO,,,,,, worLD                     "
print(a.strip())#removes the space at front and back of the string not in between
print(a)
print(a.lower())
print(a.upper())
print(a.replace("H","j"))
print(a.split())#split method splits the string into substring
#concatenation
a="hello"
b="world"
c=a+"                       "+b
print(c)
age=36
txt="My name is jhon,I am {}"#format function appends data
print(txt.format(age))
quan=3
itemno=567
price="american" 
myorder="I want {} pieces of item {} for {} dollars"
print(myorder.format(quan,itemno,price))
myorder="I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quan,itemno,price))
#JOIN METHOD
mytuple=("raju","bujji","gajji")
print("#".join(mytuple))#joins ash here one after another
myDict = {"name": "John", "country": "Norway","jimpak":"jam"}
mySeparator = "  test  "

x = mySeparator.join(myDict)

print(x)
txt = "banana"

x = txt.center(20,"#")

print(x, "is my favorite fruit.")
y=txt.count(a)
print(y)

