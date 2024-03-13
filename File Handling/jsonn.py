import json

a=open("text1.txt","r")
try:
    while True:
        print(json.load(a))
except:
    print()
print(json.load(a))
a.close()