try :
    a=int(input("enetr the value of a"))
    b=int(input("enetr the value of a"))
    try:
        print(a/b)
    except:
        print("diviable by 0 is not possiable")
        
except ValueError:
    try:
        z = int(input("enter value from except"))
        print(z)
    except:
        print("error from except")
    print("str is not supported")
    
print("MIMP")