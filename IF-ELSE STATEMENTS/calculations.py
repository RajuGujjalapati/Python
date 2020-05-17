
num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))
operation = input("Please enter the option: \n1 for Addition\n2 for Substraction\n3 for Multiplication\n4 for Division\n")

if operation == "1":
	print ("Addition of", str(num_1), "and", str(num_2), "is :", str(num_1 + num_2))
elif operation == "2":
	print ("Substraction of", str(num_1), "and", str(num_2), "is :", str(num_1 - num_2))
elif operation == "3":
	print ("Multiplication of", str(num_1), "and", str(num_2), "is :", str(num_1 * num_2))
elif operation == "4" and num_1 != 0:
	print ("Division of", str(num_1), "and", str(num_2), "is :", str(num_1 / num_2))
elif operation == "4" and num_1 == 0:
	print ("You can't have the first number as 0 in division.")
else:
	print("Invalid option.")
