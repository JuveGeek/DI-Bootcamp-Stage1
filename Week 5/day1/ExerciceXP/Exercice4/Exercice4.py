class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name=zoo_name
        self.animals=[]

    def add_animal(self, new_animal):
        for x in self.animals:
            if x!=new_animal:
                self.animals.append(new_animal) 

    def get_animals(self):
        for x in self.animals:
            print(x)

