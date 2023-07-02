num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

def add_numbers(num1, num2):
    results = num1 + num2
    return results

sum_of_numbers = add_numbers(num1, num2)
print("Sum of the numbers: " + str(sum_of_numbers))