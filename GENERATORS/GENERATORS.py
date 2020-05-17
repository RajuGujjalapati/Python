def test(x,y):
    res=x+y
    return res,x,y,True#whatever we do, oncew we write the return keyword the
#it wont allow to execte other return statements.
    return x
    return y
op=test(20,50)
print(op)

##my code
def test(x,y):
    res=x+y
    yield res,x,y,True
    yield x
    yield y
print(test(20,40))
############youtube corey schafer
nums=[1,2,3]
i_nums=iter(nums)
while True:
    try:
        item=next(i_nums)
        print(item)
    except StopIteration:
        break
###########another
def my_range(start,end):
    current=start
    while current<end:
        yield current
        #return current#if we use 'return' then this return just '1' time.
        #return stops there and if we try to loop it shows error
        #but yield store in memory
        #and continuous where it left offf!.
        current+=1
nums=my_range(1,10)
for i in nums:
    print(nums)
class my_gen:
    def __init__(self,start,end):
        self.value=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value>=self.end:
            raise StopIteration
        current=self.value
        self.value+=1
        return current
nums=my_gen(1,10)
print(next(nums))
        
