from re import *
text="ABCDABCDAB"
pattern="AB"
matcher=finditer(pattern,text)
count=0
for i in matcher:
    print(i.start())
    print(i.group())
    count=count+1
print("count:",count)
