#function in class
class Emp():
    def setdata(obj,name,age,salary):
        obj.name=name
        obj.age=age
        obj.salary=salary
        
    def calldata(obj):
        print(obj.name)
        print(obj.age)
        print(obj.salary)
        print()

e1=Emp()
e1.setdata("avi",18,2500000)
e1.calldata()

e2=Emp()
e2.setdata("abhi",19,1500000)
e2.calldata()