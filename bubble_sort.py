list=[3,2,4,5,1]
for i in range(1,len(list)):
    for k in range(0,len(list)-i):
        if list[k]>list[k+1]:
            temp=list[k]
            list[k]=list[k+1]
            list[k+1]=temp
for i in range (len(list)):
    print(list[i])