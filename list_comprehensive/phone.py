mobiles=[
    {"id":1,"name":"samsungs22","brand":"samsung","varients":[
        {"ram":"8gb","rom":"128gb","price":84000},
        {"ram":"8gb","rom":"256gb","price":100000},

    ]}, 
    {"id":1,"name":"samsungsa52","brand":"samsung","varients":[
        {"ram":"4gb","rom":"128gb","price":54000},
        {"ram":"8gb","rom":"256gb","price":65000},

    ]},
     {"id":1,"name":"one plus nord2","brand":"one plus","varients":[
        {"ram":"8gb","rom":"128gb","price":34000},
        {"ram":"8gb","rom":"256gb","price":45000},

    ]},
     {"id":1,"name":"miii1","brand":"redmi","varients":[
        {"ram":"8gb","rom":"128gb","price":24000},
        {"ram":"8gb","rom":"256gb","price":35000},
        
        
    ]},
]


# all_mob_name=[mob.get("name") for mob in mobiles]
# print(all_mob_name)

# all_mob_brand=[mob.get("brand") for mob in mobiles]
# print(all_mob_brand)

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price") in range(20000,30001):
#             print(mob.get("name"))

# prce_filter=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("price") in range(20000,30001)]
# print(prce_filter)

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("ram")=="4gb":
#             print(mob.get("name"))

# ramm=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")=="4gb"]
# print(ramm)

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("ram")=="8gb" and v.get("price")<=40000:
#             print(mob.get("name"))

mobb=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")=="8gb" and v.get("price")<=40000]
print(mobb)

costly_prices=max([v.get("price") for mob in mobiles for v in mob.get("varients")])
print(costly_prices)