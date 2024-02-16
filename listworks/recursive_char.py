text="ABACCD"
lst=[]
duplicate_lst=[]
for ch in text:
    char_count=lst.count(ch)
    if char_count==0:
        lst.append(ch)
    else:
        duplicate_lst.append(ch)
print(f"second recursive character is {duplicate_lst[1]}")
        
    