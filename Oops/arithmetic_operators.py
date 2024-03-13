class Arithmetic:
    def __init__(obj1,h,m,s):
        obj1.hour=h
        obj1.min=m
        obj1.sec=s
    def __str__(obj):
        print(obj.hour,end=":")
        print(obj.min,end=":")
        print(obj.sec)
        return ""
    def __add__(obj1,obj2):
        obj1.hour=obj1.hour+obj2.hour
        obj1.min=obj1.min+obj2.min
        obj1.sec=obj1.sec+obj2.sec
        print(obj1)
    def __truediv__(obj1,obj2):
        obj1.hour=obj1.hour/obj2.hour
        obj1.min=obj1.min/obj2.min
        obj1.sec=obj1.sec/obj2.sec
        print(obj1)
    
        
a=Arithmetic(2,3,4)
b=Arithmetic(20,30,40)
#a+b
'''a.__add__(b)
print(a)'''

#b.__truediv__(a)
b/a