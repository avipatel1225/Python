#single inheritance
'''class a:
    def demo(p):
        print("from class a")
        
class b(a):
    def demo2(p):
        print("from class b")
        
x=b()
x.demo()
x.demo2()'''

#multilevel inheritance
'''class a:
    def demo(p):
        print("from class a")
        
class b(a):
    def demo2(p):
        print("from class b")
        
class c(b):
    def demo3(p):
        print("from class c")
        
x=c()
x.demo()
x.demo2()
x.demo3()'''

#multiple inheritance
'''class a:
    def demo(p):
        print("from class a")
        
class b:
    def demo2(p):
        print("from class b")
        
class c(a,b):
    def demo3(p):
        print("from class c")
        
x=c()
x.demo()
x.demo2()
x.demo3()'''

#hierarchical inheritance
'''class a:
    def demo(p):
        print("from class a")

class b(a):
    def demo2(p):
        print("from class b")
        
class c(a):
    def demo3(p):
        print("from class c")
        
x=c()
x.demo()
x.demo3()
print()
z=b()
z.demo()
z.demo2()'''

#hybrid inheritance
class a:
    def demo(p):
        print("from class a")
        
class b:
    def demo2(p):
        print("from class b")
        
class c(b):
    def demo3(p):
        print("from class c")
        
class d(c,a):
    def demo4(p):
        print("from class d")
        
class e(d):
    def demo5(p):
        print("from class e")
        
z=c()
z.demo2()
z.demo3()
print()
x=d()
x.demo()
x.demo2()
x.demo3()
x.demo4()
print()
y=e()
y.demo()
y.demo2()
y.demo3()
y.demo4()
y.demo5()