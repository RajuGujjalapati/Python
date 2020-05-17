fvar=open(r'C:\Users\New\OneDrive\Desktop\data.txt','r')
data=fvar.readlines()
print(len(data))
print(data[0])
fvar.close()
i=0
repeated=[]
for i in range(len(data)):
    k=i+1
    for j in range(k,len(data)):
        if data[i]==data[j] and data[i] not in repeated:
            repeated.append(data[i])
            print()
            print(repeated)
            print()
    '''temp=fvar.lower()
    res=temp.startswith("sandy")
    if (res==True):
        print(res)
        i=i+1
    '''

