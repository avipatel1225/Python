class Time:
    def __init__(obj,h,m,s):
        obj.hour=h
        obj.min=m
        obj.sec=s
    def __str__(obj):
        print(obj.hour)
        print(obj.min)
        print(obj.sec)
        return ""
        
a=Time(20,5,15)
print(a)