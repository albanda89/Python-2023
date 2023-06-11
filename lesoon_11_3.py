# Exercise 3: Special Methods - Rectangle
# 1. Create a class called Rectangle with attributes width and height. Implement the
# __str__() and __eq__() special methods for the Rectangle class. Test the string
# representation and equality comparison of Rectangle objects.


class  Rectangle :
    def __init__ (self,  width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __eq__(self, other):
        return (
            type(other) == Rectangle
            and self.width == other.width
            and self.height == other.height)

#first try
# Create two Rectangle objects
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(4, 5)

# Test string representation
print(rectangle1)

# Test equality comparison
print(rectangle1 == rectangle2)

