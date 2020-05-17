'''from collections import OrderedDict
#ordered dictionary is dictionary subclass which remembers the order in which the entries were done.
d=OrderedDict()'''
d=dict()
d[0]='r'
d[2]='a'
d[3]='j'
d[4]='u'
print(d)
d[1]='k'
print(d)
#print(d[6])#we get KeyError
