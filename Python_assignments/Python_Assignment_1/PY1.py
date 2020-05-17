with open(r'data.txt','r') as re:
    a=re.read()
    
    appending_files=[]
    last=[]
    for i in a:
        if i not in appending_files:
            appending_files.append(i)
            #x=[m.split('\n') for m in appending_files]
            #for n in x:
             #   f=n[0]
            #last.append(f)
            
print(appending_files)
        

