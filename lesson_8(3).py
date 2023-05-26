# Task 1:
# Create a class named Car and let class have brand, model name, construction year as attributes
class car:
    car_brand = " "
    car_modelname = " "
    car_construction_year = 0

# Task 3 
# constructor
class car:
    def __init__(self,incarbrand,incarmodelname,incar_constructionyear):
        self.car_brand = incarbrand
        self.car_modelname = incarmodelname
        self.car_construction_year = incar_constructionyear

# The new return printable function
    def __repr__(self):
        rpr = "Car brand is  " + self.car_brand + "car model is "+ self.car_modelname + "car constructed year is " + str(self.car_construction_year)
        return rpr


# Task 2:
# Create an Object of the car class and name it car1 with the brand porsche, the model cayenne and a construction year of 2019

car1 = car("porsche","cayenne",2019)

print (car1.car_brand)
print(car1.car_modelname)
print(car1.car_construction_year)
print(repr(car1))


