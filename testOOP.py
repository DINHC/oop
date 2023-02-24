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

