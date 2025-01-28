import time
import functools

def timer(input_function):

    @functools.wraps(input_function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = input_function(*args, **kwargs)
        end = time.time()
        print(f"Function {input_function.__name__} took {end-start} seconds to run.")
        return result
    return wrapper


@timer
def slow_function(n):
    return fib(n)

# Decorating fib directly would get really verbose
# because the recursive calls would ALL be timed. 
def fib(n):
    if n <= 1: return 1
    return fib(n-1) + fib(n-2)

slow_function(1)
slow_function(20)
slow_function(30)