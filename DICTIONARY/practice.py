dict={'name':'raju','age':22,'sex':'male','cast':'bc'}
print("name is:",dict['name'])
print(dict)
#we can update the dictioanry  values by addding a new entry with the same key value
dict['age']=23
print(dict['age'])
dict2={('raju'):"king"}
print(dict2)
rs=dict.get('name','na')
print(rs)
#get:if it is present it shows ,if not, it shows 'na'
print(dict)
#setdefault
res=dict.setdefault('x','inserting')
print(res)
print(dict)
#assigning d1,d2 to d3
dict3={}
dict3.update(dict)
dict3.update(dict2)
print(dict3)
dict['sex']='changed'
print(dict)
dict3=dict.copy()
print(dict3)
print(str(dict))
print(dict.keys())
print(dict.items())
#tuple pairs
print(dict.values())
print(dict.fromkeys('n'))
for x in dict:
    print(x)
x={'name':'raju','age':22,'sex':'male','cast':'bc'}
y={'sam':'dad','asd':'dada'}
for z in x:
    print(dict[z])
print()
for x,y in dict.items():
    print(x,"",y)
####
if 'name' in dict:
    print("yes,it has"":::")
    ##to know the length
print(len(dict))
#thisdict=dict(brand="Ford", model="Mustang", year=1964)
#print(thisdict)
#thisdict1=dict.fromkeys(thisdict)###########

#print(thisdict1)
dict.pop("name")
print(dict)
#deletes the required item########
dict.popitem()
print(dict)
#popitem deletes the last item##########
for x in dict:
    print(dict[x])
#prints only values in dict#######
for x in dict:
    print(x)

#############add the values to the dict#########################
dict["king"]="raju"
print(dict)









