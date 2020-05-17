import pymysql as p
db = p.connect('localhost','root','SaiKrishna@006','world')
#### ip adress , user , password , schema/ database name 
mycursor = db.cursor()


#### selelect query ....

#q1 = "select * from city where id = 4104;"
q1 = ['select count(*) from city;',"select * from city where id = 4104;"]
data = []
for query in q1:
    mycursor.execute(query)
    d = mycursor.fetchall()
    data.append(d)
db.close()

print(data)

'''

##### insert query

q1 = "INSERT INTO city (ID, NAME, CountryCode, District, Population) VALUES (4157, 'SHEKAR', 'AFG', 'SHEKAR', 7776667);"
mycursor.execute(q1)
db.commit()#save #.rollback
db.close()
'''
