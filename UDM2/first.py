def createfiles(*files):
    for x in files:
        fvar=open(x,'w')
        fvar.close()
        print("created",x)
#createfiles('a.py','b.txt','c.txt')
def reversestr(x):
    return x[::-1]
#res=reversestr("sandy")
#print(res)
