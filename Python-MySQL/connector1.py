#connector
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="app200905",
  database="python1"
)

m = mydb.cursor()

a=int(input("Enter the id:"))
b=input("Enter the name:")
c=input("Enter the last name:")
d=input("Working:")
'''
q = "insert into py1 values('"+str(a)+"','"+b+"','"+c+"','"+d+"')"
print(q)
m.execute(q)
mydb.commit()
'''
q="select * from py1"
m.execute(q)
z=m.fetchall()
print(z)