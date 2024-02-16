# student rollnum,course,total

class student:
    roll:int
    course:str
    total:int

    def __init__(self,rollnum,course,total):
        self.roll=rollnum
        self.course=course
        self.total=total
    def display(self):
        print(self.roll,self.course,self.total)

obj1=student(1000,"django",450)
obj1.display()