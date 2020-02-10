#Using super keyword
class Animal:
    species = 'land'
    def dispSpecies(self):
        print('Species printed within Animal Class: '+self.species)
class Dog(Animal):
    food = 'carnivores'
    def dispFood(self):
        print('Species accessed from within the Dog Child Class using super(): '+super().species)#Animal is the parent class of Dog #super() is used to access the parent class variable or method
        print('Species accessed from within the Dog Child Class using Parent Class name: '+Animal.species)
        print('Food accessed from within the Dog Class: '+self.food)
        super().dispSpecies()#Calling parent class method using super() keyword
    def dispWhat(self):
        print('This is inside the Dog class')
        
class BabyDog(Dog):
    legs = 'four'
    def dispLegs(self):
        print('Food accessed from within the BabyDog Child Class using super(): '+super().food)
        print('Species accessed from within the BabyDog Child Class using Parent Class name: '+Animal.species)
        print('Species accessed from within the BabyDog Child Class using Parent Class name: '+Dog.species)
        print('Species accessed from within the BabyDog Child Class using Parent Class name: '+super().species)
        print('Legs accessed from within the BabyDog Class : '+self.legs)
        super().dispWhat()
        super().dispFood()
test = BabyDog()
test.dispLegs()
