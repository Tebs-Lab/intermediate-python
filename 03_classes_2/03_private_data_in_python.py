# Most OOP languages have a concept of "private" data.
# Private data should only be modified by code that is 
# inside the class definition. Having some data makes
# the system more predictable and debuggable because 
# there are a limited number of places where a given 
# pice of data can be changed. 

# Many languages further distinguish between "private" and "protected" data 
# where private data should only every be read OR written inside the class
# definition. Protected data can be read anywhere, but only written inside 
# class. Public data can be read or written anywhere. 

# Python's support for private data is limited compared to 
# other languages. There are basically 3 tools:
class PrivateDataDemo:
    def __init__(self):
        # Tool 1: Naming conventions and trust. In Python it is well 
        # established that any variable starting with an underscore 
        # should be treated as private. 
        self._private_convention = "This data is 'private' but only by convention."

        # Tool 2: Name Mangling. This adds one level of additional safety
        # to the standard naming conventions. Any variable starting with TWO
        # underscores will have "Name Mangling" applied to it. (Demo below)
        self.__private_mangled = "This data is 'private' and there is a light enforcement mechanism."

        # Tool 3: "properties". To make this instance variable a property we'll add methods below.
        # That code will shadow the variable itself, allowing us to define specific behavior for
        # "getting" the variable and "setting" the variable. In this example we use name mangling as well
        # to denote that this specific variable is private, but we expose it with public functions below
        self.__protected_property = "This data is managed by functions defined below to behave as a 'protected' variable."
    
    @property
    def protected_property(self):
        # Notice that inside the class definition I do not need to use or know the "mangled" version
        # of the name.
        return self.__protected_property
    
    @protected_property.setter
    def protected_property(self, new_value):
        # One reason to control variable access like this is type safety and enforcement.
        if not isinstance(new_value, str): 
            raise TypeError(f"protected_property must be a string, got {new_value}, {type(new_value)}")
        self.__protected_property = new_value


x = PrivateDataDemo()

# Note that I *can* but *shouldn't* do the following:
print(x._private_convention)
x._private_convention = 10
print(x._private_convention)

# The name mangled variable isn't directly accessible...
# print(x.__private_mangled) # AttributeError!

# But... if we introspect on the object we'll find something called
# _PrivateDataDemo__private_mangled
print(dir(x))
print(x._PrivateDataDemo__private_mangled)

# So I still can, but definitely shouldn't, do the following:
x._PrivateDataDemo__private_mangled = 10
print(x._PrivateDataDemo__private_mangled)

# Finally, using properties lets us use the method name like it's a variable
# and the proper method will be called.
print(x.protected_property) # note that the @property method is called.
x.protected_property = "this is a different string"
print(x.protected_property)
x.protected_property = 10 # Raises our type error.

# Micro-exercise: Below is a class with two private variables. 
# Extend the class using properties so that one of the private 
# variables is "read only" (aka protected) and modify the other 
# so that it has public setter.
class MicroExercise:
    def __init__(self):
        self.__privateOne = "Look ma, some data!"
        self.__privateTwo = "Look pa, other data!!"


# Write some code here that will test your implementation.
