number=int(input("Enter the value that you want to check for factorial::>"))
factorial=1
while number>=1:
    factorial=factorial*number
    number=number-1
    if number==0:
        pass
print(factorial)
