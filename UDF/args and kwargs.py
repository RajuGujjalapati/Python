def myfun(*check):
    for values in check:
        print(values)
    #print(arg)
myfun("hello","hi","raju","how","you","are","doing")
"""def myfunc(*check):
    for i in check:
        return i*10
        print(i)
myfunc(20,40,60)"""
def my_func(**args):
    for key,values in args.items():
        print("%s:%s"%(key,values))
my_func(first='raju',mid='king',of='jungle',pos='raju')
#we can also give an extra parameter in the paranthesis like (arg,**args)

#Here we'r defining two keywords at below
#
def myfun(k,g,f):
    print("k",k)
    print("g",g)
    print("f",f)
args=("raju","rani","kaju")
myfun(*args)
kwa={'k':"raju","g":"king","f":"success"}
myfun(**kwa)

