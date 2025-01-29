from typing import Any

def duplicates(input_list: list[Any]):
    '''
    Given a list of items, return a list with one copy of the items that
    appear more than once. The order of the duplicate elements should be the
    same as the order they appear in the list. So:

    duplicates([1, 2, 3, 1, 2]) -> [1, 2]
    duplicates([2, 1, 3, 1, 2]) -> [2, 1]

    :param list[Any] input_list: A list of items to check for duplicates.

    :return list[Any]: A list of items that appear more than once in the input list.
    '''
    return_list = []
    for i, item in enumerate(input_list):
        if item in input_list[i+1:] and item not in return_list:
            return_list.append(item)

    return return_list


def is_anagram(string_a: str, string_b: str):
    '''
    Given two strings, return True if they are anagrams of each other, False otherwise.
    
    Anagrams are strings containing the same set of letters with the same count of each
    letter. abc and cba are anagrams, as are abba and baab. aab is not an anagram of bba.

    :param str string_a: The first string to compare.
    :param str string_b: The second string to compare.

    :return bool: True if the strings are anagrams, False otherwise.
    '''
    counter = {}

    for c in string_a:
        if counter.get(c) == None:
            counter[c] = 0
        
        counter[c] += 1

    for c in string_b:
        if counter.get(c) == None:
            counter[c] = 0
        
        counter[c] -= 1

    for c, count in counter.items():
        if count != 0:
            return False
    
    return True