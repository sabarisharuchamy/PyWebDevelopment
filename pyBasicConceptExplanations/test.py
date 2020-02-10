emp = ('id', 'name', 'age','salary','designation')
x = int(input('Enter number of records to be inserted\t'))
emprecs = {}
for i in range(x):
              emprecs[i+1]=dict.fromkeys(emp)
              print('Enter the '+str(i+1)+' record details')
              for j in range (5):
                              emprecs[i+1][emp[j]]=input('Enter the '+emp[j]+': ')
              
print(emprecs)
              
