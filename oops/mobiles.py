data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},  
     ]

# create
def create(*args,**kwargs):
    data.append(kwargs)
    return f"{kwargs} created successfully"


print(create(id="101",name="iphpone12",price=45000))


# retrieve
def retrieve(id=None):
    obj=[mob for mob in data if mob.get("id")==id]
    return obj
print(retrieve(id=103))

# delete
def destroy(*args,**kwargs):
    id=kwargs.get("id")
    obj=[mob for mob in data if mob.get("id")==id].pop()
    data.remove(obj)
    return f"{obj} is removed"
print(destroy(id=100))

# update

def put(id,*args,**kwargs):
    obj=[mob for mob in data if mob.get("id")==id].pop()
    obj.update(kwargs)
    return f"{obj} has been updated"

print(put(id=101,name="iphpone12",price=45000))