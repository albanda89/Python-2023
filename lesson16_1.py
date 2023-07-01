class InvalidInputError(Exception):
    pass

def divide_numbers():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero. Please enter a non-zero value.")
            
            result = num1 / num2
            print("Result:", result)
            break
        
        except ValueError:
            print("Invalid input. Please enter an integer.")
        
        except ZeroDivisionError as e:
            print(e)
        
        except InvalidInputError as e:
            print(e)


# Testing the function
divide_numbers()
