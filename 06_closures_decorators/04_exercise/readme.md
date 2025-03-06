# Decorators Exercise

In this exercise you'll build two simplified versions of popular real-world decorators. One is a utility to time and report how long a function takes to execute, the other is a miniature version of the `lru_cache` decorator from the `functools` module. 

## Part 1: Timing A Function

Create a decorator that tracks and prints the amount of time a function took to execute.

* Use the built in `time` module, specifically `time.time()` to get the current time in seconds as a floating point number.
    [https://docs.python.org/3/library/time.html#time.time](https://docs.python.org/3/library/time.html#time.time)
* Measure the time before the function starts executing.
* Measure the time when it finishes.
* Compute the difference and print it. 

## Part 2: Caching

Create a decorator that adds a size limited cache to any function, such that:

* The maximum number of entries to the cache can be specified as an argument to the decorator. 
* Function calls are cached by mapping the arguments to the return value.
    * Calls to the function that are already in the cache should NOT invoke the function but should instead return the previously cached result.
* Only caches the first `n` unique calls to the function, then stops expanding the cache. 
* Bonus points: implement an eviction strategy such that calls to the function past the specified `n` delete the least recently used cache entries and make room for new ones. 