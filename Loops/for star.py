'''for i in range(1,101):
    if i%2!=0:
        print(i,end="  ")'''
        
'''for i in range(50,9,-10):
    print(i)'''
    
'''for i in range(1,6):
    if i<5:
        print(i,end="")
        print("+",end="")
    else :
        print(i,end="")
        print("=",end="")'''

'''for i in range(1,6):
    if i%2==0:
        print(i,end="")
        print("+",end="")
    else :
        print(i,end="")
        print("!=",end="")'''
        
'''for i in range(1,6):
    if i%2==0:
        print("+",end="")
        print(i,end="")
    else :
        print("-",end="")
        print(i,end="")'''
        
'''for i in range(1,7):
    if i<6:
        if i%2!=0:
            print(i,"-",end="",sep="")
        else :
            print(i,"+",end="",sep="")
    else :
        print(i,"=",end="",sep="")'''
        
no=int(input("Enter the number for end point:"))

for i in range(1,no+1):
    if i%2==0:
        print("+",i,end="",sep="")
    else :
        print("-",i,end="",sep="")
