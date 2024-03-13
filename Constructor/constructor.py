#constructor
class Cons:
    def __init__(self):
        print("hi hello how are you")
        
a=Cons()

#method over-reading
class Demo:
    def __init__(obj):
        print("hi")
        
    def __init__(obj):
        print("hi")
        print("hi")
        print("hi")
        
z=Demo()