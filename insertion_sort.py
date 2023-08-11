uns=[4,2,1,5,3]
for i in range(len(uns)):
    min=uns[i]
    inx=i
    for k in range(i+1,len(uns)):
        if min>uns[k]:
            min=uns[k]
            inx=k
    temp=uns[inx]
    uns[inx]=uns[i]
    uns[i]=temp
print(uns)

