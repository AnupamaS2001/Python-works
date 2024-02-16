# list=[3,4,5]
# total=sum(list)
# for i in range(0,len(list)):
#     res=total-list[i]
#     print(res)




list=[2,4,5,6]
i=0
j=1
count=len(list)
for i in range(0,count-1):
    for j in range(0,count):
        sum=i+j
    print(i,j)
    