import os
import shutil
src=r'C:\Users\New\OneDrive\Desktop/zil';
des=r'C:\Users\New\OneDrive\Desktop/bil';
files=os.listdir(src)
for f in files:
    shutil.move(src+'\\'+f,des)
