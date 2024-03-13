dict={"one":"hi","two":"hello","three":7,"four":25,}

while(True):
    print("Enter No.1 to add")
    print("Enter No.2 to pop")
    print("Enter No.3 to popitem")
    print("Enter No.4 to update")
    print("Enter No.5 to display")
    print("Enter No.0 to exit")

    a=int(input("Enter the Choice:"))

    if a!=0:
        if a==1:
            x=input("Enter the name of the key:")
            y=int(input("Enter the integer value:"))
            dict[x]=y
        elif a==2:
            x=input("Enter the name of the key to pop:")
            dict.pop(x)
        elif a==3:
            dict.popitem()
        elif a==4:
            x=int(input("Enter the integer value to be updated:"))
            y=int(input("Enter the integer value:"))
            
            '''z=dict.keys()
            for i in z:
                if dict[i]==x:
                    dict[i]=y
                    break
            else :
                p=input("Enter the new key name:")
                dict[p]=y'''
            z=dict.items()
            for i in z: 
                if i[1]==x:
                    dict[i[0]]=y
                    break
            else :
                p=input("Enter the new key name:")
                dict[p]=y
        elif a==5:
            print(dict)
        else :
            print("** Invalid Choice **")
    else :
        print("THank YoU!!!")
        print("Byeee")
        break