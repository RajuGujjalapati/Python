import re
var='today we have python class i like python'
res=re.search('python',var)
res1=re.findall('python',var)
res2=re.sub('python','java',var)
print(res)
print(res1)
print(res2)
#re.match()
#regular expressions only deaals with strings
#re.search:-search the words anywhere in the string.
#re.findall:-finds all variables in list format.
#re.sub:-replace one variable with other.syn:-re.sub('required var','changing var',var)
var="my old mobile number is 7348593096 & 9043493949 & 8549939459"
import re
res=re.findall('7[0-9]{9}' , var)#pattern matching
print(res)


var="my old mobile number is +91-7348593096 & +12-9043493949 & oun-8549939459"
import re
res=re.findall('[+]91-[0-9]{10}' , var)#pattern matching
print(res)
import re

var="""INDIA ip is 1.2.133.14
        USA ip is 124.168.3.144
        UK ip is 166.1.138.1"""
pat1='[A-Z]{2,}'
pat2='[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}'
'''c=re.findall(pat1,var)
print(c)
i=re.findall(pat2,var)
print(i)'''
pat=pat1+'|'+pat2#concatination
res=re.findall(pat,var)
print(res)

##############
import re
pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
password =input("Enter string to test: ")
result = re.findall(pattern, password)
if (result):
    print ("Valid password")
else:
    print ("Password not valid")

