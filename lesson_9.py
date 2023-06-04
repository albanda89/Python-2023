# Task 1
class Vehicle:
    def __init__(self, max_speed, mileage, name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    def seating_capacity(self, capacity):
        return f"The seating capacity of {self.name} is {capacity}."

car = Vehicle(200, 100000, "volkswagen golf")
print(car.seating_capacity(5))

class Bus(Vehicle):
    color = "white"

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


# Testing the program
bus = Bus(120, 5000, "Volvo")
print(f"Maximum Speed: {bus.max_speed}")
print(f"Mileage: {bus.mileage}")
print(f"Name: {bus.name}")
print(f"Color: {bus.color}")
print(bus.seating_capacity())
print(bus.seating_capacity(60))
