'''for i in range(1,6):
    if i==3:
        print("$",end="")
    else :
        print("*",end="")'''
        
'''for i in range(1,6):
    if i==1 or i==5:
        print("$",end="")
    else :
        print("*",end="")'''
        
'''for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print("\n")'''
    
'''for i in range(1,6):
    for j in range(1,6):
        if j==3:
            print("$",end="")
        else :
            print("*",end="")
    print("\n")'''
    
'''for i in range(1,6):
    for j in range(1,5):
        if j==1:
            print("*",end="")
        else :
            print("$",end="")
    print("\n")'''
    
'''for i in range(1,6):
        for j in range(1,6):
            if j!=1 and j!=5:
                if i==1 or i==5:
                    print("*",end="")
                else :
                    print(" ",end="")
            else :
                print("*",end="")
        print("\n")'''
        
'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("*",end="")
        else :
            print("$",end="")
    print("\n")'''
    
'''for i in range(1,7):
    for j in range(6,0,-1):
        if i==j:
            print("$",end="")
        else :
            print("*",end="")
    print("\n")'''
    
for i in range(1,6):
    for j in range(5,0,-1):
        if i!=j:
            if j!=1 and j!=5:
                if i==1 or i==5:
                    print("$",end="")
                else :
                    print(" ",end="")
            else :
                    print("$",end="")
        else :
            print("*",end="")
    print("")