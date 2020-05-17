"""n=5
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
#2.
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    
    print()
#3.
n=5
for i in range(0,n):
    for j in range(n,0,-1):
        print("*",end=" ")
    print()
    n-=1"""
#4.
for i in range(7):
    for j in range(6):
        if ((i==0 or i==6) and (j!=5)) or 
