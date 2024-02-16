f_read=open("C:\\Users\\anupa\\OneDrive\\Desktop\\python_works\\file\\vehicle_numbers.txt")

f_write=open("C:\\Users\\anupa\\OneDrive\\Desktop\\python_works\\file\\kerala_num.txt","w")

for line in f_read:
    reg_number=line.rstrip("\n")

    if reg_number.startswith("kl"):
        f_write.write(reg_number+"\n")