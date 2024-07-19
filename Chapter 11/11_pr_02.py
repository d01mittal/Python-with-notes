class animal:
    animal="dog"

class pet(animal):
    color="white"

class dog(pet):
    @staticmethod
    def bark():
        print("Dogs bark like bow bow!")

d=dog()
d.bark()