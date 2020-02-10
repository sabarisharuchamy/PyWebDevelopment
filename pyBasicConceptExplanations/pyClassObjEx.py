##class MyClass:
##  x = 5
##
###First Object
##p1 = MyClass()
##print(p1.x)#Get x value before changing
##p1.x = 20#Set x value to 20
##print(p1.x)#Get x value after changing
##
###Second Object
##p2 = MyClass()
##print(p2.x)#Get x value before changing
##p2.x =30#Set x value to 30
##print(p2.x)#Get x value after changing

##class MyDetail:
##    firstName = 'Ram'
##    middleName = 'Charan'
##    lastName = 'Teja'
##    age = 50
##
##p1 = MyDetail()
##print('My full name is '+p1.firstName+' '+p1.middleName+' '+p1.lastName+' and My age is ',p1.age)
##p1.firstName = 'Jai'
##p1.middleName = 'Sree'
##p1.lastName = 'Ram'
##p1.age = 25
##print('My full name is '+p1.firstName+' '+p1.middleName+' '+p1.lastName+' and My age is ',p1.age)
##
##p2 = MyDetail()
##print('My full name is '+p2.firstName+' '+p2.middleName+' '+p2.lastName+' and My age is ',p2.age)
##p2.firstName = 'Lord'
##p2.middleName = 'Maha'
##p2.lastName = 'Vishnu'
##p2.age = 32
##print('My full name is '+p2.firstName+' '+p2.middleName+' '+p2.lastName+' and My age is ',p2.age)

##class Employee:
##    empId = 'defaultId'
##    empName = 'defaultName'
##    empDesignation = 'defaultDesignation'
##    empSalary = 'defaultSalary'
##
##empRecs = {}    
##num = int(input('Enter the number of employees to be recorded\n'))
##for i in range(1,num+1):
##    empRecs[i]=Employee()
##    empRecs[i].empId = int(input('Enter Employee'+str(i)+' id:\n'))
##    empRecs[i].empName = input('Enter Employee'+str(i)+' name:\n')
##    empRecs[i].empDesignation = input('Enter Employee'+str(i)+' designation:\n')
##    empRecs[i].empSalary = float(input('Enter Employee'+str(i)+' salary:\n'))
##
##for i in range(1,num+1):
##    print('Employee'+str(i)+' details:')
##    print('Id:',empRecs[i].empId)
##    print('Name: '+empRecs[i].empName)
##    print('Designation: '+empRecs[i].empDesignation)
##    print('Salary: ',empRecs[i].empSalary)
    
##class Simple:
##    num1 = int(input('Enter the first number:\n'))
##    num2 = int(input('Enter the second number:\n'))
##    def __init__(self):#Only once the input for the two nos is given and then the result is printed based on the number of objects created
##        #Whenever an object is created, the constructor wil be called.
##        print('Addition of two numbers is',(self.num1+self.num2))
##        print('Subtraction of two numbers is',(self.num1-self.num2))
##        print('Multiplication of two numbers is',(self.num1*self.num2))
##        print('Division of two numbers is',(self.num1/self.num2))
##
##cont = int(input('Enter number of times for the constructor to be invoked:\n'))
##for i in range(cont):
##    Simple()

##class Simple:
##    num1 = 0#Not necessary
##    num2 = 0#Not necessary
##    def __init__(self):#Whenever an object is created, the constructor wil be called and the input is given for the two nos and the results are printed
##        self.num1 = int(input('Enter the first number:\n'))
##        self.num2 = int(input('Enter the second number:\n'))
##        print('Addition of two numbers is',(self.num1+self.num2))
##        print('Subtraction of two numbers is',(self.num1-self.num2))
##        print('Multiplication of two numbers is',(self.num1*self.num2))
##        print('Division of two numbers is',(self.num1/self.num2))
##
##cont = int(input('Enter number of times for the constructor to be invoked:\n'))
##for i in range(cont):
##    Simple()    

##class Simple:
##    def __init__(self):#Whenever an object is created, the constructor wil be called and the input is given for the two nos and the results are printed
##        self.num1 = int(input('Enter the first number:\n'))#Created when the constructor is called
##        self.num2 = int(input('Enter the second number:\n'))#Created when the constructor is called
##        print('Addition of two numbers is',(self.num1+self.num2))
##        print('Subtraction of two numbers is',(self.num1-self.num2))
##        print('Multiplication of two numbers is',(self.num1*self.num2))
##        print('Division of two numbers is',(self.num1/self.num2))
##
##cont = int(input('Enter number of times for the constructor to be invoked:\n'))
##for i in range(cont):
##    Simple()

##class Simple:
##    def __init__(self):#Whenever an object is created, the constructor wil be called and the input is given for the two nos
##        self.num1 = int(input('Enter the first number:\n'))#Created when the constructor is called
##        self.num2 = int(input('Enter the second number:\n'))#Created when the constructor is called
##        
##arith = {}
##cont = int(input('Enter number of times for the constructor to be invoked:\n'))
##for i in range(cont):
##    arith[i] = Simple()#Object with num1 and num2 binded are stored in arith
##    print('Addition of two numbers is',(arith[i].num1+arith[i].num2))#Getting the values bound to arith object and doing addition
##    print('Subtraction of two numbers is',(arith[i].num1-arith[i].num2))
##    print('Multiplication of two numbers is',(arith[i].num1*arith[i].num2))
##    print('Division of two numbers is',(arith[i].num1/arith[i].num2))


##class Simple:
##    def __init__(self):#Whenever an object is created, the constructor wil be called and the input is given for the two nos
##        self.num1 = int(input('Enter the first number:\n'))#Created when the constructor is called
##        self.num2 = int(input('Enter the second number:\n'))#Created when the constructor is called
##    def sum(self):
##        print('Addition of two numbers is',(self.num1+self.num2))#Getting the values bound to arith object and doing addition
##    def sub(self):
##        print('Subtraction of two numbers is',(self.num1-self.num2))
##    def mul(self):
##        print('Multiplication of two numbers is',(self.num1*self.num2))
##    def div(self):
##        print('Division of two numbers is',(self.num1/self.num2))
##        
##arith = {}
##cont = int(input('Enter number of times for the constructor to be invoked:\n'))
##for i in range(cont):
##    arith[i] = Simple()#Object with num1 and num2 binded are stored in arith
##    arith[i].sum()
##    arith[i].sub()
##    #arith[i].mul()
##    #arith[i].div()
    
##class Simple:
##    def __init__(self,myTea,myCoffee):#Whenever an object is created, the constructor wil be called and the input is set for the two nos
##        self.num1 = myTea
##        self.num2 = myCoffee
##    def sum(self):
##        print('Addition of two numbers is',(self.num1+self.num2))#Getting the values bound to arith object and doing addition
##    def sub(self):
##        print('Subtraction of two numbers is',(self.num1-self.num2))
##    def mul(self):
##        print('Multiplication of two numbers is',(self.num1*self.num2))
##    def div(self):
##        print('Division of two numbers is',(self.num1/self.num2))
##        
####arith = Simple(23,2)
####arith.sum()
####arith.sub()
##arith = {}
##cont = int(input('Enter number of times for the constructor to be invoked:\n'))
##for i in range(cont):
##    arith[i] = Simple((int(input('Enter the first number:\n'))),(int(input('Enter the second number:\n'))))#Values are passed and set using the constructor during onject creation
##    arith[i].sum()
##    arith[i].sub()
##    #arith[i].mul()
##    #arith[i].div()

##class Simple():
##    name = None
##    age = 0
##    def insert(self,myTea,myCoffee):
##        self.name = myTea
##        self.age = myCoffee
##    def disp(self):
##        print('My name is '+str(self.name))
##        print('My age is',self.age)
##myObj = Simple()
##myObj.insert('Guru',22)#Values are set by calling insert method
##myObj.disp()#Values are printed - Guru, 22
##myObj2 = Simple()
##myObj2.disp() #Values are not set but attempted printing, So printed None,0

        
class Simple():
    name = None
    age = 0
    def __init__(self,myTea,myCoffee):
        self.name = myTea
        self.age = myCoffee
    def disp(self):
        print('My name is '+str(self.name))
        print('My age is',self.age)

#myObj = Simple()#TypeError: __init__() missing 2 required positional arguments: 'myTea' and 'myCoffee'#Uncomment for error
myObj = Simple('Sridhar',28)
myObj.disp()
       
