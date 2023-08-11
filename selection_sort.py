uns=[4,3,2,1,5,8,7,6]
for i in range(len(uns)):
    temp=uns[i]
    k=i-1
    while k>=0 and temp<uns[k]:
        uns[k+1]=uns[k]
        k-=1
    uns[k+1]=temp
print(uns)
