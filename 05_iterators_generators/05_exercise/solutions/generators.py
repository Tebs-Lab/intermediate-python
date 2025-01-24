from collections.abc import Iterable

def squares(n: int):
    for i in range(1, n+1):
        yield i*i

def multiple_iter(iterable: Iterable, n: int):
    listified_iterable = list(iterable)
    for _ in range(n):
        for i in listified_iterable:
            yield i

print(list(multiple_iter(squares(5), 4))) # the first 5 squares, repeated 4 times.