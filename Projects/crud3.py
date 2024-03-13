#crud operation using class
user_list=[]
def update():
    old_name=input("Enter the name of the User to Update:")
    for i in user_list:
        if i.name == old_name:
            update_name=input("Enter the name of the NEW User:")
            i.name=update_name
            update_contact=int(input("Enter the contact of the NEW User:"))
            i.contact=update_contact
            update_password=input("Enter the password of the NEW User:")
            i.password=update_password
            print("User Updated Successfully")                
            break
    else:
        print("User name not matched")

def remove():
    remove_name=input("Enter the name of the User to Remove:")
    v=0
    for i in user_list:
        if i.name == remove_name:
            del user_list[v]
            break
        v=v+1
    else:
        print("User name not matched")
        
class User():
    def setdata(obj):
        name=input("Enter name of the User:")
        contact=int(input("Enter the contact of the User:"))
        password=input("Enter password of the User:")
        obj.name=name
        obj.contact=contact
        obj.password=password
        user_list.append(obj)
        print("User Added Successfully")
        
    def __str__(obj):
        print("Name:",obj.name)
        print("Contact:",obj.contact)
        print("Password:",obj.password)
        return " "
        
while True:
    print("---------------------------------------")
    print("| Enter 1. To Create/Add User Details |")
    print("| Enter 2. To Remove User Details     |")
    print("| Enter 3. To Update User Details     |")
    print("| Enter 4. To Display User Details    |")
    print("| Enter 0. To End The Program         |")
    print("---------------------------------------")
    ch=int(input("Enter Your Choice:"))
    
    if ch!=0:
        if ch==1:
            user1=User()
            user1.setdata()
        elif ch==2:
            if len(user_list)!=0:
                remove()
            else:
                print("User not available")
        elif ch==3:
            if len(user_list)!=0:
                update()
            else:
                print("User not available")
        elif ch==4:
            if len(user_list)!=0:
                for i in user_list:
                    print(i)
            else:
                print("User not available")
        else:
            print("Invalid Choice")
    else:
        print("Thank You!!!Byee")
        break