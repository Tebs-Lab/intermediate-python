# Docstrings are a standardized way to add documentation to your code.
# The conventions for them are set forth in pep-0257:
# https://peps.python.org/pep-0257/

# The most common use of docstrings is to document functions and classes.
# There are numerous tools (including ones built into your IDE) for surfacing 
# doc strings, or creating automatic reference documentation from the contents
# of docstrings. 

# In general, docstrings should contain:
# 1) A summary of the function or class.
# 2) A description each of the parameters.
# 3) A description of the return value.

def example_function(a: int, b: float) -> float:
    '''
    This function multiplies two numbers together.
    
    Parameters:
    a (int): The first number to multiply.
    b (float): The second number to multiply.
    
    Returns:
    float: The product of a and b.
    '''
    return a * b

# Class docstrings should, at minimum, describe the purpose of the class.
# but it is also considered good practice to document the methods and attributes.
class Rectangle:
    '''
    This is an example of a class docstring. It describes the purpose of the class.
    In this case, the class is an example of proper documentation. It is also a
    representation of a rectangle, which has a width and a height and methods for
    computing the area and perimeter.

    Attributes
    ----------
    height : float
        The height of the rectangle.
    width: float
        The width of the rectangle.

    Methods
    -------
    perimeter() -> float:
        Returns the perimeter of the rectangle.
    area() -> float:
        Returns the area of the rectangle.
    '''

    def __init__(self, height: float, width: float) -> None:
        '''
        Initializes the rectangle with the given height and width.

        Parameters
        ----------
        height : float
            The height of the rectangle.
        width: float
            The width of the rectangle.
        '''
        self.height = height
        self.width = width

    def perimeter(self) -> float:
        '''
        Returns the perimeter of the rectangle.

        Returns
        -------
        float
            The perimeter of the rectangle.
        '''
        return 2 * (self.height + self.width)
    
    def area(self) -> float:
        '''
        Returns the area of the rectangle.

        Returns
        -------
        float
            The area of the rectangle.
        '''
        return self.height * self.width
    
# Micro-exercise:
# One example of a tool that uses docstrings is pydoc, which comes built
# into Python. For example, run these command in your terminal 
'''
python -m pydoc 04_classes_3/03_docstrings.py
python -m pydoc -w 04_classes_3/03_docstrings.py
'''

