start_num=int(input("Enter the starting number:"))
end_num=int(input("Enter the end num:"))
for num in range(start_num,end_num+1):
    #print(num)
    if num>1:
        for i in range(2,num):#ikada 2 %3 in first step ,so i=2 and num=3
            #so, it prints 2 as prime
            if (num%i)==0:
                break
        else:
            print(num, 'is \"kaju" prime')
