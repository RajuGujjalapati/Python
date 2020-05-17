#the actual working process for recursion
def fact5():
    return 5*fact4()
def fact4():
    return 4*fact3()
def fact3():
    return 3*fact2()
def fact2():
    return 2*fact1()
def fact1():
    return 1
print(fact5())
#2.
def recursion(n):
    if n==1:
        return 1
    return n*recursion(n-1)
print(recursion(10))
#3.
def rev(n):
    if len(n)==0:
        return []
    return n[-1:]+rev(n[:-1])
print(rev([1,2,3,4,56,7]))
