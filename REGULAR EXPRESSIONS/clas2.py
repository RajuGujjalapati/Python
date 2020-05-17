import re
var='''ABC dob is 17.05.1997
       XYZ dob is 02-02-1997
       EFG dob is 30:05:1992'''
pat1='[A-Z]{2,}'
pat2='[0-9]{2}[^A-Za-z0-9][0-9]{2}[^A-Za-z0-9][0-9]{4}'

pat=pat1+'|'+pat2
res=re.findall(pat,var)
print(res)
res=re.sub(pat,"SANDY",var)#use 'dob' or pat1 or pat2 at (o) index.
print(res)
