#chainmap is a dictionary like class for creating a single view of multiple mappings.
from collections import ChainMap
a={1:"gujjalapati",2:"raju"}
b={3:"kumar",4:"naidu"}
a1=ChainMap(a,b)
print(a1)
c={}
c.update(a)
c.update(b)
print(c)
di={1:4}
chain1=chain.new_child(di)
print(chain1)
