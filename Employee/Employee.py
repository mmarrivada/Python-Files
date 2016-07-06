'''
    class:Employee
    Description:base class for all employees

'''
import itertools

class Employee:
    #emp_id=1
    emp_id=itertools.count( )
    def __init__(self,name,position,salary):
        
        # self.emp_id = self.emp_id
        # self.__class__.emp_id +=1
        self.emp_id=next(self.emp_id)
        self.name=name
        self.position=position
        self.salary=salary
        self.total_pay=salary

    def bonus(self,amount=200):
        self.total_pay+=amount
        print()

    def getEmpInfo(self):

        return {'Name' : self.name,'Id':self.emp_id,'Position':self.position,'Total Payment': self.total_pay }

if __name__=='__main__':
    emp1 = Employee("Jhon","Manager",5000)
    emp1.bonus(1000)
    print(emp1.getEmpInfo())

    emp2 = Employee( "Domino","Developer", 3000 )
    emp2.bonus( 500 )
    print(emp2.getEmpInfo( ))

