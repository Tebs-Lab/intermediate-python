# Classes can be given properties that are tracked by the class itself
# rather than instances of the class. This is useful for things like 
# constants that all instances of the class should share, and also for 
# maintaining state that is shared across all instances of the class.

# Here's an example of the "singleton" pattern -- where only one instance
# of a given class should ever be created. This is useful for things like
# shared logging objects, shared database connections, etc.

class Singleton:
    # This is a class property, not an instance property.
    # instances may access the property, and it can be accessed using 
    # the class name as well.
    _instance = None

    # __new__ is always called before __init__ and actually creates the 
    # instances of classes. The new instance is ultimately passed to __init__
    # to be initialized and then returned.
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance
        
    
    def __init__(self):
        assert self is Singleton._instance

# Here's a simple test to show that only one instance of Singleton is ever created.
a = Singleton()
b = Singleton()
print(a is b)
print(a is Singleton._instance)
print(b is Singleton._instance)
print(a is a._instance)
print(b is b._instance)
print(a is b._instance)

# Note that: using patterns similar to singletons you can also create a "factory" pattern
# that sets a limit on how many instances of a class can exist at once. This is 
# very useful for e.g., managing subprocesses and database connections.

# Another useful class property is a constant. This is a value that should never
# change and is relevant to all instances of the class.
class Circle:
    PI = 3.14159

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def circumference(self) -> float:
        return 2 * self.PI * self.radius
    
    def area(self) -> float:
        return self.PI * self.radius ** 2
    
c = Circle(1)
print(c.PI)
print(Circle.PI)

# Micro-exercise: Take 2 minutes and come up with another example of when a 
# class property might be useful. 