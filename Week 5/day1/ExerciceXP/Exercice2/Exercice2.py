from unicodedata import name


class Dog():
    def __init__(self,name, heigth):
        self.name=name
        self.heigth=heigth

    def bark(self):
        print(self.name, "goes woof")

    def jump(self):
        print(self.name, "jumps ", self.heigth, "cm high" )

davids_dog= Dog("Rex", 50)

print("Le nom du chien est ", davids_dog.name, "il mésure ",davids_dog.heigth)
davids_dog.bark()
davids_dog.jump()