cakes=[
     {"id":1,"name":"blueberry","shape":"circle","varients":[
        {"weight":"0.5kg","price":400},
        {"weight":"1kg","price":800}
    ]},
     {"id":2,"name":"vancho","shape":"square","varients":[
        {"weight":"0.5kg","price":500},
        {"weight":"1kg","price":1000}
    ]},
     {"id":3,"name":"chocalate","shape":"heart","varients":[
        {"weight":"0.5kg","price":600},
        {"weight":"1kg","price":1200}
    ]},
     {"id":4,"name":"cheese","shape":"rectangle","varients":[
        {"weight":"0.5kg","price":650},
        {"weight":"1kg","price":1300}]}
]



#cake price<600

lpc=[cak.get("name") for cak in cakes for v in cak.get("varients") if v.get("price")<=600 ]
print(lpc)


# 1kg,circle

kg_circle=[cak.get("name") for cak in cakes for v in cak.get("varients") if v.get("weight")=="1kg" and cak.get("shape")=="circle"]
print(kg_circle)


#price,0.5,cheese

cheese=[v.get("price") for cak in cakes for v in cak.get("varients") if v.get("weight")=="0.5kg" and cak.get("name")=="cheese"]
print(cheese)


#names

name=[cak.get("name") for cak in cakes]
print(name)  

#1kg names


kg_names=[cak.get("name") for cak in cakes for v in cak.get("varients") if v.get("weight")=="1kg"]
print(kg_names)


#costly

cost=[v.get("price") for cak in cakes for v in cak.get("varients")] 
print(max(cost))


#heart cake


hc=[cak.get("name") for cak in cakes if cak.get("shape")=="heart"]
print(hc)