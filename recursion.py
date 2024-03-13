'''i=0
def sum(a,b):
    global i
    while i<5:
        c=a+b
        print(c)
        i+=1
        sum(c,a)
	
sum(a=1,b=5)'''
#FACTORIAL
#without recursion
'''n=int(input("Enter the number for factorial:"))
j=1
for i in range(1,n+1):
    j=i*j
print(j)'''
#with recursion
m=int(input("Enter the number for factorial:"))
def fac(a):
    while a>1:
        a=a*fac(a-1)
        break
    return a
c=fac(a=m)
print(c)