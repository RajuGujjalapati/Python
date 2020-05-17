statement=input("enter the statement you want:")
word=input("enter the word you want to check:")
a,b,c=0,0,0
while a!=-1:
        a=statement.find(word,c,len(statement))
        c=a+1
        if statement.find(word,c,len(statement))!=-1:
           b+=1
        print("word is present in",b,"times in statement")
else:
        print('try again')
           
