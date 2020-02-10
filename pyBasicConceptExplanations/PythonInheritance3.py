#Multi Level Inheritance
class Animal():
    species = 'Animal'
    def disp_spe(self):
        print('Species is '+self.species)

class Dog(Animal):
    pet = 'Dog'
    def disp_nam(self):
        print('My Pet is '+self.pet)

class BabyDog(Dog):
    secpet = 'BabyDog'
    def disp_sec(self):
        print('My second pet is '+self.secpet)

myBaby = BabyDog()
myBaby.disp_spe()
myBaby.disp_nam()
myBaby.disp_sec()
