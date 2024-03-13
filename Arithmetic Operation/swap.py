'''a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

a=a+b
b=a-b
a=a-b

print("New value of a:",a,sep="")
print("New value of b:",b,sep="")'''

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

print(id(a))
print(id(b))

a,b=b,a

print(id(a))
print(id(b))

print("New value of a:",a,sep="")
print("New value of b:",b,sep="")