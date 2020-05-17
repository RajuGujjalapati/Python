result_str="";    
for row in range(0,5):    
    for col in range(0,5):     
        if (col==0 or (row==0 or row==4)) or (row==2 and (col==3 or col==4)) or (col==4 and (row>2 and row<5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
