class employee:
    id:int
    name:str
    dept:str
    salary:int
    company_name:str
    def __init__(self,id,name,dept,salary,company_name):
        self.id=id
        self.name=name
        self.dept=dept
        self.salary=salary
        self.company_name=company_name

    def display(self):
        