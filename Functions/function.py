'''def sq(a):
	print(a**2)

sq(6)

def sqroot(a):
    b=a**(1/2)
    print(b)

sqroot(25)'''

'''list=[5,3,2,1,4]
def ascending(list):
    for j in range(len(list),0,-1):
        for i in range(1,len(list)):
            if(list[i-1] > list[i]):
                list[i-1],list[i]=list[i],list[i-1]
    print(list)

ascending(list)'''

'''fst=[2,3,4,1,5,2,6,2]
def pop(a,b):
    count=0
    lst = a.copy()
    for i in range(len(lst)-1):
        if b==lst[i]:
            if count!=0:
                a.pop(i)
        count=count+1
    if(a[len(a)-1]==b):
        a.pop()
    print(a)
pop(fst,2)'''

list=[1,2,3,2,4,5,2,7,6,2]
def mode(a,b):
    count=0
    for i in range(len(a)):
        for j in a:
            if j==b:
                if count!=0:
                    a.remove(j)
                    break
                count=count+1
        count=0
    print(a)   
    
mode(list,2)