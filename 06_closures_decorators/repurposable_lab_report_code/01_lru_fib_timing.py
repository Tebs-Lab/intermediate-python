from functools import lru_cache
import timeit

def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

@lru_cache()
def cached_fib(n):
    if n <= 1:
        return 1
    return cached_fib(n-1) + cached_fib(n-2)



fib_time = timeit.timeit('fib(30)', number=200, setup="from __main__ import fib")
cached_fib_time = timeit.timeit('cached_fib(30)', number=200, setup="from __main__ import cached_fib")

print(f'Uncached: {fib_time}\nCached: {cached_fib_time}')