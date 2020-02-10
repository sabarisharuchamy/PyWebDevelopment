#global
x = "Good"

def myfunc():
    print("Christmas is " + x)#global variable can be accessed from local scope

myfunc()
print("Darbar is also "+x)#global variable being accessed from global scope

#local
def myfunc2():
    z = 'Boom'
    print('Let me teach '+z)#Local variable can be accessed from only within the local scope

myfunc2()
#print('Let me sing '+z) #Uncomment this for error #Local variable cannot be accessed from global scope

#Creating global variable from inside the local scope
def myfunc3():
    global y,t
    y = 10
    t = 'Ram'
    print('Inside the local scope '+t)
    print('Inside the local scope',y)

myfunc3()
print('Outside the local scope and Inside the global scope '+t)
print('Outside the local scope and Inside the global scope',y)

#For changing global variable value from within the local scope
x = 5

def myfun4():
    global x
    x = 10
    print('Value of x inside the local scope',x)

myfun4()
print('Value of x outside the local scope and inside the global scope',x)

#Allocation Error
a = 2

def myfunc5():
    #print(a) #Uncomment for error #Reason - Trying to access the variable a before assigning the value in local scope
    a = 10
    print('Value of a inside the local scope',a)

myfunc5()
print('Value of a outside the local scope and inside the global scope',a)
