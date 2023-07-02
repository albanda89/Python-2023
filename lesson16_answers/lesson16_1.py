class InvalidInputError(Exception):
    pass

def divide_numbers(num1, num2):
 
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero. Please enter a non-zero value.")
            
    result = num1 / num2
    return result
           

def main(num1=None):

    try:
        if num1 is None:
            num1 = int(input("Enter the first number: "))
        
        num2 = int(input("Enter the second number: "))

        result = divide_numbers(num1, num2)
        print("Result:", result)    

    except ValueError:
        print("Invalid input. Please enter an integer.")
        main()
        
    except ZeroDivisionError as e:
        print(e)
        main(num1)


if __name__ == '__main__':
    main()