class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1. Create another cat breed named Siamese which inherits from the Cat class.

class Siamese(Cat):
    pass

bengal= Bengal("bob", "Wouah")
chartreux = Chartreux("mare", "miaoh")
siamese = Siamese("Zebra", "ZZZZZZZZZZ")


#2. Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
all_cats=[bengal, chartreux, siamese]

print(chartreux)
