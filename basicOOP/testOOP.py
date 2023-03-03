#Basic code of OOP. Class Dog with varaible name and age set 
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


#Added a class attribute with species. 
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

#A litte more complex/fun
class Dragon: 
    species = "Danger Fire Snek"

    def __init__(self, name, age, ability, region, dangerlevel):
        self.name = name 
        self.age = age
        self.ability = ability 
        self.region = region 
        self.dangerlevel = dangerlevel 