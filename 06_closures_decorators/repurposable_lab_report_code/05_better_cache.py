import functools


def better_cache(input_function):
    cache = {}

    @functools.wraps(input_function)
    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items()))) 
        if cache_key in cache: 
            r = cache[cache_key]
            print(f'HIT {cache_key} -> {r}')
        else:
            r = input_function(*args, **kwargs)
            cache[cache_key] = r
            print(f'MISS, adding {cache_key} -> {r}') # For debugging

        return r

    return wrapper


@better_cache
def tester(a, b, c=0, d=0):
    return a + b + c + d

tester(1, 2)           # MISS
tester(1, 2)           # HIT
tester(1, 2, c=0)      # MISS!! (see the writeup below)
tester(1, 2, c=0)      # HIT
tester(1, 2, c=5)      # MISS
tester(1, 2, c=5)      # HIT
tester(1, 2, d=4, c=5) # MISS
tester(1, 2, c=5, d=4) # HIT (even with swapped order of c and d)