from time import process_time

def timeit(function):
    def wrapper():
        t1_start = process_time() 
        function()
        t1_stop = process_time()
        exec_time= t1_stop-t1_start
        print('Execution time is: ' + str(exec_time))
    return wrapper

@timeit
def hello(name):
    print('Hello ' + name)

hello('Suresh')

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
        
        if isinstance(num, int):
            raise Exception('List should have only integers')

        if num % 2 == 0:
            even_sum += num

    return even_sum

numbers = [1,'a',2]
result = sum_even_numbers(numbers)
print("Sum of even numbers: " + str(result))
print(sum_even_numbers.__doc__)

