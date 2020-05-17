'''def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-2)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(5)
#a func calling itself


import sys
sys.setrecursionlimit()#using 
print(sys.getrecursionlimit())'''
i=0
def greet():
    global i
    i+=1
    print("Hello",i)
    greet()
greet()
#Function to print factorial
'''def fact(n):
    if (n==0):
        return 1

    return n*fact(n-1)


result=fact(5)
print(result)'''
    
