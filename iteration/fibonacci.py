limit=int(input("enter the limit"))

i=1
pre=0
cur=1
print(pre)
print(cur)
for i in range(0,limit):
    next=pre+cur
    print(next)
    pre=cur
    cur=next
    