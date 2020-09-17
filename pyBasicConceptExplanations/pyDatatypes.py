#Number
x = 5 #integer
y = 2.32 #float
z = 5j #complex
print(x)
print(type(x))
x = int(20)#not recommended #Created by using constructor
print(x)
print(type(x))
print(y)
print(type(y))
y = float(20.5)#not recommended #Created by using constructor
print(y)
print(type(y))
print(z)
print(type(z))
z = complex(1j)#not recommended #Created by using constructor
print(z)
print(type(z))
#String
x = 'Hello'
print(x)
print(type(x))
x = str("Hello World")#not recommended #Created by using constructor
print(x)
print(type(x))
#There are four collection data types in the Python programming language:

#List - ordered,indexed,changeable,allows duplicate values,element access.
#Tuple - ordered,indexed,unchangeable,allows duplicate values,element access.
#Set - unordered,unindexed,only element access,No duplicate values.
#Dictionary - unordered, changeable, indexed[key],Unique Key[string or numeric constant],No duplicate key but duplicate value is allowed.

#Sequence Data Type
#list
x = ['Zoom','Boom','Zoom','5',3,6]
print(x)
print(type(x))
y = [1,2,3,4]
z = ['One','Two','Three','Four']
x = [y,z]
print(x)
print(type(x))
x = list(("Lucas", "Lucifer", "Ludo",'2',3,6))#not recommended #Created by using constructor
print(x)
print(type(x))
#tuple
x = ('Zoom','Boom','Zoom','5',3,6)
print(x)
print(type(x))
y = [1,2,3,4]
z = ['One','Two','Three','Four']
x = (y,z)
print(x)
print(type(x))
x = tuple(("Zoom", "Lucifer", "Boom",'2',3,6))#not recommended #Created by using constructor
print(x)
print(type(x))
x = ('a')#Tuple with a single element becomes a string/int
print(type(x))
print(x)
x = ('a',)#To create a tuple with single element use , after the first element
print(type(x))
print(x)
#range
x = range(6)
print(x)
print(type(x))
for i in range(6):
    print(i)

#mapping Datatype
#Dictionary
x = {"name" : "John", "age" : 36}
print(type(x))
print(x['name'])
print(x['age'])
x = {"names":['Richard','Razor','Maggy'],23:('Ten','Twenty',30),"occupation":{'Richard':'Soldier','Razor':'Doctor','Maggy':'Nurse'}}
print(x.get('names'))
print(x['names'][2])
print(x[23])
print(x.get('occupation'))
print(x.get('occupation').get('Richard'))
x = dict(name="John", age=36)#not recommended #Created by using constructor
print(x)
print(type(x))

#set datatype
#set
x = {1,3,2,4,2}
print(type(x))
print(x)
x.remove(3)
print(x)
x = {'Mela','Ram','Mela','Chris'}
print(x)
x = set(("John", "Rocs", "Tera"))#not recommended #Created by using constructor
print(x)
print(type(x))

#frozen set
x = frozenset((1,3,2,4,2))#only way to create a frozen set
print(type(x))
print(x)
#x.remove(3) #Uncomment for error #Frozen set is same as set except it is immutable
x = frozenset(("John", "Rocs", "Tera"))

#Boolean Datatype
print(10 > 9)
print(10 == 9)
print(10 < 9)
x = True
print(type(x))
print(x)
x = bool(5)#not recommended #Created by using constructor
print(type(x))
print(x)
x = bool(False)#not recommended #Created by using constructor
print(type(x))
print(x)
print(bool(0))#Integer 0 - Not a valid existence
print(bool(''))#Empty string without space - Not a valid existence
print(bool({}))#Empty Set / Dictionary - Not a valid existence
print(bool(None))#None - Not a valid existence
print(bool(False))
print(bool(()))#Empty tuple - Not a valid existence
print(bool('Ram'))#string - a valid existence
print(bool({1,2,3}))#set - a valid existence
print(bool((1,2,3)))#tuple - a valid existence
print(bool(['a','b','c']))#list - a valid existence
print(bool({'a':23,'b':25}))#dictionary - a valid existence
print(bool(True))
print(bool(' '))#string with space - a valid existence
x = 200
print(isinstance(x, int))#isinstance is a method to check whether a variable is of particular datatype
a = 200
b = 33
if b > a: #if with condition b > a will result in boolean value: true or false
  print("b is greater than a") #Executed if true
else:
  print("b is not greater than a") #Executed if false


#Binary DataType
#Bytes
#bytes() returns an immutable bytes object.
x = b"Hello"
print(type(x))
print(x)
x = bytes(5)
print(type(x))
print(x)
x = bytes([1,2,3,4,5])
#x[3]=2 #Uncomment for error #Bytes - Cannot change value
print(type(x))
print(x)
x = bytes('hello','utf-8')
print(type(x))
print(x)

#ByteArray - is mutable
x = bytearray(5)
print(type(x))
print(x)
a=bytearray([1,2,3,4,5])
print(a)
a[4]=3
print(a)

#MemoryView
a=bytes(4)
print(memoryview(a))
for i in memoryview(a):
    print(i)#prints 0
print(memoryview(bytes([1,2,3,4,5])))
for i in memoryview(bytes([1,2,3,4,5])):
    print(i)#prints 1,2,3,4,5
print(memoryview(bytearray([1,2,3,4,5])))
for i in memoryview(bytearray([1,2,3,4,5])):
    print(i)#prints 1,2,3,4,5
for i in memoryview(bytes('hello','utf-8')):
    print(i)#prints 104,101,108,108,111

print(ord('H'))
print(chr(104))
