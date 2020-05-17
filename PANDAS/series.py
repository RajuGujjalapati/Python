import pandas as pd
import numpy as np
info=np.array(['p','a','n','d','a','s'])
print(info)
a=pd.Series(info)
print(a)
re=pd.read_table(r'C:\Users\New\OneDrive\Desktop/data.txt',sep='#')
re1=pd.read_csv(r'C:\Users\New\OneDrive\Desktop/data.txt',sep='#')
#for csv file the default seperator is ','.


###if we doesn't have headers then add "header=None"
#then it shows the headers in numbers.
#If you want to add good details in headers then create a list with suitable names
#then add "names='list_var'" then it fits in header perfectly!.
#bit.ly url for data
print(re)

a=re1.Name
print(a)
import pandas as pd
ayee=pd.read_table('http://c.mymovies.dk/lacherish/title:asc')
print(ayee)
