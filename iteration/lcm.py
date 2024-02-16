num1=int(input ("enter value for num1:>"))
num2=int(input("enter value for num2:>"))
# hcf=1
# lg_num=num1 if(num1>num2) else num2
# sm_num=num1 if(num1<num2) else num2
# for i in range(1,sm_num+1):
#     if num1%i==0 and num2%i==0:
#         hcf=i
# lcm=(num1*num2)/hcf
# print("lcm=",lcm)



lcm=1
lg_num=num1 if(num1>num2) else num2
product=num1*num2
for i in range(lg_num,product+1):
     if i%num1==0 and i%num2==0:
         lcm=i
         break
print("lcm=",lcm)