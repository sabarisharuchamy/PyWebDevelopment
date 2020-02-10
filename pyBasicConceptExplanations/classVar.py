##class MyClass:
##    x = 5
##    y = 2
##
##myObj = MyClass()
##print("Before change",myObj.x)
##print("Before change",myObj.y)
##myObj.x = 25
##myObj.y = 44
##print("After change",myObj.x)
##print("After change",myObj.y)
class Details:
    name = ''
    age = ''
    designation = ''

emp1 = Details()
emp1.name = 'Ramesh'
emp1.age = 44
emp1.designation = 'System Architect'
print("Employee name is "+emp1.name)
print("Employee age is",emp1.age)
print("Employee designation is "+emp1.designation)

emp2 = Details()
emp2.name = 'Prabu'
emp2.age = 25
emp2.designation = 'Software Engineer'
print("Employee name is "+emp2.name)
print("Employee age is",emp2.age)
print("Employee designation is "+emp2.designation)
