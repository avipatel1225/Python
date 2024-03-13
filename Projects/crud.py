z=[]

while(True):
    print("Enter 1 to Add No")
    print("Enter 2 to Remove No")
    print("Enter 3 to Insert No")
    print("Enter 4 to Display No")
    print("Enter 5 to Update No")
    print("Enter 0 to EXIT!!")

    a = int(input("Enter the value:"))

    if a!=0:    
        if a==1:
            x=int(input("Enter the Number to Add:"))
            z.append(x)
        elif a==2:
            x=int(input("Enter the Number to Remove:"))
            z.remove(x)
        elif a==3:
            x=int(input("Enter the Number to Add:"))
            y=int(input("Enter the position to add number:"))
            z.insert(y-1,x)
        elif a==4:
            print(z)
        elif a==5:
        '''
            flag=1
            p=int(input("Enter the number to update:"))
            for i in z:
                if i==p:
                    flag=2
                    x=int(input("Enter the Number to Add:"))
                    y=z.index(p)
                    z.insert(y,x)
                    z.remove(p)
                    break
            if flag==1:
                print("Not Found")'''
            p=int(input("Enter the number to update:"))
            for i in z:
                if i==p:
                    x=int(input("Enter the Number to Add:"))
                    y=z.index(p)
                    z.insert(y,x)
                    z.remove(p)
                    break   
            else :
                print("Not Found")
           
        else :
            print("Incorrect Value")
        print()
    else :
        print("BYE!!!")
        break