#String Format
quantity = '30 Ton'
product = 'Rice'
price = 5000

txt = 'I bought {} of {} for the price {}'
print(txt.format(quantity,product,price))
txt = 'I gave Rs.{2} for each ton in {0} of {1}'
print(txt.format(quantity,product,price))
print("My name is {fname}, I'am {age}".format(fname = "John", age = 36))

print(f"I purchased {quantity} of {product} worth Rs.{price} per ton")

movie = 'Mortal Kombat'
ticket = 400
time = 14.20
print('I went to the movie %s at noon %.2f by purchasing ticket for %d'%(movie,time,ticket))

city='Ahmedabad'
print("Age",21,"City",city)

a="Hello\
        Welcome"
print(a)

#String formatmap
# input stored in variable a. 
a = {'x':'John', 'y':'Wick'} 
  
# Use of format_map() function 
print("{x}'s last name is {y}".format_map(a))

# Input dictionary 
profession = { 'name':['Barry', 'Bruce'], 
               'profession':['Engineer', 'Doctor'], 
               'age':[30, 31] } 
                       
# Use of format_map() function  
print('{name[0]} is an {profession[0]} and he'
      ' is {age[0]} years old.'.format_map(profession)) 
        
print('{name[1]} is an {profession[1]} and he'
      ' is {age[1]} years old.'.format_map(profession)) 

#************************************************************************************************************************************************************************************
#String Formatting Types
#:<
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "<" to left-align the value:

txt = "We have {:<8} chickens."
print(txt.format(49))

#************************************************************************************************************************************************************************************
#:>
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use ">" to right-align the value:

txt = "We have {:>8} chickens."
print(txt.format(49))

#************************************************************************************************************************************************************************************
#:^
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))


#************************************************************************************************************************************************************************************
#:=
#To demonstrate, we insert the number 8 to specify the available space for the value.
#Use "=" to place the plus/minus sign at the left most position:

txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

#************************************************************************************************************************************************************************************
#:+
#Use "+" to always indicate if the number is positive or negative:

txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

#************************************************************************************************************************************************************************************
#:-
#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):

txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

#************************************************************************************************************************************************************************************
#:
#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:

txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))

#************************************************************************************************************************************************************************************
#:,
#Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."
print(txt.format(13800000000))

#************************************************************************************************************************************************************************************
#:_
#Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."
print(txt.format(13800000000))

#************************************************************************************************************************************************************************************
#:b
#Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

#************************************************************************************************************************************************************************************
#:d
#Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))

#************************************************************************************************************************************************************************************
#:e
#Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:e} chickens."
print(txt.format(5))

#************************************************************************************************************************************************************************************
#:E
#Use "E" to convert a number into scientific number format (with an upper-case E):

txt = "We have {:E} chickens."
print(txt.format(5))

#************************************************************************************************************************************************************************************
#:f
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = "The price is {:.2f} dollars."
print(txt.format(45))

#without the ".2" inside the placeholder, this number will be displayed like this:

txt = "The price is {:f} dollars."
print(txt.format(45))

#************************************************************************************************************************************************************************************
#:F
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')

txt = "The price is {:F} dollars."
print(txt.format(x))

#same example, but with a lower case f:

txt = "The price is {:f} dollars."
print(txt.format(x))

#************************************************************************************************************************************************************************************
#:o
#Use "o" to convert the number into octal format:

txt = "The octal version of {0} is {0:o}"

print(txt.format(10))

#************************************************************************************************************************************************************************************
#:x
#Use "x" to convert the number into Hex format:

txt = "The Hexadecimal version of {0} is {0:x}"

print(txt.format(255))

#************************************************************************************************************************************************************************************
#:X
#Use "X" to convert the number into upper-case Hex format:

txt = "The Hexadecimal version of {0} is {0:X}"

print(txt.format(255))


#************************************************************************************************************************************************************************************
#:%
#Use "%" to convert the number into a percentage format:

txt = "You scored {:%}"
print(txt.format(0.25))

#Or, without any decimals:

txt = "You scored {:.0%}"
print(txt.format(0.25))

#************************************************************************************************************************************************************************************


