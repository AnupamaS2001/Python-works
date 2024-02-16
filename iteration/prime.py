isflag=False
num=int(input("enter the num"))
for i in range (2,num):
    if(num%i==0):
        isflag=True
        break
print("it is prime num" if(isflag==False) else "it is not prime" )

