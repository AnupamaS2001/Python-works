from re import *

pan=input("enter the pan num")
pattern="[A-Z]{3}[PCAFHT]+\d{4}[A-Z]{1}"

matcher=fullmatch(pattern,pan)

if matcher==None:
    print("invalid")
else:
    print("valid")