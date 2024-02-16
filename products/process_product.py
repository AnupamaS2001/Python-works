from json import load

path="C:\\Users\\anupa\\OneDrive\\Desktop\\python_works\\products\\items.json"
with open(path,encoding="UTF-8") as f:
    data=load(f)

# print total num of products
print(len(data))
  
# print all actegories
all_categories={p.get("category") for p in data}
print(all_categories)

# print electronics product names
elec_items=[p.get("title") for p in data if p.get("category")=="electronics"]
print(elec_items)

# top rated product
rate=max(data,key=lambda p:float(p.get("rating").get("rate")))
print(rate.get("title"))