def outer():
    msg="hello"
    def inner():
        print(msg)
        print("inner")
        
    return inner
a=outer()
a()
#here we can call outer function variables to inner functions too.
