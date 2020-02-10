#file = open('dog_breeds.txt')


try:
    reader = open('dog_breeds.txt')
    print(type(reader))
    print(reader.read())
except:
    print("Something went wrong when writing to the file")
finally:
    reader.close()

file = open('dog_breeds.txt', 'rb')
print(type(file))
file = open('dog_breeds.txt', 'wb')
print(type(file))
file = open('dog_breeds.txt', 'rb', buffering=0)
print(type(file))
