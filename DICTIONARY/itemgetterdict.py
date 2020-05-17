x={'a':4,'b':2,'c':7,'d':-9,'e':.1}
y=sorted(x.items(),key=lambda x: x[1])
print(y)
###########################
import operator
z=sorted(x.items(),key=operator.itemgetter(1))
print(z)
