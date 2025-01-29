import pytest
from functions import count_characters, most_and_least_common

# The error in count_characters is that every character count is off by one.
# Instead of starting at 0, the count should start at 1. In our solution we
# simply removed the "else" so the += 1 is always executed (including the first time)
def test_count_characters():
    assert count_characters('hello') == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert count_characters('hello world') == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    assert count_characters('') == {}

# There were two errors in most_and_least_common. The first error was that the 
# empty list was being returned instead of (None, None) when the empty list was
# passed in a san argument. The second error was that when ties were evaluated, the
# LAST tied item in the input was being returned instead of the FIRST item. 
def test_most_and_least_common():
    assert most_and_least_common([1, 2, 3, 4, 5]) == (1, 1)
    assert most_and_least_common([1, 1, 2, 2, 3, 3]) == (1, 1)
    assert most_and_least_common([1, 1, 2, 2, 3, 3, 3, 3, 3]) == (3, 1)
    assert most_and_least_common([]) == (None, None)

if __name__ == '__main__':
    pytest.main([__file__])