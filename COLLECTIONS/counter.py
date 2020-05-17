#counts the number of values present
from collections import Counter
a=[1,2,1,2,3,4,3,4,55,4,4,3,3,3,6,7,6,7,8,8,9,9]
c=Counter(a)
print(c)
print(list(c.elements()))#writes the whole list in sorting order.
print(c.most_common())
sub={2:2,3:1}#subtracting '2' for '2' times then '3' for '1' time.
print(c.subtract(sub))

print(c.most_common())
