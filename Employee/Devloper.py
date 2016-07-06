'''
    Name:Devloper.py
    Description:Devloper Class
'''
from Employee import Employee

class Developer(Employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        Employee.__init__(self,name,"Developer",salary)
if __name__=='__main__':

    developer1=Developer("Rosy",6000)
    developer1.bonus(100)
    print(developer1.getEmpInfo())

    developer2=Developer("Crissy",5000)
    developer2.bonus(300)
    print(developer2.getEmpInfo())

    developer3=Developer("Shan",4000)
    developer3.bonus()
    print(developer3.getEmpInfo())
