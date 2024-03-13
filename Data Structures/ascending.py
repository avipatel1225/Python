dict={"one":32,"two":2,"three":31,"four":322,"five":132,}
final={}
list=[]
for i in dict.items():
    list.append(i[1])
list.sort()

for i in list:
    for j in dict.items():
        if i==j[1]:
            final[j[0]]=j[1]
            break

print(final)