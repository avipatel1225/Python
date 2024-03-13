'''a=open("numbers.txt")
p=a.read()
b=open("even.txt","a")
c=open("odd.txt","a")
for i in p:
    if int(i)%2==0:
        b.write(i)
    else:
        c.write(i)
b.close()
c.close()
a.close()
d=open("even.txt")
print(d.read())
d.close()
e=open("odd.txt")
print(e.read())
e.close()'''

a=open("paragraph.txt")
p=a.read()
b=open("vowels.txt","a")
c=open("consonants.txt","a")
for i in p:
    if i==
    'a' or i=='e' or i=='i' or i=='o' or i=='u':
        b.write(i)
    else:
        c.write(i)
b.close()
c.close()
a.close()
d=open("vowels.txt")
print(d.read())
d.close()
e=open("consonants.txt")
print(e.read())
e.close()