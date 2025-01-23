# Type hinting is a feature added to Python in 3.5 that allows
# you to specify the type of a variable, function argument, and return value.
# These hints are not enforced (more on that later) but they are used
# by documentation tools and IDEs to provide better code completion and
# documentation.

# The most common use of type hinting is in function definitions.
# here, a is expected to be an int and b is expected to be a float
# and the function is expected to return a float.
def example(a: int, b: float) -> float:
    return a * b

# However, type hints are not enforced by Python itself. 
# Note that this code works, even though it should not.
x = example(2, 'oops') 
print(x)

# The history of type hinting is deeply connected to the most
# popular static type-checking package for Python: mypy. In your terminal
# try installing mypy to your virtual env then running it on this file:
'''
pip install mypy
mypy 04_classes_3/01_type_hints.py
'''
# You should see an error message when you do so, related to line 15 above.
# This type of "static type checking" can catch a huge number of bugs before runtime 
# and is a major motivator of type hints in Python.

# micro-exercise: fix the type error on line 15, then rerun mypy 
# to see the output for an "error free" run.

# For complex data types, the hinting syntax is more complex.
def list_product(numbers: list[float]) -> float:
    product = 1
    for n in numbers:
        product *= n
    return product

# If you're using key word arguments the syntax looks like this:
def example_two(a: int, b: float = 2.0) -> float:
    return a * b


# The typing module provides additional tools for type hinting.
# One such example is the "any" type, where you can explicitly specify
# a variable that might have a wide variety of types.
# Or you can use "Union" to specify that a variable can be one of several types.
from typing import Any, Union

def list_contains(items: list[Any], target: Any) -> bool:
    return target in items

def fancy_math(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return (a * b) + a**b

# Type hinting can also be used with classes and class methods.
class Example:
    # By convention, __init__ should always be annotated to return None: 
    # https://peps.python.org/pep-0484/
    def __init__(self, x: int) -> None:
        # Notice we are also type hinting the instance variable x.
        self.x: int = x

    def double(self) -> int:
        return self.x * 2
    
Example(5)
Example(5.0)


# Classes can also be type hinted like this:
from typing import ClassVar

class ExampleTwo:
    # Variables declared here, but not assigned a value, will be 
    # considered instance variables
    instance_var: int
    another_instance_var: str

    # Variables declared here, and assigned a value, will be considered
    # class variables. You may additionally use the ClassVar type hint to 
    # make this more explicit. (there is also a class variable annotation)
    class_var: str = "class variable"
    class_var_two: ClassVar[int] = 10

    def __init__(self, instance_var: int, another_instance_var: str) -> None:
        self.instance_var = instance_var
        self.another_instance_var = another_instance_var


x = ExampleTwo(5, "five")
print(x.instance_var, x.another_instance_var, x.class_var, x.class_var_two)
print(ExampleTwo.class_var, ExampleTwo.class_var_two)



# There are LOTS of other tools in the typing module. Consider reading pep-0484 for more details.
# Here are two last handy examples
from typing import Iterable, Callable

# Anything that is "iterable" can be used in a for loop.
def loop_example(items: Iterable) -> None:
    for item in items:
        print(item)

# Anything "callable" can be executed like a function.
def call_example(func: Callable) -> None:
    func()


# Finally, global variables can also be type hinted directly.
for_example: float = 25.25

# But for a true example of absurdity, these can also be completely ignored
example_two: str = 1

# Micro-exercise: Use mypy to identify and fix all the type errors in this file.