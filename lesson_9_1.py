# Task 2
class Vehicle:
    def __init__(self, max_speed, mileage, name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of {self.name} is {capacity}."


# Example usage:
car = Vehicle(200, 10000, "Tesla Model S")
print(car.seating_capacity(5))  # Output: The seating capacity of Tesla Model S is 5.
