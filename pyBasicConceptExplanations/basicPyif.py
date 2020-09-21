"""
File:test.py
Date:11-09-2020
Version:1.0
Description:Program to learn python
"""
print("Ashok Gowtham")
print('Ashok Gowtham')
print("""Ashok
is
learning
Python""")
print('''Ashok
is
learning
Java''')
print("Ashok\nis\tlearning\nPerl")
if 5 > 4:
    print("5 is greater than 4")
print("Outside of if scope")
if 5 > 4:
    print("5 is greater than 4")
    print("4 is lesser than 5")
print("Outside of if scope")
if 5 > 4:
        print("5 is greater than 4")
    #print("4 is lesser than 5")#Uncomment for error
print("Outside of if scope")
if 5 > 4:
        print("5 is greater than 4")#same level of indentation
        print("4 is lesser than 5")#same level of indentation
print("Outside of if scope")
a = 5#store 5 in variable a
b = 4#store 4 in variable b
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")
print("Outside of if scope")
a = 6
b = 5
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")
print("Outside of if scope")
firstName = input("Enter ur first name:\n")
middleName = input("Enter ur middle name:\n")
lastName = input("Enter ur last name:\n")
print("Your full name is",firstName,middleName,lastName)
x = int(input("Enter number1:\n"))
y = int(input("Enter number2:\n"))
res = x + y
print("Addition of two nos is",res)
