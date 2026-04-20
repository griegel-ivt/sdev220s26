class Vehicle:
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

car = Automobile("car", "", "", "", "", "")

car.year = input("Year: ")
car.make = input("Make: ")
car.model = input("Model: ")
car.doors = input("Doors: ")
car.roof = input("Roof: ")

print("\nVehicle type: " + car.type + 
      "\nYear: " + car.year +
      "\nMake: " + car.make +
      "\nModel: " + car.model +
      "\nNumber of doors: " + car.doors +
      "\nType of roof: " + car.roof)