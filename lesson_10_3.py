## clear Task 3 
## Write a Python function called calculate_average that accepts a variable number of arguments (numbers) 
## and returns the average of those numbers. 
## Test the function with different sets of numbers.

## Writing lambda function that accepts number of argument and returns the average
 
def calculate_average(*args):
    if len(args) == 0:
        return 0
    else:
        return sum(args) / len(args)

# Testing the function
result = calculate_average(1, 2, 3, 4, 5)
print(result)  # Output: 3.0





