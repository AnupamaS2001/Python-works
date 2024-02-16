from re import *

lang=input("enter the text")
pattern="[klmn][369][\w]*"

matcher=fullmatch(pattern,lang)

if matcher==None:
    print("invalid")
else:
    print("valid")