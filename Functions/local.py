def demo():
    a=300
    print(a)
    global a
    a=100

a=15
print(a)
demo()
print(a)