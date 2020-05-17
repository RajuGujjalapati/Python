def gen(file,x,y):
    try:
        fvar=open(file,'r')
        yield "FILEFOUND"
    except FileNotFoundError as err:
        yield "NOFILE"
    res1=x+y
    yield res1
    res2=x**y
    yield res2
    if(x>y):
        yield 'X'
    else:
        yield 'Y'
        
op=gen("abc.txt",60,20)


#print(next(op))
#print(type(op))
#res=list(op)
#print(res)#add to program after seeing the one output'
op1=next(op)
if (op1=="FILEFOUND"):
    print("file is present calling second return")
    op2=next(op)
    if (op2>50):
        print("calling third return")
        op3=next(op)
        op4=next(op)
        if (op4=='X'):
            print("X is greater")
        else:
            print("Y is greater")
    else:
        print("stopped at second return")
else:
    print("file is not present")
#generators are noraml func which can return multiple time
#yield 


