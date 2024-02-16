class book:
    author_name:str
    name:str
    publisher:str
    price:int
    def __init__(self,author_name,name,publisher,price):
        self.author_name=author_name
        self.name=name
        self.publisher=publisher
        self.price=price
    def display(self):
        print(self.author_name,self.name,self.publisher,self.price)
    def __str__(self):
        return self.name
obj1=book("aami","mandhaaram","dc books",540)
print(obj1)
obj1.display()