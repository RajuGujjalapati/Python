import numpy as np
my_list=[[10,20,30],[40,50,60],[70,80,90]]
matrix=np.array(my_list)
print("Elements:")
print(matrix)
for ele in matrix:
    #print(ele)
    for element in ele:
        print(element, end='  ')
    print()
#in the fisrt for loop it iterates through the double list.
    #in 2nd for loop it iterates through the 2nd for loop.
#then it printsbina good manner.
    
