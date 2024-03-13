#function in class
def sumdata(obj1,obj2):
        new=Time()
        new.hour=obj1.hour + obj2.hour
        new.min=obj1.min + obj2.min
        new.sec=obj1.sec + obj2.sec
        return new
        
class Time():
    def setdata(obj,hour,min,sec):
       obj.hour=hour
       obj.min=min
       obj.sec=sec
       
    def getdata(obj):
        print(obj.hour,end=" : ")
        print(obj.min,end=" : ")
        print(obj.sec)
        print()

t1=Time()
t1.setdata(15,35,23)
t1.getdata()

t2=Time()
t2.setdata(3,25,37)
t2.getdata()

#t1.sumdata(t2)
#t1.getdata()

#t3=t1.sumdata(t2)
#t3.getdata()    

t3=sumdata(t1,t2)
t3.getdata()