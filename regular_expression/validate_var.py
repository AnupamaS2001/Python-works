from re import *

varname=input("enter the variable")
pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,varname)
if matcher==None:
    print("invalid")
else:
    print("valid")