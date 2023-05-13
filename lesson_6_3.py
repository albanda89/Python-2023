# Task 3 

"""
This is the task #3 of the lesson #6
"""

def sum_even_numbers(numbers):
    ''' This function calculates the sum of all even numbers in the given list'''
    if numbers is None:
        raise Exception('The list is None')

    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num

    return even_sum

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
result = sum_even_numbers(numbers)
print("Sum of even numbers: " + str(result))
print(sum_even_numbers.__doc__)
