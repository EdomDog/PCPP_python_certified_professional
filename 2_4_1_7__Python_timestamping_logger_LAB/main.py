'''
CHAPTER:
    2.4.1.7 Lab - timestamping logger

Estimated time
    15-30 minutes

Level of difficulty
    Medium

Objectives
    Improving the student's skills in creating decorators and operating with them.
Scenario
    Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
    Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
    Apply your decorator to those functions to ensure that the time of the function executions can be monitored.

Hint
    To print the current time, you could use the following code:

    # import module responsible for time processing
        from datetime import datetime

    # get current time using now() method
    timestamp = datetime.now()

    # convert timestamp to human-readable string, following passed pattern:
    string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    print(string_timestamp)

'''
# Sebastian Faber, 25.09.2024

from datetime import datetime

# Decorator
def print_timestamp(func):
    def wrapper(*args, **kwargs):
        # Get timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       
        # Call base function
        result = func(*args, **kwargs)        

        # output        
        func_name=(func.__name__).ljust(9," ")
        return(f"print_timestamp: {func_name}\ttime: {timestamp}: {result} ")
    return wrapper

# add two numbers
@print_timestamp
def add(a, b):
    return a + b

# multiply two numbers
@print_timestamp
def multiply(a, b):
    return a * b

# substrace two numbers
@print_timestamp
def substract(a, b):
    return a - b

# Testing
if __name__ == "__main__":
    result1=add(3,4)
    result2=multiply(3,4)
    result3=substract(3,4)

    print(result1)
    print(result2)
    print(result3)



