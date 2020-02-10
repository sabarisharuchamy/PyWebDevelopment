#To Print Multiplication Table after getting number of rows and the number to multiply with
x = input('which multiplication table do you need?\n')#ex - 3
x = int(x)
y = input('What is the length of the multiplication table?\n')#ex - 15
y = int(y)
z = x * y
z += 1
t = 0
for i in range(0,z,x):
   if i > 0:
       t += 1
       print(t,'*',x,'=',i)#ex - 1 * 3 = 3,2 * 3 = 6,...,15 * 3 = 45

#To print the mark range based on the input grade    
x = input('Enter your grade\n')
if x == 'A':
   print('Your mark is above 90%')
elif x == 'B':
   print('Your mark is between 70% and 90%')
elif x == 'C':
   print('Your mark is between 50% and 70%')
else:
   print('Your mark is below 50%')

#To get an input string from the user and convert the even position characters to upper case
x = input('Enter a string\n')
y = len(x)
x = x.lower()#Converting the input string to lowercase to maintain consistency
z = ''
i = 0
while i < y:
   if i % 2 != 0:
       z += x[i].upper()
   else:
       z += x[i]
   i += 1
else:
   print(z)

#Create an empty list, Populate the list with data and then perform operations such as Insert, Replace, Remove, Clear based on the user input
mylist=[]
x = 0
while x!=6:
   x = int(input('Menu - List Operations:\nEnter 1 for Add\nEnter 2 for insert\nEnter 3 for replace\nEnter 4 for remove\nEnter 5 for clear\nEnter 6 for Exit\n'))
   if x==1:
       listNo = int(input('\nEnter number of list items\t'))
       for i in range(0,listNo):
           mylist.append(input('\nEnter the '+str(i)+' data\t'))
       else:
           print(mylist)
   elif x!=1:
       if(len(mylist)==0):
           print('The list is empty! Please enter atleast 1 item and then select the desired operation')
           listNo = int(input('\nEnter number of list items\t'))
           for i in range(0,listNo):
               mylist.append(input('\nEnter the '+str(i)+' data\t'))
           else:
               print(mylist)
       elif x==2:
           xIndex = int(input('Enter the position to insert the element\n'))
           mylist.insert(xIndex,input('\nEnter the element\n'))
           print(mylist)
       elif x==3:
           xReplace = input('Enter the element to be replaced\n')
           yReplace = input('Enter the element to replace with\n')
           xIn = mylist.index(xReplace)
           mylist[xIn]=yReplace
           print(mylist)
       elif x==4:
           xElement = input('Enter the element to be remove\n')
           mylist.remove(xElement)
           print(mylist)
       elif x==5:
           mylist.clear()
           print(mylist)

#Create a map with predefined keys and add more records based on the existing keys
emp = ('id', 'name', 'age','salary','designation')
x = int(input('Enter number of records to be inserted\t'))
emprecs = {}
for i in range(x):
             emprecs[i+1]=dict.fromkeys(emp)
             print('Enter the '+str(i+1)+' record details')
             for j in range (5):
                             emprecs[i+1][emp[j]]=input('Enter the '+emp[j]+': ')
             
print(emprecs)


#Employee Storage System using File Handling
print('---------------------------Employee Record Storage System-------------------------')
noEmp = int(input('Enter the number of employees to be stored:\n'))
import os
if os.path.exists('Records'):
   print(os.getcwd())
   print('Changing to Records Directory')
   os.chdir(os.getcwd()+'\\Records')
   print(os.getcwd())
   for i in range(1,(noEmp+1)):
       fileName = 'Emp'+str(i)+'.txt'
       f=open(fileName,'wt')
       name = input('Enter Employee'+str(i)+' Name:\n')
       designation = input('Enter Employee'+str(i)+' Designation:\n')
       salary = input('Enter Employee'+str(i)+' Salary:\n')
       f.write('******************************************************************************\n')
       f.write('Employee name: '+name+'\n')
       f.write('Employee designation: '+designation+'\n')
       f.write('Employee salary: '+salary+'\n')
       f.write('******************************************************************************')
       f.close()
   for i in range(1,(noEmp+1)):
       print('Employee'+str(i)+' Details:\n')
       fileName = 'Emp'+str(i)+'.txt'
       f=open(fileName,'rt')
       print(f.read())
       f.close()
else:
   print(os.getcwd())
   print('Records Directory doesnt exit. Creating Directory now...')
   os.mkdir('Records')
   print('Records Directory Created!')
   print(os.getcwd())
   print('Changing to Records Directory')
   os.chdir(os.getcwd()+'\\Records')
   print(os.getcwd())
   for i in range(1,(noEmp+1)):
       fileName = 'Emp'+str(i)+'.txt'
       f=open(fileName,'wt')
       name = input('Enter Employee'+str(i)+' Name:\n')
       designation = input('Enter Employee'+str(i)+' Designation:\n')
       salary = input('Enter Employee'+str(i)+' Salary:\n')
       f.write('******************************************************************************\n')
       f.write('Employee name: '+name+'\n')
       f.write('Employee designation: '+designation+'\n')
       f.write('Employee salary: '+salary+'\n')
       f.write('******************************************************************************')
       f.close()
   for i in range(1,(noEmp+1)):
       print('Employee'+str(i)+' Details:\n')
       fileName = 'Emp'+str(i)+'.txt'
       f=open(fileName,'rt')
       print(f.read())
       f.close()
