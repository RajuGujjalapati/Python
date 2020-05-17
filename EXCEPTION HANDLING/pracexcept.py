try:
    fi=open(r'C:/desktop\raju.text','r')
    print("YHH! try is executed")
except Exception as err:
    fi=open(r'C:\Users\New\OneDrive\Desktop\PYTHON\PYTHON CLASS\EXCEPTION HANDLING/nani.txt','w')
    fi.write("i'am writing something new on this file")
    fi.close()
    print("file created!")
    print(err)
else:
    print("let's see its executed or not")
finally:
    print("whatever it is the final block will execute")
