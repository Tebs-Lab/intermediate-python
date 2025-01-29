def count_characters(input_string: str) -> dict[str, int]:
    '''
    This function takes a string as input and returns a dictionary with the 
    count of each character in the string.

    :param input_string str: The input string
    :return dict[str, int]: A dictionary with the count of each character in the string
    '''
    return_value = {}

    for c in input_string:
        if return_value.get(c) == None:
            return_value[c] = 0
        else:
            return_value[c] += 1

    return return_value


def most_and_least_common(input_list):
    '''
    Returns a tuple with exactly two items. 

    The first item is the one that appears the MOST number of times in the provided input. 
    The second item should be the item that occurs the FEWEST number of times in the provided input.

    The returned list can contain two of the same value, for example
    [1,1,1,1] -> (1, 1), because 1 is the most and least occurring item.

    If there are ties this function returns the value that appears
    in the input list first.
    For example: 
    * [1, 1, 2, 2] -> (1, 1)
    * [2, 2, 1, 1] -> (2, 2)

    If the input list is empty, return the tuple (None, None).
    '''
    if len(input_list) == 0:
        return []

    counter = {}
    for item in input_list[::-1]:
        if counter.get(item) == None:
            counter[item] = 0
        
        counter[item] += 1
    
    # These values are chosen to be impossible so that 
    # the initial comparisons will always be True
    min_count = len(input_list) + 1
    min_value = None
    max_count = 0
    max_value = None

    for item, count in counter.items():
        if count < min_count:
            min_count = count
            min_value = item

        if count > max_count:
            max_count = count
            max_value = item

    return max_value, min_value