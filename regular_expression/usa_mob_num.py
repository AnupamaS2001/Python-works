from re import *

mob=input("enter the number")
pattern = "[0-9]{3}[-\s]?[0-9]{3}[-\s]?[0-9]{4}"

matcher=fullmatch(pattern,mob)
print("invalid" if matcher==None else "valid") 