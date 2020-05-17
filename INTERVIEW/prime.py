num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):
       print(i)
       if (num % i) == 0:  #at any cost the num divisible by in the range of 2 to somethoing
           #then it is not prime'.
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")
start=1
end=20
for val in range(start,end+1): 
   if val>1:
      for n in range(2,val):
         print(n,end=',')
      print()
'''         if val%n==0:
            break
      else:
         print(val ,'is a prime number')'''
