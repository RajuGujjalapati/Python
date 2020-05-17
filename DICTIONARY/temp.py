strr="hello hello, welcome welcome to python.advance.projects\
        and start learning python"
words=strr.split()
d={}.fromkeys(words,0)
print(d)
for w in words:
    d[w]+=1
    print(d)
