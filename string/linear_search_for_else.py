lst=[4,6,8,9]
num=6
for i in range (0,len(lst)):
    if(num==lst[i]):
        print("element found")
        break

else:
    print("element not found")