num=(input("enter the num"))
digit_count=len(num)
num=int(num)
original=num
sum=0
while(num!=0):
    last_digit=num%10
    cube=last_digit**digit_count
    sum=sum+cube
    num=num//10
print("armstrong" if(sum==original) else "not armstrong")    