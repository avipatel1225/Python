try:
    z=int(input("enter first num"))
    x=int(input("enter sec num"))
    if z ==0 or x ==0:
        raise ValueError

    print(z/x)
except:
    print("from error block")
finally:
    print("from final")
else:
    print("MIMP")