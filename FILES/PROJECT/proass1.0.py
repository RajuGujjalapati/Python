fvar=open(r'C:\Users\New\OneDrive\Desktop\Python_assignments\Python_Assignment_1\data.txt','r')
data=fvar.readlines()
data.sort()
print(data)
print()
dup=[]                                           #print(data[::-1])
allemp=[]
uniq=[]
for x in data:
    if(x not in allemp):
        allemp.append(x)
#use print(x) function for all the values
        #the below code helps you to get the data without("#") and also takes salary from back to front. 
        print(x.split("#")[::-1])
        
#the duplicate lines like which are appearing only more than once
for x in data:
    if(data.count(x))>1 and x not in dup:
        dup.append(x)
        print(x)
#from here the unique files created which are appearing only once.
for x in data:
    if(data.count(x)==1) and x not in uniq:
       uniq.append(x)
       print(x)

        
                

 




