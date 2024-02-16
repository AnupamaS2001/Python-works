# movies released after 2014

for mv in data:
    r_date=mv.get("released")
    year=r_date.split(" ")[-1]

    if year.isdigit():
        if int(year)>2014:
            print(mv.get("title"),mv.get("released"))



