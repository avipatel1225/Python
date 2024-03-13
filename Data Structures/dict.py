#creating dict
d={"one":"hey","two":1,"x":1}

print(d)
print(dir(d))

print()
#Functions of dict
print(d.values())

print(d.keys())

'''print(d.popitem())
print(d)'''

'''print(d.pop("one"))
print(d)'''

print(d.items())

print(d.fromkeys("one"))
x=d.fromkeys("one")
x["o"]=1
x["e"]=100
print(x)

print(d.get("one"))