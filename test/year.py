# years=[[1803,1809,1805],[1909,1911,1913],[2000,2004,2005],[2011,2012,2013]]
# count=len(years)
# for i in range(0,count-1):
#     for j in range(0,3):
#      if((years(i(j))%100)==0) and (years(i(j))%400==0):
#        print(years(i(j)))
#      elif (years(i(j))%100!=0) and (years(i(j))%4==0):
#        print(years(i(j)))
#      else:
#        print("not leap year")
#     j+=1
# i+=1


year=int(input ("enter the year"))
if(((year%100)==0) and (year%400==0)):
    print(f"{year} is leap year.")
elif(year%100!=0) and (year%4==0):
    print(f"{year} is leap year.")
else:    
    print(f"{year} is not leap year.")