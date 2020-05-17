import os
res=os.access(r'C:\Users\New\OneDrive\Desktop',os.F_OK)
print(res)
#to check whether file is exisiting or not.
res=os.access(r'C:\Users\New\OneDrive\Desktop',os.R_OK)
print(res)
res=os.access(r'C:\Users\New\OneDrive\Desktop',os.W_OK)
print(res)
res=os.access(r'C:\Users\New\OneDrive\Desktop',os.X_OK)
print(res)
res=os.getcwd()#current path
print(res)
#os.chdir(r'C:/W3RESOURCE')#to changee the path
#os.chroot(r'path')
res=os.environ
print(res)
res=os.getenv('APPDATA')#environment variable
print(res)
#res=os.remove(r'C:\Users\New\OneDrive\Desktop\PYTHON\PYTHON CLASS')
print(res)
#os.mkdir(r'C:/PYTON/DESKTOP/RAJU')
#CREATES NEW PATH
#os.mkdir(r'C:\Users\New\OneDrive\Desktop\TELUSKO/A,B')
#os.rename(r'C:\Users\New\OneDrive\Desktop\TELUSKO/A,B',r'C:\Users\New\OneDrive\Desktop\TELUSKO/C')
res=os.stat(r'C:\Users\New\OneDrive\Desktop\TELUSKO/C')
print(res)
import shutil
dir (shutil)
res=shutil.copy(r'C:\Users\New\OneDrive\Desktop\TELUSKO/C',r'C:\Users\New\OneDrive\Desktop\PYTHON/XYZ')
print(res)

import os
os.system('mstsc')
