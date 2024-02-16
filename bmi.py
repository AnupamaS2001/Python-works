weight_kg=40
height_cm=152
height_m=height_cm/100
bmi=weight_kg/(height_m**2)
print("bmi=",bmi)
if(bmi<=19):
    print("under weight")
elif(bmi>19) and (bmi<25):
    print("normal")
elif(bmi>24) and (bmi<30):
    print("over weight")
elif(bmi>=30):
    print("obesity")