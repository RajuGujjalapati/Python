''''def recu(n):
    if (n==1):
        return 1
    else:
        return n*recu(n-1)
print(recu(5))'''
########
def fn(x,y):
    if (x==0):
        return y
    else:
        return fn(x-1,x+y)#x=3(4-1)at 1st iteration, x=2 at 2nd , x=1 at 3rd
print(fn(4,2))
#####
def sum1(n):
    if n==1:
        return 1
    else:
        return pow(n,n)+sum1(n-1)
print(sum1(4))
###
def lis(n):
    if len(n)==0:
        return []
    else:
        return n[-1:]+lis(n[:-1])
print(lis([1,2,4,5,6]))
