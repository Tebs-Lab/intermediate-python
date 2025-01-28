# We're using this timing module later in the script...
import timeit

# Python allows us to create decorators that can be used to modify the behavior of functions.
# These decorators are fundamentally based on closures and first class functions. In their simplest
# form a decorator is a function that takes a function as an argument, and returns a new function
# that has additional behavior that occurs before or after the input function is called.

# Here's an example of a decorator that performs "caching" by saving previous
# results of a function in a dictionary, and returning the cached result if the
# function is called with the same argument again.
def simple_cache(input_function):
    cache = {}

    def wrapper(n):
        if n in cache: return cache[n]

        r = input_function(n)
        cache[n] = r
        return r
    
    return wrapper


# When we "decorate" this function fib with the @simple_cache decorator, behind the scenes 
# our simple_cache function is called with fib as an argument. The result is that any time
# we call fib, an instance of the function we call "wrapper" on line 15 is actually called.
@simple_cache
def fib(n):
    if n <= 1: return 1
    return fib(n-1) + fib(n-2)


# This is the same code, but not decorated. 
def fib_natural(n):
    if n <= 1: return 1
    return fib_natural(n-1) + fib_natural(n-2)


fib_time_natural = timeit.timeit('fib_natural(25)', number=200, setup="from __main__ import fib_natural")
print(fib_time_natural)

fib_time = timeit.timeit('fib(25)', number=200, setup="from __main__ import fib")
print(fib_time) 

# Mini-exercise: Create a decorator that prints the return value of a function
# each time it is called, then decorate fib_natural with your decorator to test 
# the output.
# Note: you will want to comment out the above timing before testing your own decorator!