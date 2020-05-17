import operator
def item_ope():
    
    s=['h','e','l','l','o']
    print(operator.getitem(s,1))
    print(operator.itemgetter(1,4)(s))
    inventory=[('apple',3),('banana',2),('pear',5),('orange',1)]
    get_count=operator.itemgetter(1)
   # print(list(map(get_count,inventory)))
    print(sorted(inventory,key=get_count))
    print(str(s))
    print(len(s))
    print(type(s))


item_ope()
def dict_sort_by_value():
    dict_num={'first':11,'second':3,'third':44,'four':67}
    print(dict_num.keys())
    print(type(dict_num))
    print(dict_num.values())
    sorted_val=sorted(dict_num.items(),key=operator.itemgetter(1))
    print(sorted_val)
    sorted_key=sorted(dict_num.items(),key=operator.itemgetter(0))
    print(sorted_key)

dict_sort_by_value()
