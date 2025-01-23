import functools
import logging
import sys

# This turns on info level logging and logs to standard out
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def log(input_function):

    functools.wraps(input_function)
    def wrapper(*args, **kwargs):
        logging.info(f'{input_function} called with args: {args} and kwargs: {kwargs}')
        r = input_function(*args, **kwargs)
        logging.info(f'{input_function} returned {r}')
        return r

    return wrapper


def repeat(input_function):
    
    functools.wraps(input_function)
    def wrapper(*args, **kwargs):
        r1 = input_function(*args, **kwargs)
        r2 = input_function(*args, **kwargs)
        return r1, r2
    
    return wrapper

@log
@repeat
def add(a, b):
    return a + b


@repeat
@log
def sub(a, b):
    return a + b


r = add(1, 2)
print(f"Final value for r: {r}")

print('\n=====\n')

r2 = sub(1, 2)
print(f"Final value for r2: {r2}")