#valid Complex
d = 5j
e = 3+0j
f = 3.5+3j
print(d)
print(e)
print(f)

#Type Conversion
x = 5
y = 12.44
print(float(5))
print(int(y))
print(complex(5))
print(f*2)
print('ba'+'na'*2)

x,y,z='Orange','Banana','Grapes'

print(x+' '+y+' '+z)

x = y = z = 'Lemon'
print(x+' '+y+' '+z)

x = y = z = 10
print(x,y,z)

#slicing
z = 'Sree rama!'
print(z[0])#S
print(z[4:])# rama!
print(z[:4])#Sree
print(z[-1])#!
print(z[-4:])#ama!
print(z[-8:])#ee rama!
print(z[:-1])#Sree rama
print(z[-6:-1])# rama

#len()
print(len(z))

#lower()
print(z.lower())

#upper()
print(z.upper())

#strip()
t = '        Terminator        Regint                   '
print(t.strip())

#lstrip()
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)

#rstrip()
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "banana,,,,,ssaaww....."
x = txt.rstrip(",.asw")
print(x)

#multiline string
a = '''Ram
Murug
Kanna'''
print(a)

#replace()
print(t.replace('Regint','Judgment'))

t = 'Tic Tic Tic Tac Toe'
print(t.replace('Tic','Tipp'))
print(t.replace('Tic','Tipp',2))

#split()
y = 'Hiya,Riki,Mala'
z = 'John Bradshaw Layfield'
print(y.split(','))
print(z.split(' '))

#rsplit()
txt = "apple, banana, cherry"
print(txt.rsplit(", "))

txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
print(txt.rsplit(", ", 1))

#splitlines()
print(a.splitlines())

#partition()
'''Search for the word "bananas", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"'''
txt = "I could eat bananas all day"
print(txt.partition("bananas"))

txt = "I could eat bananas all day"
print(txt.partition("apples"))

#rpartition()
txt = "I could eat bananas all day, bananas are my favorite fruit"
print(txt.rpartition("bananas"))

txt = "I could eat bananas all day, bananas are my favorite fruit"
print(txt.rpartition("apples"))

#membership
print('Tic' in t)
print('Tedd' in t)
print('Tedd' not in t)

#Identity
print('hi' is 'Hi')
print('hi' is not 'Hi')

print('Hi there \'Randy\' \nKennedy \rOrton \b-RKO')
print("Hella FF\b\bFella \"How\" are you?")

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#String methods
#isdigit()
a='777'
print(a.isdigit())

a='77a'
print(a.isdigit())

#isaplha()
a='abc'
print(a.isalpha())

a='ab7'
print(a.isalpha())

#isalnum()
txt = "Company12"
print(txt.isalnum())

txt = "Company 12"
print(txt.isalnum())

#isdigit()
txt = "50800"
print(txt.isdigit())

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "\u0061"
print(a.isdigit())
print(b.isdigit())
print(c.isdigit())

#isidentifier()
print('Identifier')
txt = "Demo"
print(txt.isidentifier())

a = "MyFolder"
b = "_Demo002"
c = "2bring"
d = "my demo"
e = "class"
f = "!~good"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
print(e.isidentifier())
print(f.isidentifier())

import keyword

#iskeyword()
print(keyword.iskeyword(a))
print(keyword.iskeyword(e))

#islower()
txt = "hello world!"
print(txt.islower())

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())

#isupper()
txt = "THIS IS NOW!"
print(txt.isupper())

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())

#isprintable()
txt = "Hello! Are you #1?"
print(txt.isprintable())

txt = "Hello!\nAre you #1?"
print(txt.isprintable())

#title()
txt = "Welcome to my world"
print(txt.title())

txt = "Welcome to my 2nd world"
print(txt.title())

txt = "hello b2b2b2 and 3g3g3g"
print(txt.title())

#istitle()
txt = "Hello, And Welcome To My World!"
print(txt.istitle())

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

#isspace()
a='   '
print(a.isspace())

a=' \'  '
print(a.isspace())

#startswith()
x = 'Robot is a machine that does what humans can do and can\'t do'
print(x.startswith('Robot'))

#endswith()
print(x.endswith('do'))

#find
print('homeowner'.find('meow'))
print('homeowner'.find('wow'))

print(x.find('do'))
print(x.find('do',28,50))
print(x.find('do',50))

#rfind()
txt = "Mi casa, su casa."
print(txt.rfind("casa"))

txt = "Hello, welcome to my world."
print(txt.rfind("e", 5, 10))

#join
print("*".join(['red','green','blue']))
print(" ".join(['Randy','Monty','Cross']))

#capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)
txt = "36 is my age."
x = txt.capitalize()
print(x)

#casefold()
txt = "Hello, And Welcome To My World!"
print(txt.casefold())
txt = "FLASH IS THE FASTEST SUPER HERO"
print(txt.casefold())
txt = "zoom is the villain of flash"
print(txt.casefold())

#swapcase()
txt = "Hello, And Welcome To My World!"
print(txt.swapcase())
txt = "FLASH IS THE FASTEST SUPER HERO"
print(txt.swapcase())
txt = "zoom is the villain of flash"
print(txt.swapcase())

#center()
txt = "John"
print(txt.center(20))
print(txt.center(20,'T'))

txt = "Typhoon Earthquake"
print(txt.center(50))
#print(txt.center(20,'TOP')) #Uncomment for error #The fill character must be exactly one character long

#ljust()
txt = "banana"
print(txt.ljust(20))
print(txt.ljust(20, "O"))

#rjust()
x = txt.rjust(20)
print(x, "is my favorite fruit.")
print(txt.rjust(20, "O"))

#zfill()
txt = "50"
print(txt.zfill(10))
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

#count()
x = 'Robot is a machine that does what humans can do and can\'t do'
print(x.count('do'))
txt = "I love apples, apple are my favorite fruit"
print(txt.count("apple", 10, 24))

#encode()
txt = "My name is Ståle"
print(txt.encode())
txt="This is © . This is ∉ . And this is €"
print(txt.encode())

txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
#print(txt.encode(encoding="ascii",errors="strict")) #Uncomment for error #UnicodeEncodeError: 'ascii' codec can't encode character '\xe5' in position 13: ordinal not in range(128)

txt="This is © . This is ∉ . And this is €"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
#print(txt.encode(encoding="ascii",errors="strict"))#Uncomment for error #UnicodeEncodeError: 'ascii' codec can't encode character '\xa9' in position 8: ordinal not in range(128)


txt = "Only available in ansi - ƒ"
print(txt.encode(encoding="ansi"))
#print(txt.encode(encoding="ascii"))#Uncomment for error #UnicodeEncodeError: 'ascii' codec can't encode character '\u0192' in position 25: ordinal not in range(128)
print(txt.encode(encoding="utf-8"))
#Only available in 8859.If a browser detects ISO-8859-1 in a web page, it defaults to ANSI.UTF-8 is a multibyte encoding that can represent any Unicode character.
#ISO 8859-1 is a single-byte encoding that can represent the first 256 Unicode characters. Both encode ASCII exactly the same way.

txt="This is © . This is ∉ . And this is €"
print(txt.encode(encoding="utf-8"))


#expandtabs
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#If the value is not found, the find() method returns -1, but the index() method will raise an exception:

txt = "Hello, welcome to my world."

print(txt.find("q"))
#print(txt.index("q")) #Uncomment for error

#maketrans()
'''Syntax : maketrans(str1, str2, str3)

Parameters :
str1 : Specifies the list of characters that need to be replaced.
str2 : Specifies the list of characters with which the characters need to be replaced.
str3 : Specifies the list of characters that needs to be deleted.

Returns : Returns the translation table which specifies the conversions that can be used by translate()'''
# translations using  
# maketrans() and translate() 
  
# specify to translate chars 
str1 = "wy"
  
# specify to replace with 
str2 = "gf"
  
# delete chars 
str3 = "u"
  
# target string  
trg = "weeksyourweeks"
  
# using maketrans() to  
# construct translate 
# table 
table = trg.maketrans(str1, str2, str3) 
  
# Printing original string  
print ("The string before translating is : ", end ="") 
print (trg) 
  
# using translate() to make translations. 
print ("The string after translating is : ", end ="") 
print (trg.translate(table)) 

#translate()
'''Syntax : translate(table, delstr)

Parameters :
table : Translate mapping specified to perform translations.
delstr : The delete string can be specified as optional argument is not mentioned in table.

Returns : Returns the argument string after performing the translations using the translation table.'''
# translations without 
# maketrans()  
  
# specifying the mapping  
# using ASCII  
table = { 119 : 103, 121 : 102, 117 : None } 
  
# target string  
trg = "weeksyourweeks"
  
# Printing original string  
print ("The string before translating is : ", end ="") 
print (trg) 
  
# using translate() to make translations. 
print ("The string after translating is : ", end ="") 
print (trg.translate(table)) 
