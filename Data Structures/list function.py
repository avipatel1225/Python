lst= [1,2,2,2,2,2,3,4,5,6,7,8,9]


#lst.clear()
lst.reverse()
print(lst.count(1))
print(lst.index(1))
lst.sort()
lst.sort(reverse = True)

print(lst)

'''z=lst
lst.append(10)'''

z=lst.copy()
lst.append(10)

print(lst)
print(z)

x=[10,20,30,40]

lst.extend(x)
print(x)
print(lst)