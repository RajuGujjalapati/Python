fvar=open(r'C:\Users\New\OneDrive\Desktop\data.txt','r')
data=fvar.readlines()
print(data)
fvar.close()
i=0
for x in data:
    temp=x.lower()
    res=temp.startswith("sandy")
    if (res==True):
        print(x)
        i=i+1
    


#fout(\\\\a)
#temp=x.split("#")
#temp[-1]=opfout.append(op)
        


