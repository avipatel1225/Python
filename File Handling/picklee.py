'''import pickle

z=open("paragraph.txt","rb")
#for write and append mode
#pickle.dump("Elephant is good",z)

#print(pickle.load(z))
#print(pickle.load(z))

try:
    while True:
        print(pickle.load(z))
except:
    print()
z.close()'''

import pickle

a=open("merged.txt","ab")
b=open("handle.txt","rb")
c=open("ehandle.txt","rb")
try:
    while True:
        pickle.dump(pickle.load(b),a)
except:
    print()
try:
    while True:
        pickle.dump(pickle.load(c),a)
except:
    print()
c.close()
b.close()
a.close()

z=open("merged.txt","rb")
try:
    while True:
    
        print(pickle.load(z))
except:
    print()
z.close()