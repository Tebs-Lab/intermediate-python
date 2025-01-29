class Averages:
    '''
    A class that calculates the mean and median of a list of numbers.
    '''
    def __init__(self, input_data: list[float]):
        '''
        A shallow copy of the input numbers is made and stored 
        as self.data.

        :param list[float] input_data: A list of numbers.
        '''
        self.data = input_data.copy()

    def mean(self) -> float:
        '''
        :return float: The mean of the copied input data.
        '''
        return sum(self.data) / len(self.data)

    def median(self) -> float:
        '''
        :return float: The median of the copied input data
        '''
        n = len(self.data)
        sorted_list = sorted(self.data)

        # No elements, no median
        if n == 0:
            return None
        # Even case
        elif n % 2 == 0:
            a = sorted_list[n // 2]
            b = sorted_list[n // 2 - 1]
            return (a + b) / 2
        # Odd case
        else:
            return sorted_list[n // 2] # Note: Integer division is needed for odd n