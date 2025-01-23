import functools

def proper_decorator(input_function):

    @functools.wraps(input_function)
    def wrapper(*args, **kwargs):
        # Do stuff before the function call...
        r = input_function(*args, **kwargs)
        # Do stuff after the function call...
        return r
    
    return wrapper

