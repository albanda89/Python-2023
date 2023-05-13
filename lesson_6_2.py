# Task 2 

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
def hello_executed_time():
    print("Hello! ")

hello_executed_time()

