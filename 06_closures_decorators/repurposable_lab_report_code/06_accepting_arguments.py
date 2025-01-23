import functools


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
def tester(a, b, c=0, d=0):
    return a + b + c + d


# Crude test code to demo the maxsize
for _ in range(3):
    for i in range(6):
        tester(i, i)