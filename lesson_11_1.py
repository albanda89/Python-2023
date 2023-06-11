# Exercise 1: Closure - Calculator
# Create a closure function called calculator that performs basic arithmetic operations. The closure
# should return a function that takes two numbers and performs a specified operation on them.

def calculotor_clou ():
    def operate( num1,num2, opertn):
        if opertn == " + ":
            return num1 + num2
        elif opertn == " - ":
            return num1 - num2
        elif opertn == " * ":
            return num1 * num2
        elif opertn == " / ":
            return num1 / num2
        else:
            return ("Value Error ")

    return operate

calculotor_clouser = calculotor_clou()

result1 = calculotor_clouser(5, 3, " + " )
print(result1)



result2 = calculotor_clouser(100, 188888, " + " )
print(result2)

