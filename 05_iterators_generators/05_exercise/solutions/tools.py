from collections.abc import Iterable

def is_sorted(data: list):
    for index, value in enumerate(data):
        # Can't compare the last element with the next one
        if index == len(data) - 1: break 

        if data[index - 1] > value:
            return False
        
    return True

def vector_add(a: list[float], b: list[float]):
    # For fun, I used a list comprehension.
    return [a[i] + b[i] for i in range(len(a))]