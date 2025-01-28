# Best Practice 1:
# Because using a decorator literally changes which function is being called
# Python has added some special tools to make debugging and introspection 
# when using decorators much easier. Note the use of functools.wraps below. 
import functools
import random # we'll use this later

# Best Practice 2:
# Use the "unpacking" syntax to allow the decorator to accept any number of arguments
# and keyword arguments. Following this pattern allows decorators to be applied seamlessly
# to any function, regardless of what arguments it accepts. 

def simple_log(input_function):

    # Note functools.wraps and *args, **kwargs
    @functools.wraps(input_function)
    def wrapper(*args, **kwargs):
        print(f"About to call {input_function.__name__} with args={args} and kwargs={kwargs}")
        r = input_function(*args, **kwargs)
        print(f"Function {input_function.__name__} returned {r}")

        return r
    
    return wrapper

@simple_log
def add(a, b, c=0):
    return a + b + c

add(1, 2, c=3)
add(1, 2)

# Finally, decorators that accept arguments can also be made, but
# it requires an additional layer of nesting, which can be confusing.
# Here's an example of a decorator that uses the above best practices
# and repeats the function call a specified number of times and returns
# a list of the results:

# Note, the function "repeat" returns a decorator.
def repeat(n: int):

    def decorator(input_function):
        @functools.wraps(input_function)
        def wrapper(*args, **kwargs):
            r = []
            for _ in range(n):
                r.append(input_function(*args, **kwargs))
            return r
        
        return wrapper # return from decorator

    return decorator # return from repeat


# Note the syntax, repeat is INVOKED with 5, which returns a decorator.
# whereas in previous examples the decorator was not called (no parenthesis and no arguments). 
@repeat(5)
def five_random_integers(min: int=0, max: int=100):
    return random.randint(min, max)

print(five_random_integers(1,10))
print(five_random_integers(1,100))

# Micro-exercise: Add the logging decorator to the five_random_integers function
# in order to determine the order of operations for functions with multiple
# decorators. You will see that order matters, so experiment with placing the
# @simple_log decorator before and after the @repeat decorator.