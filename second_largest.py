a=50
b=40
c=70
# if ((a<b) and (a>c)) or((a>b) and (a<c)):
#     print(f"second largest no:{a}")
# elif ((b<a) and (b>c)) or((b>a) and (b<c)):
#     print(f"second largest no:{b}")
# elif ((c<b) and (c>a)) or((c>b) and (c<a)):
#     print(f"second largest no:{c}")    





if((a>b)and (a>c)):
        if(b>c):
            print(f"second largest no:{b}")
        else:
            print(f"second largest no:{c}")
elif((b>a) and (b>c)):
        if(a>c):
            print(f"second largest no:{a}")
        else:
            print(f"second largest no:{c}")
elif((c>a) and (c>b)):      
        if(a>c):
            print(f"second largest no:{a}")
        else:
            print(f"second largest no:{b}")