from re import *
text="ababcdABabc"
pattern="ab"
count=0
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start())
    print(m.group())
    count+=1
print("occurence=",count)