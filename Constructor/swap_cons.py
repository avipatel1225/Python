#swap using constructor
class Emp:
    def __init__(obj,n,a,s):
        obj.name=n
        obj.age=a
        obj.salary=s
    def __str__(obj):
        print(obj.name)
        print(obj.age)
        print(obj.salary)
        return ""
    
def swap(a,b):
    a,b=b,a
    print(a)
    print(b)
    
e1=Emp("avi",18,2500000)
e2=Emp("abhi",19,1500000)
swap(e1,e2)