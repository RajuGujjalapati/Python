import random
res=random.randrange(1000,9999999)
print(res)
res1=random.random()
print(res1)
res2=int(random.uniform(1,10))
print(res2)
res3=random.randrange(1,4)
print(res3)
import random

mylist = [1,4,67,6]

print(random.choices(mylist, weights = [3,4,3,5], k = 14))
