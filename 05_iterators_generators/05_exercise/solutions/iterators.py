from collections.abc import Iterable, Iterator

class Squares(Iterator):
    def __init__(self, n: int):
        self._current = 1
        self._n = n

    def __next__(self):
        if self._current > self._n:
            raise StopIteration
        
        r = self._current ** 2
        self._current += 1

        return r
    
class MultipleIterator(Iterator):
    def __init__(self, iterable: Iterable, n: int):
        self._list = list(iterable)
        self._n = n
        self._current_repeat = 0
        self._current_index = 0

    def __next__(self):
        if self._current_repeat == self._n:
            raise StopIteration
        
        r = self._list[self._current_index]
        self._current_index += 1

        if self._current_index == len(self._list):
            self._current_repeat += 1
            self._current_index = 0

        return r

# The first 5 squares, repeated 4 times
print(list(MultipleIterator(Squares(5), 4)))