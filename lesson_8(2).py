# Exercies 
# Create a function that prints out every element of an integer list incremented by four!
lst = [1,4,5,6]
def increment_by_four(lst):
    for numb in lst:
        new_numb = numb+4
        print (new_numb) 
increment_by_four(lst)


# Exercise
# 1.Write a class called student which stores the name of the students and their age

# The student class
class Student:
    name = ""
    age = 0

# the student tom
tom = Student()
tom.name = "Tom"
tom.age = 24

# testing it
print(tom.name)
print(tom.age)

# constructor
class student:
    def __init__(self,inname,inage):
        self.name = inname
        self.age = inage

# The new return printable function
    def __repr__(self):
    
        return ("Name of the student is " + self.name +"and age of the student is "+ self.age)
