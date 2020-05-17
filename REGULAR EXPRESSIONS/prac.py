#sun just replaces only two white spaces
str = "The rain in Spain"
import re
x = re.sub("\s",'9', str,2)
print(x)
########################
import re
var="raju 32"
res=re.findall('[a-z0-9]',var)
print(res)

import re
var='!@#$%^&*()'
res=re.findall('[^A-Za-z0-9]',var)
print(res)

var='ASDERahjsidk 485294758924592'
res=re.findall('[a-z]{1,}',var)
res1=re.findall('[A-Za-z0-9]{1,}',var)
print(res+res1)
'''*******************************
'''
#THE DOT
import re
str='hello world'
x=re.findall('he..o',str)
print(x)

# + and *
str='the rain falls in spain which gains heavy rain'
x=re.findall('aix*',str)
x1=re.findall('aix+',str)
print(x,'\n',x1)
    
str1='sdahjfakjbfdfjz$%%^'
x=re.findall('[a-z]*',str1)
print(x)


#Split at empty spaces.


str = "The rain in Spain"
x = re.split(" ", str)
print(x)


#at only one occurence.

str = "The rain in Spain"
x = re.split("\s", str,2)
print(x)

