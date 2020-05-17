bad_char=[';',':','!','@','*']
test_string = "Ge;ek * s:fo ! r;Ge * e*k:s !"
for i in bad_char:
    test_string=test_string.replace(i,'')
print("Resultent list is:"+str(test_string))
string=test_string.replace(' ','')
print(string)
stri="fg!,@#poj^,&*lk$%^"
bad=['@',"#","^","!","&","%"]
stri=stri.join(bad)
print(stri)
     
#for i in badchar:
