def numgen(n):
    if n<20:
        number=0
        while number<n:
            yield number
            number+=1
    else:
        return "this is return"
mygen=numgen(7)
print(mygen)
counter=0
while counter<10:
    print(next(mygen))
    counter+=1
    print(next(mygen))
    print(next(mygen))
    print(next(mygen))
