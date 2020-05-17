#API:application program interface;open pyxl is the module which connects the program with API
#openpyxl
#from openpyxl import load_workbook
from openpyxl import Workbook
print("complete")
myexcel = Workbook()
mysheet =myexcel.active
mysheet['A1'] = "name"
mysheet['B1'] = "age"
mysheet['C1'] = "salary"
#myexcel.save(r'D:\script\test.xlsx')
n = ['a','b','c','d','e','f','g','h']
a= [25,28,31,26,33,24,25,24]
s=[200,1000,50,100,275,350,475,600]
rows = len(n)
startpos = 2
listindex = 0
while(rows!=0):
     namestr = 'A'+str(startpos)#A2
     agestr = 'B'+str(startpos)#B2,B3
     salstr  = 'C'+str(startpos)

     mysheet[namestr] = n[listindex]
     mysheet[agestr]  = a[listindex]
     mysheet[salstr]  = s[listindex]
     rows-=1
     startpos+=1
     listindex+=1

myexcel.save(r'C:\Users\New\OneDrive\Desktop\PYTHON\test.xlsx') 
