#Function Varitations
#with arguments and with return value
def add(x, y):
   result = x + y
   return result
#without arguments and without return value
def sub():
   x = int(input('Enter x value:\n'))
   y = int(input('Enter y value:\n'))
   result = x - y
   print('Sub of 2 nos is',result)
#with arguments and without return value
def mul(x,y):
   result = x * y
   print('Mul of 2 nos is',result)
#without arguments and with return value
def div():
   x = int(input('Enter x value:\n'))
   y = int(input('Enter y value:\n'))
   result = x / y
   return result

choice = int(input('Enter the choice of operation: 1 for +, 2 for -, 3 for *, 4 for /\n'))
if choice == 1:
   x = int(input('Enter x value:\n'))
   y = int(input('Enter y value:\n'))
   result = add(x,y)
   print('Sum of 2 nos is',result)
elif choice == 2:
   sub()
elif choice == 3:
   x = int(input('Enter x value:\n'))
   y = int(input('Enter y value:\n'))
   mul(x,y)
elif choice == 4:
   result = div()
   print('Div of 2 nos is',result)
else:
   print('Invalid Choice.. Please try again')