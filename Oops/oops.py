class Emp():
    name=""
    age=0
    salary=0

list=[]
e1=Emp()
e1.name="Avi"
e1.age=19
e1.salary=2500000
list.append(e1)

e2=Emp()
e2.name="Abhi"
e2.age=18
e2.salary=500000
list.append(e2)

e3=Emp()
e3.name="Kush"
e3.age=20
e3.salary=1500000
list.append(e3)

e4=Emp()
e4.name="Jash"
e4.age=20
e4.salary=100000
list.append(e4)

'''def max(a,b):
    if a>b:
        print(e1.name)
        print(e1.age)
        print(e1.salary)
    else:
        print(e3.name)
        print(e3.age)
        print(e3.salary)
if e1.salary > e2.salary:
    max(e1.salary,e3.salary)
else:
    max(e2.salary,e3.salary)'''
    
value=0
for i in list:
    if value < i.salary:
        value=i.salary

for i in list:
    if value==i.salary:
        print(i.name)
        print(i.age)
        print(i.salary)