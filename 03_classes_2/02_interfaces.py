import math

# One of the most popular uses for inheritance is to define 
# an "abstract" class that defines a strict interface for 
# child classes to follow, without providing any implementation details.
# Python provides some tools for doing this including the 
# "Abstract Base Class" and "@abstractmethod" decorator
from abc import ABC, abstractmethod

# Shape2D is an "abstract class" or an "interface": it defines 
# methods that should always be implemented in it's child classes
# but does not define any particular implementation details for 
# the child classes. 
class Shape2D(ABC):
    @abstractmethod
    def perimeter():
        pass

    @abstractmethod
    def area():
        pass

# Anything that inherits from Shape2D must implement each of the
# abstract methods defined in Shape2D. For example the following fails:
class BadCircle(Shape2D):
    def __init__(self, radius):
        self.radius = radius

# c = BadCircle(4) # TypeError because BadCircle doesn't implement the abstract methods.

# Let's do it right now:
class Circle(Shape2D):
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return math.pi * 2 * self.radius
    
    def area(self):
        return math.pi * (self.radius ** 2) # ** is "to the power of" in Python
    

c = Circle(4)
print(c.perimeter())
print(c.area())

# Mini-Exercise: Pick your favorite shape and and 
# properly extend the Shape2D class for that shape.