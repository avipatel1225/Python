'''def add(a,b):
    c=a+b
    print(c)
    return c
	
func=add
print(type(func))
print(func(5,10))'''

'''def demo(a):
    print("I am in Demo")
    def hello(b):
        b()
        print("I am in Hello")
    hello(a)    
def test():
    print("I am in Test")
demo(test)'''

'''list=[1,2,3,4,5]
def new(a):
    a.append(10)
    print(a)
    print(type(a))
new(list)
print(list)
print(type(list))'''

def func():
    print("I am in Function")
    def new(a):
        print("I am in New")
        a()
    new(func)
func()