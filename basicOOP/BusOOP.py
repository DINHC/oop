class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def __str__(self):
        return self.name
    

class SpaceShip:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def __str__(self):
        return self.name
class Bus(Vehicle):
    pass

class Camry(Vehicle):
    pass

class Enterprise(SpaceShip):
    pass

School_bus = Bus("School Volvo", 12, 50)

camryxle = Camry("Camry XLE", 28000, 4)

trek = Enterprise("Enterprise", 1000000000, 250)


#print(isinstance(School_bus, Vehicle)) <--- use of the isintance with School_bus and Vehicle returns True. 

# print(isinstance(trek, Vehicle)) <----- returns false, trek is made with Class SpaceShip not Vehicle

print(trek)