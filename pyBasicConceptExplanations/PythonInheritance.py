#Single Level Inheritance
class Employee():
    salary = 20000
    def disp_sal(self):
        print('Employee salary is',self.salary)
class Programmer(Employee):
    bonus = 10000
    def disp_bon(self):
        print('Employee Designation is Programmer')
        print('Employee salary is',self.salary)
        print('Employee bonus is',self.bonus)

myProg = Programmer()
myProg.disp_bon()

#myEmp = Employee()
#myEmp.disp_sal()



