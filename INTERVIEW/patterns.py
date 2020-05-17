for i in range(7):
    for j in range(7):
        if (i+j==3)or (i-j==3 and i>=3)or (i==1 and j>=4) or (i+j==9 and i<=6):
            print("*",end="")
            
        else:
            print(end=" ")
    print()
            
