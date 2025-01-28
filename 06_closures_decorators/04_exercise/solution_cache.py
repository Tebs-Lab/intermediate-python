import functools
from heapq import heappop, heappush
from time import time

def size_limited_cache(maxsize: int = 20):
    '''
    This decorator will cache the results of the function it decorates, 
    up to a specified maximum number of results. If the cache is full,
    items will be evicted in a least-recently-used manner. Function parameters
    must be hashable for this decorator to work properly.

    :param maxsize int: The maximum number of items to cache. Default is 20.
    '''

    def decorator(input_function):
        cache = {}
        last_used_pqueue = []

        # This helper function updates an lru key in the last_used_pqueue
        # this is called on a cache hit. 
        def update_used(cache_key):
            nonlocal last_used_pqueue
            for timestamp, key in last_used_pqueue:
                if key == cache_key:
                    last_used_pqueue.remove((timestamp, cache_key))
                    break
            new_lru_key = (time(), cache_key)
            heappush(last_used_pqueue, new_lru_key)

        # This is the actual decorator that gets returned.
        @functools.wraps(input_function)
        def wrapper(*args, **kwargs):
            cache_key = (args, tuple(sorted(kwargs.items())))
            lru_key = (time(), cache_key) # heapq uses the first element of the tuple to sort
            
            if cache_key in cache: 
                r = cache[cache_key]
                update_used(cache_key)
                print(f'HIT {cache_key} -> {r}')
            else:
                r = input_function(*args, **kwargs)

                if len(cache) < maxsize:
                    cache[cache_key] = r
                    heappush(last_used_pqueue, lru_key)
                    print(f'MISS, adding {cache_key} -> {r}')
                else:
                    evicted = heappop(last_used_pqueue)
                    del cache[evicted[1]]
                    cache[cache_key] = r
                    heappush(last_used_pqueue, lru_key)
                    print(f'MISS, {cache_key} but cache at maxsize. Evicted {evicted}.')

            return r

        return wrapper
    
    return decorator


@size_limited_cache(maxsize=5)
def tester(a, b, c=0, d=0):
    return a + b + c + d


# Crude test code to demo the maxsize
# Note that this is the worst case scenario for the cache
# which will always end up evicting the oldest item right
# before that item is used. 
for _ in range(3):
    for i in range(6):
        tester(i, i)

# Here's a more interesting scenario to test:
for _ in range(4):
    for i in [1, 2, 3, 4, 1, 5, 6]:
        tester(i, i)

# Overall, a lesson for lru caching is that it works best
# when there is a high degree of temporal locality in the 
# use pattern.