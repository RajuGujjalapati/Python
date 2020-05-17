fvar=open(r'C:\Users\New\OneDrive\Desktop\data.txt','r')
data=fvar.readlines()
print(data)
list_set=set(data)
unique_list=(list(list_set))
fvar.close()
i=0
max=0
for x in unique_list:
    #temp=x.lower()
    #res=temp.startswith("sandy")
    #if (res==True):
        #print(x)
        raj=int(unique_list.split('#')[0])
        if (max<raj):
            max=num
print(max)
i=i+1
