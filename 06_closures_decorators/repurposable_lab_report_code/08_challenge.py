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

def size_limited_cache(maxsize=20):

    def decorator(input_function):
        cache = {}

        @functools.wraps(input_function)
        def wrapper(*args, **kwargs):
            cache_key = (args, tuple(sorted(kwargs.items()))) 
            if cache_key in cache: 
                r = cache[cache_key]
                print(f'HIT {cache_key} -> {r}')
            else:
                r = input_function(*args, **kwargs)

                if len(cache) < maxsize:
                    cache[cache_key] = r
                    print(f'MISS, adding {cache_key} -> {r}')
                else:
                    print(f'MISS, {cache_key} but cache at maxsize.')

            return r

        return wrapper
    
    return decorator



@size_limited_cache(maxsize=5)
@repeat
@log
def add(a, b):
    return a + b


add(1,2)
add(1,2)


'''
Logs and prints:

INFO:root:<function add at 0x1032f4c10> called with args: (1, 2) and kwargs: {}
INFO:root:<function add at 0x1032f4c10> returned 3
INFO:root:<function add at 0x1032f4c10> called with args: (1, 2) and kwargs: {}
INFO:root:<function add at 0x1032f4c10> returned 3

MISS, adding ((1, 2), ()) -> (3, 3)
HIT ((1, 2), ()) -> (3, 3)

Commentary:

Since @log decorates the initial function, everything that 
prints via the logger is specific to the raw add function. 

@repeat decorates the logged version of add, so when we call
it the first time we see 2 identical sets of log entries.

@size_limited_cache decorates the repeated-and-logged function.
This explains two things: 

1) The cached return value is (3, 3) because @repeat returns a 
   tuple with both return values.

2) The second invocation of the function doesn't log anything.
   The cache "hits" on the arguments, so the repeated-and-logged 
   version of the function is not ever called -- we just return
   the saved return value.

Hopefully this demonstrates the importance of decorator order when 
you choose to use more than one at a time.
'''