from re import *

vehicle_num=input("enter the vehicle number")
pattern="(KL)[-\s]\d{2}[-\s][A-Z]{1,2}[-\s]\d{4}"

matcher=fullmatch(pattern,vehicle_num)

if matcher==None:
    print("invalid")
else:
    print("valid")