gender="female"
tummy_size=26
buttock_size=30
size=tummy_size/buttock_size
print("value=",size)
if(gender=="male"):
    if(size<=0.95):
        print("low")
    elif(size<1)and (size>0.95):
        print("moderate")
    else:
        print("high")
elif(gender=="female"):
    if(size<=0.80):
        print("low")
    elif(size<0.85)and (size>0.80):
        print("moderate")
    else:
        print("high")