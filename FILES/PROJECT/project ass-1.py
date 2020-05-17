fvar=open(r'C:\Users\New\OneDrive\Desktop\data.txt','r')
data=fvar.readlines()
print(data)
list_set=set(data)
unique_list=(list(list_set))
fvar.close()
i=0
for x in unique_list:
    #temp=x.lower()
    #res=temp.startswith("sandy")
    #if (res==True):
        print(x)
        i=i+1
#whenever iam using list_set and unique_list ,iam getting all the values without repetition,eventhough the output may differs from each
        #whenever i am using "data" in for loop iam getting all the values even with repetitio
