'''z=open("ehandle.txt")
y=open("handle.txt","w")
x=z.read()
y.write(x)
y.close()
a=open("handle.txt")
print(a.read())
a.close()
b=open("handle.txt","a")
b.write("\nwelcome sir \ngood to see you")
b.close()
c=open("handle.txt")
print(c.read())
c.close()'''

z=open("handle.txt")
a=z.read()
z.close()
y=open("merged.txt","w")
y.write(a)
y.close()
x=open("ehandle.txt")
b=x.read()
x.close()
w=open("merged.txt","a")
w.write(b)
w.close()
u=open("merged.txt")
print(u.read())
u.close()