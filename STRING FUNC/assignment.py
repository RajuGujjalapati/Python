stat = input("Please enter the statement that you want to check: ")
word = input("Please enter the word to check in the statement: ")
n = 0
i = 0
j = 0

if word in stat:
	while i!= -1:
		i = stat.find(word, n, len(stat))
		n = (i + 1)
		if (stat.find(word, n, len(stat))) != -1:
			j +=1

	print (f"{word} is present {j} times in the provided statement.")

else:
	print (f"{word} is not present in the provided statement.")
