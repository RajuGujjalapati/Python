
#default dict isa dictionary subclass ehich calls a factory func. to supply misssing values.
from collections import *   #defaultdict
d=defaultdict(int)
#prints '0' if not find.....prints nothing if use str there
#try to give dict, tuple,str there
d[1]='python'
d[2]='raju'
print(d)
print(d[4])


