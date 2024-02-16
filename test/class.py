class books:
    data=[
        {"id":100,"name":"python","price":350},
        {"id":101,"name":"java","price":450},
        {"id":102,"name":"django","price":1300},
        {"id":103,"name":"html","price":1000},
        {"id":104,"name":"bootstrap","price":300}
    ]
    def get(self,*args,**kwargs):
        return f"{self.data}"

    def retrieve(self,id,*args,**kwargs):
        obj=[bks for bks in self.data if bks.get("id")==id]
        return obj
    
    def put(self,id,*args,**kwargs):
        obj=[bks for bks in self.data if bks.get("id")==id].pop()
        obj.update(kwargs)
        return obj
    def delete(self,id,*args,**kwargs):
        obj=[bks for bks in self.data if bks.get("id")==id].pop()
        self.data.remove(obj)
        return obj
    
obj=books()
print(obj.get(books))
print(obj.retrieve(id=101))
print(obj.put(id=104,name="flutter",price=370))
print(obj.delete(id=101))

