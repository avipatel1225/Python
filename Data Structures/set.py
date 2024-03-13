#creating a set
x={1,2,"hi","hello","xyz",4.5,6,3.5}
y={10,2,"hey","hello","abc",4,6.1}

'''print(type(x))
print(x)
'''
#creating an empty set
a=set()
'''

print(type(a))

#changing set to list
z=list(x)
print(type(z))'''

#Functions of set
print(dir(x))
print(x)

'''x.add(50)
print(x)

x.pop()
print(x)

x.remove(4.5)
print(x)

b=x.copy()
print(b)

x.discard("xyz")
print(x)

c=x.intersection(y)
print(c)

d=x.difference(y)
print(d)'''

print(x.isdisjoint(y))
print(x.isdisjoint(a))

print(a.issubset(x))

print(x.issuperset(a))
print(x.issuperset(y))

print(x.symmetric_difference(y))

print(x.union(y))

'''x.clear()
print(x)'''