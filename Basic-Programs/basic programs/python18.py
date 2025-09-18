#Object oriented programming
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    
    def getSalary(self):
        print(self.salary)
rohan=employee("Rohan","780000") 
rohan.getSalary()
# print(rohan.salary)     
# print(rohan.name) 
gohan=employee("Gohan","980000") 
gohan.getSalary()
# print(rohan.salary)     
# print(rohan.name) 