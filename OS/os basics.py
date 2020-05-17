from os import listdir,walk
from stat import *
#cwd=os.getcwd()
#print(cwd)
#o=os.chflags(r"C:\Users\New\OneDrive\Desktop/data.txt", stat.UF_NODUMP)
#print(o)
from os.path import isfile, join
mypath=r'C:\Users\New\OneDrive\Desktop\PYTHON\MY PYTHON'
f=[]
onlyfiles=[f for f in listdir(mypath)]
print(str(onlyfiles))
                                                

#for d,e,f in walk(mypath):
    


for f2 in onlyfiles:
    
    #f2=onlyfiles.split(',')
    print(f2)
