'''import pymysql as p
db = p.connect('127.0.0.0','root','root','world')
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


##### insert query

q1 = "INSERT INTO city (ID, NAME, CountryCode, District, Population) VALUES (4157, 'SHEKAR', 'AFG', 'SHEKAR', 7776667);"
mycursor.execute(q1)
db.commit()#save #.rollback
db.close()
'''
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
