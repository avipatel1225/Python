list=[7,3,4,9,2,1,5,8,6]

for j in range(len(list),0,-1):
    for i in range(1,len(list)):
        if(list[i-1] > list[i]):
            list[i-1],list[i]=list[i],list[i-1]
        
print(list)