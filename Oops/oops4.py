#class in list
list=[]

class Emp():
    def setdata(obj,n,a,s):
        obj.name=n
        obj.age=a
        obj.salary=s
        list.append(obj)
    
    def __str__(obj):
        '''print(obj.name)
        print(obj.age)
        print(obj.salary)
        return " "'''
        return obj.name + "\n" + str(obj.age) + "\n" + str(obj.salary) + "\n"

#creating 5 emp objects
e1=Emp()
e1.setdata("avi",18,2500000)

e2=Emp()
e2.setdata("aarav",19,1000000)

e3=Emp()
e3.setdata("abhi",18,1500000)

e4=Emp()
e4.setdata("hari",20,2000000)

e5=Emp()
e5.setdata("yuvraj",17,500000)

#sorting list in ascending order based on emp salary
for j in range(len(list),0,-1):
    for i in range(1,len(list)):
        if list[i-1].salary > list[i].salary:
            list[i-1],list[i]=list[i],list[i-1]
            
#printing sorted list
for i in list:
    print(i)