#crud operation using MySQL
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="app200905",
  database="crud1"
)

m = mydb.cursor()

while True:
    print("Enter 1. Add Product")
    print("Enter 2. Remove Product")
    print("Enter 3. Update Product")
    print("Enter 4. Display Product")
    print("Enter 0. Exit")
    ch=int(input("Enter your choice:"))
    
    if ch!=0:
        if ch==1:
            id=int(input("ID:"))
            name=input("Name:")
            category=input("Category:")
            price=int(input("Price:"))
            
            q="insert into product values('"+str(id)+"','"+name+"','"+category+"','"+str(price)+"')"
            m.execute(q)
            mydb.commit()
        elif ch==2:
            id=int(input("ID:"))
            
            q="delete from product where id='"+str(id)+"'"
            m.execute(q)
            mydb.commit()
        elif ch==3:
            id=int(input("ID:"))
            
            q="delete from product where id='"+str(id)+"'"
            m.execute(q)
            mydb.commit()
            
            print("||Enter new Data||")
            id=int(input("ID:"))
            name=input("Name:")
            category=input("Category:")
            price=int(input("Price:"))
            
            p="insert into product values('"+str(id)+"','"+name+"','"+category+"','"+str(price)+"')"
            m.execute(p)
            mydb.commit()
        elif ch==4:
            q="select * from product"
            m.execute(q)
            z=m.fetchall()
            for i in z:
                print("ID:",i[0])
                print("Name:",i[1])
                print("Category:",i[2])
                print("Price:",i[3])
        else:
            print("Invalid choice")
    else:
        print("Thank You!!!")
        break