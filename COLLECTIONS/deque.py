#deque called as 'deck' is an optimised list to perform insertion and deletion easily.
from collections import *
a=['r','a','j','u']
d=deque(a)
print(a)
d.append('py')
print(d)
d.appendleft('pe')
print(d)
d.pop()
print(d)
d.popleft()
print(d)
