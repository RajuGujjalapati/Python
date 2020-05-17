import os
os.chdir(r'C:/Users/New/OneDrive/Desktop/PYTHON')
for f in os.listdir():
     file_ext=f.split('.')
     print(file_ext)
     #f.strip()removes spaces[1:].zfill(2)#2 represents no. of pace holders #zerofills
     #if u wanrt to eliminate any kind of num or str in a name use [1:]or as per
     #the reqirement
     #
