
#try:
  #  file=open(r'C:\Users\New\OneDrive\Desktop\PYTHON\PYTHON CLASS\ra.txt','w')
  #  file.write("this the file i created using try and exception blocks,is this updated?")
#except FileNotFoundError:
  #  print("Create the file!")
#except :
   # print("this is another error")

#else:
#    print("created!")
#finally:
   # file.close()"""
def functionName(level):
    if level < 1:
        raise Exception(level)
    return level
 
try:
    l=functionName(10)
    print ("level=",l)
except Exception as e:
    print ("error in level argument",e.args[0]) 
