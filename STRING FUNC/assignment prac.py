var="python is easy and python is a good language so python is good for basic learners"
n=0
while n<=1:
    res=var.find('python',n,len(var))
    n=n+1
    print(res)
    if res>=0:
        res1=var.find('python',n,len(var))
        n=n+1
        print(res1)
        if res1>=res:
            res2=var.find("python",n,len(var))
            print(res2)
