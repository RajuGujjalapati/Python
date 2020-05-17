def marks(p):
    assert p<=100,"out of range"
    print("===>",p)
marks(90)
def passs(p):
    assert len(p)<=12,"password char exceeded"
    print("===>",p)
passs("sandy@123")
'''#3.
def marks(p):
    if (len(p)<8 or len(p)>12):
        raise ValueError("invalid password length")
    else:
        return "success"
op=marks("san")
print(op)

#4.
def marks(p):
    if (len(p)<8 or len(p)>12):
        raise Exception("invalid password length")
    else:
        return "success"
op=marks("san")
print(op)'''
