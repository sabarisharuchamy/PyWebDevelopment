#Palindrome Checking
txt = input('Enter the string to check for palindrome\n')
txtlen = len(txt)
txt2 = ''
txt = txt.lower()
for i in range(txtlen-1,-1,-1):
    #print(txt[i])
    txt2 += txt[i]


if txt == txt2:
    print(txt+" is a palindrome")
else:
    print(txt+" is not a palindrome")
