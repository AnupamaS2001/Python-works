# linear searching

lst=[10,45,76,34,97]
element=int(input("enter the the element"))
is_present=False

for i in range(0,len(lst)):
    if(lst[i]==element):
        is_present=True
        break
print(is_present)


