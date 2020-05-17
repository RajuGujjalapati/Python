fvar=open(r'C:\Users\New\OneDrive\Desktop\data.txt','r')
data=fvar.readlines()
print(data)
fvar.close()
i=0
for x in data:
    temp=x.upper()
    res=temp.startswith("INDIA")
    if (res==True ):
        print(x)
        i+=1
        
"""for y in data:
                    temp=y.upper()
                    res1=temp.startswith("USA")
                    if (res1==True):
                        print(y)
                    i-=1
                    while i>=0:
                            for z in data:
                                temp=z.upper()
                                res2=temp.startswith("Uk")
                                if (res2==True):
                                    print(z)
                                    i-=1"""
        
        
    
    
    
