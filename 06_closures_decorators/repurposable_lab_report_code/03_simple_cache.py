import timeit


def simple_cache(input_function):
    cache = {}

    def wrapper(n):
        if n in cache: return cache[n]

        r = input_function(n)
        cache[n] = r
        return r
    
    return wrapper


@simple_cache
def fib(n):
    if n <= 1: return 1
    return fib(n-1) + fib(n-2)


fib_time = timeit.timeit('fib(30)', number=200, setup="from __main__ import fib")
print(fib_time) # 3.398300032131374e-05