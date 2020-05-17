f=open(r'C:\Users\New\OneDrive\Desktop/data.txt','r')
data=f.readlines()
#data.sort()
#print(data)

dup=[]
allemp=[]
for x in data:
    if (x not in allemp):
        allemp.append(x)
allemp.sort()
print(allemp)
        
for z in allemp:
    a=z.split('#')[::-1]
    z.split(',')
    print(z)
    print(a)
    
'''for i in data:
    re=i.split('#')
    print(re)
'''
