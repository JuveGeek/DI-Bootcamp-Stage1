class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

#Instantiate three Cat objects using the code provided above.

firt_cat = Cat("Dodat", 13)
second_cat = Cat("Milou", 5)
third_cat = Cat("Boby", 15)

def findYounger():
    
    if firt_cat.age > second_cat.age and firt_cat.age > third_cat.age:
        print("Le plus vieux est ", firt_cat.name ,"il a ",firt_cat.age ," ans ")
        return firt_cat.age

    elif second_cat.age > third_cat.age and second_cat.age > firt_cat.age:
        print("Le plus vieux est ", second_cat.name ,"il a ",second_cat.age ," ans ")
        return second_cat.age
    else:
        print("Le plus vieux est ", third_cat.name ,"il a ",third_cat.age ," ans ")
        return third_cat.age



findYounger()
