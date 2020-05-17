mark = int(input("Please enter the mark of the student: "))

if 1 <= mark < 35:
	print ("The student has failed.")
elif 35 <= mark < 50:
	print ("Third Class")
elif 50 <= mark < 60:
	print ("Second Class")
elif 60 <= mark < 85:
	print ("First Class")
elif 85 <= mark <= 100:
	print ("Excellent")
else:
	print ("Input mark should be between 0 to 100.")
