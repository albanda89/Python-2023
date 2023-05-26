# Task 1:
# Create a class named Car and let class have brand, model name, construction year as attributes

# creating car class
class car:
    car_brand = "" 
    car_modelname = ""
    car_construction_year = 0

# Task 2:
# Create an Object of the car class and name it car1 with the brand porsche, the model cayenne and a construction year of 2019

#creating object car1
class car:
    car_brand = "" 
    car_modelname = ""
    car_construction_year = 0


    car1 = car()
    car1.car_brand = "porsche"
    car1.car_modelname = "cayenne"
    car1.car_construction_year = 2019

    print (car1.car_brand)
    print(car1.car_modelname)
    print(car1.car_construction_year)

# constructor
class car:
    def __init__(self,incarbrand,incarmodelname,incar_constructionyear):
        self.car_brand = incarbrand
        self.car_modelname = incarmodelname
        self.car_construction_year = incar_constructionyear


# The new return printable function
    def __repr__(self):
    
        return ("Car brand is  " + self.car_brand +"car model is "+ self.car_modelname + "car constructed year is " + self.car_construction_year)

    


