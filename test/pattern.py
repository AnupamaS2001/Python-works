text="ABABC"
# list=[]
# dp_lst=[]
# for ch in text:
#     count=list.count(ch)
#     if count==0:
#         list.append(ch)
#     else:
#         dp_lst.append(ch)
# print(dp_lst)

for i in text:
    if text.count(i)==1:
        print(i)
