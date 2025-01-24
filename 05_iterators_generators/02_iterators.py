# Iterators are objects that implement a few dunder methods
# which then allow them to be used in loops and with the next()
# function. They are somewhat more flexible than generators, but
# also a bit clunkier to build (and must be built as a class).

# Here's a simple example where we more-or-less replicate the range() function:
class CountByN:
    def __init__(self, start: int=0, end: int=None, increment_by: int=1):
        self.increment_by = increment_by
        self.current = start
        self.end = end

    # __iter__ is required to be implemented for iterators.
    # most often you just return self, although in some cases
    # you might return a different object.
    def __iter__(self):
        return self

    # __next__ is required to be implemented for iterators.
    # each time it is called, it should return the next value
    # as well as perform any "incrementing" steps.
    def __next__(self):
        r = self.current
        self.current += self.increment_by

        # Unlike generators, we have to explicitly raise the StopIteration
        # exception whenever this iterator should stop.
        if self.end is not None and self.current > self.end:
            raise StopIteration

        return r
    

for i in CountByN(0, 10, 2):
    print(i)


# Python also has an abstract class for iterators, which can be used
# to simplify our own iterator class (by leaving off the __iter__ method)
from collections.abc import Iterator

# This implementation is functionally identical to the above
class IterTwo(Iterator):
    def __init__(self, start: int=0, end: int=None, increment_by: int=1):
        self.increment_by = increment_by
        self.current = start
        self.end = end

    def __next__(self):
        r = self.current
        self.current += self.increment_by

        if self.end is not None and self.current > self.end:
            raise StopIteration

        return r
    
# For iterators that would otherwise infinite, you can use 
# the range() and next functions:
iterator_instance = CountByN(0, increment_by=50)
for _ in range(20):
    print(next(iterator_instance))

# Micro-Exercise: write an iterator class that iterates over the Fibonacci sequence.
