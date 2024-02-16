from re import *

aadhar=(input("enter the aadhar num"))
pattern="\d{4}[- ]?\d{4}[- ]?\d{4}"

matcher=fullmatch(pattern,aadhar)

# if matcher==None:
#     print("invalid")
# else:
#     print("valid")
print("invalid" if(matcher==None) else ("valid"))