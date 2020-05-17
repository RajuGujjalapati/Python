name="python"
def test(y,x=50,z=7):
    print(x)
    print(y)
    print(z)
    res=x+y+z
    print("name is",name)
    global age
    age=30
    return res #true
op=test(2,4,5)
print(op)
print("age is:",age)
def test(x,y,*z,a=50):
    print(x)
    print(y)
    print(z)
    print(a)
test(2,4,6,8,10,12,14,16)
def ttry(*x,f=9):
    print(x)
    print(f)
op=ttry(2,[3,4,6,7,8,8])
print(op)

