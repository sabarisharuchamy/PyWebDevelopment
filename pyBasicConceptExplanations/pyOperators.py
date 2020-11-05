#python operators
#Arithmetic Operator
#+
x = 10
y = 3
z = x + y
print('Addition or + operator result:',z)#13
#-
z = x - y
print('Subtraction or - operator result:',z)#7
#*
z = x * y
print('Multiplication or * operator result:',z)#30
#/
z = x / y
print('Division or / operator result:',z)#3.3333333333333335
#//
z = x // y
print('Floor Division or // operator result:',z)#3
#%
z = x % y
print('Modulus(Remainder) or % operator result:',z)#1
#**
z = x ** y
print('Power or ** operator result:',z)#1000

#Assignment Operator
#=
x = 5
print('Value of x is',x)#5
#+=
x += 3 #Translates to x = x + 3
print('Value after x += 3 is',x)#8
#-=
x -= 3 #Translates to x = x - 3
print('Value after x -= 3 is',x)#5
#*=
x *= 3 #Translates to x = x * 3
print('Value after x *= 3 is',x)#15
#/=
#Changing x value to 17
x = 17
x /= 3 #Translates to x = x / 3
print('Value after x /= 3 is',x)#5.666666666666667
#%=
#Changing x value to 17
x = 17
x %= 3 #Translates to x = x % 3
print('Value after x %= 3 is',x)#2
#//=
#Changing x value to 17
x = 17
x //= 3 #Translates to x = x // 3
print('Value after x //= 3 is',x)#5
#**=
x **= 3 #Translates to x = x ** 3
print('Value after x **= 3 is',x)#125

#&=
#Changing x value to 7
x = 7 #Binary value of 7 is 111
print('Binary value of '+str(x)+' is',format(x,'b'))
x &= 5 #Translates to x = x & 5 #Binary value of 5 is 101
print('Binary value of '+str(5)+' is',format(5,'b'))
#111
#101
#---
#101 #Bitwise & -> 1 & 1 = 1, 0 & 0 = 0, 1 & 0 = 0, 0 & 1 = 0
print('Value after x &= 5 is',x)#5

#|=
#Changing x value to 7
x = 7 #Binary value of 7 is 111
print('Binary value of '+str(x)+' is',format(x,'b'))
x |= 5 #Translates to x = x | 5	#Binary value of 5 is 101
print('Binary value of '+str(5)+' is',format(5,'b'))
#111
#101
#---
#111 #Bitwise | -> 1 | 1 = 1, 0 | 0 = 0, 1 | 0 = 1, 0 | 1 = 1
print('Value after x |= 5 is',x)#7

#^=
print('Binary value of '+str(x)+' is',format(x,'b'))
x ^= 3 #Translates to x = x ^ 3	#Binary value of 3 is 011
print('Binary value of '+str(3)+' is',format(3,'b'))
#111
#011
#---
#100 #Bitwise | -> 1 ^ 1 = 0, 0 ^ 0 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1
print('Value after x |= 3 is',x)#40

#>>=
#Changing x value to 7
x = 7 #Binary value of 7 is 111
print('Binary value of '+str(x)+' is',format(x,'b'))
x >>= 2 #Translates to x = x >> 2 #x = 7 >> 2
#111 >> 2 -> after removing 11 from the rightside of 111, 00 are added to the leftside of 1 becoming 001 -> 1
print('Value after x >> 2 is',x)#1

#<<=
#Changing x value to 7
x = 7 #Binary value of 7 is 111
print('Binary value of '+str(x)+' is',format(x,'b'))
x <<= 2 #Translates to x = x << 2 #x = 7 << 2
#111 << 2 -> No removal is done, just 00 are added to the rightside of 111 becoming 11100 which results in the increased decimal value of 28 
print('Value after x << 2 is',x)#28

#Comparison Operators
#== (Equal)
x = 10; y = 10;
print('Result of x == y is',x == y)#True
x = 12; y = 5;
print('Result of x == y is',x == y)#False
#!= (Not equal)
#x != y
x = 10; y = 10;
print('Result of x != y is',x != y)#False
x = 12; y = 5;
print('Result of x != y is',x != y)#True
#> (Greater than)
#x > y
x = 10; y = 10;
print('Result of x > y is',x > y)#False if x and y are equal Or if y is greater than x
x = 12; y = 5;
print('Result of x > y is',x > y)#True
#< (Less than)
#x < y
x = 10; y = 10;
print('Result of x < y is',x < y)#False if x and y are equal Or if x is greater than y
x = 2; y = 5;
print('Result of x < y is',x < y)#True
#>= (Greater than or equal to)
#x >= y
x = 10; y = 10;
print('Result of x >= y is',x >= y)#True if x and y are equal Or if x is greater than y
x = 2; y = 5;
print('Result of x >= y is',x >= y)#False
#<= (Less than or equal to)
#x <= y
x = 10; y = 10;
print('Result of x <= y is',x >= y)#True if x and y are equal Or if y is greater than x
x = 2; y = 5;
print('Result of x <= y is',x >= y)#False

#Logical Operators
#and - Both the condition before and after 'and' should yield True
x = 10
y = 23
z = 5
print(x > 6 and x < 12)#True - Since x is within the range of 6 to 12
print(x > y and y > z)#False - Since x is lower than y, it won't check the second condition at all
print(y > z and x > y)#False - Even though the first condition is True but the second condition is False - So the whole result is False

#or - Any one of the condition need to be True
x = 10
y = 23
z = 5
print(x > y or y > z)#True

#not - Inverse of the actual result
print(not(True))#False
print(not(False))#True
x = 55
y = 7
print(not(x > y))#False

#Identity Operators
#is
print(ord('h'))
print(ord('H'))
print('hi' is 'Hi')#False - ASCII value of h is 104 and H is 72
print('Hi' is 'Hi')
x = ['apple','banana','cherry']
y = ['apple','banana','cherry']#same values as x but different memory(different instance / reference)
z = x #Assigning both the reference and values of x to z
print('Values of x',x)
print('Values of y',y)
print('Values of z',z)
x.append('donut')
print('Values of x after appending one item to x',x)
print('Values of y after appending one item to x',y)#changes made in x wont affect y
print('Values of z after appending one item to x',z)#changes made in x affects z
print(x == y)#True #Contains same values
print(x is y)#False #Contains same values but different instances
print(x == z)#True #Contains same values
print(x is z)#True #Contains same values and share same instance

#is not
print(x is not y)#True
print(x is not z)#False