'''To calculate the standard deviation of those numbers:
Work out the Mean (the simple average of the numbers)
Then for each number: subtract the Mean and square the result.
Then work out the mean of those squared differences.
Take the square root of that and we are done!'''
import numpy as pd
data=[1,23,4,343,545,4556,76,45,34,34]
res=pd.std(data)
res1=pd.mean(data)
#VARIANCE
res2=pd.var(data)
print(res)
print(res1)
print(res2)

