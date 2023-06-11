# Exercise 2: Decorators - Timer
# Write a decorator function called timer that measures the execution time of a function and prints the
# elapsed time. Apply the timer decorator to a function of your choice and test its functionality.

import time

def timer_decorator(funct_2):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = funct_2(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} s")
        return result
    return wrapper


# Define a function to test the timer decorator
@timer_decorator
def calculate_elapse( a):
    print ("good job " + a )

# Call the function to test the timer decorator
calculate_elapse( "Aruni")
