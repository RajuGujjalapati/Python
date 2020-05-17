import time
import threading
import os


def square(num):
    for i in num:
        time.sleep(0.5)
        print("square : " , i*i)


def cube(num1):
    for x in num1:
        time.sleep(0.2)
        print("cube : " , x*x*x)


L1 = [2,3,4,5]
t = time.time()
'''
square(arr)
cube(arr)

'''

t1 = threading.Thread(target=square, args=(L1,))
t2 = threading.Thread(target=cube, args=(L1,))

t1.start()
t2.start()

t1.join()
t2.join()


print(" Completed in :", time.time()-t)
