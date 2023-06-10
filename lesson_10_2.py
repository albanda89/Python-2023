## Task 2 
# Write a Python lambda function that takes two parameters a and b, 
# and returns the sum of their squares. Assign the lambda function to a variable called sum_of_squares. 
# Test the lambda function by passing different values for a and b.

# Writing lambda function that takes two parameters a and b, and adding suar of each
sum_of_squares = lambda a, b: a**2 + b**2

# Testing the lambda function
result = sum_of_squares(1, 2)
print(result)  # Output: 5

result = sum_of_squares(4, 5)
print(result)  # Output: 41

result = sum_of_squares(3, 2)
print(result)  # Output: 13
