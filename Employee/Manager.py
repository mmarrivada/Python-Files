'''
    Name:Manager.py
    Description:Manager Class
'''
from Employee import Employee

class Manager(Employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        Employee.__init__(self,"name","Manager",salary)
if __name__=='__main__':

    manager1=Manager("Anna",6000)
    manager1.bonus(1000)
    print(manager1.getEmpInfo())

    manager2=Manager("Bogut",5000)
    manager2.bonus()
    print(manager2.getEmpInfo())

    manager3=Manager("Smith",4000)
    manager3.bonus(900)
    print(manager3.getEmpInfo())
