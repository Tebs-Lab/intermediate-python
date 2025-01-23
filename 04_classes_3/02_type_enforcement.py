# You may wish to add enforcement to your type hints, that is
# you may want functions that are used improperly to raise errors
# rather than attempt to run.

# Two popular (production ready) options for this are pydantic and beartype. 
# Lets look at some examples.
'''
pip install beartype pydantic
'''

# The simplest way to validate type hints with both libraries
# is by using a decorator.
from pydantic import validate_call
from beartype import beartype

@validate_call
def enforced_via_pydantic(a: int, b: float) -> float:
    return a * b

# enforced_via_pydantic("wrong", 2.0) # ValidationError (unique error from pydantic package.)

@beartype
def enforced_via_beartype(a: int, b: float) -> float:
    return a * b

# enforced_via_beartype("wrong", 2.0) # BeartypeCallHintParamViolation (unique error from beartype)

# The beartype annotation can be used on classes as well, which will 
# automatically apply beartype to all the methods.
@beartype
class Example:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age


# Pydantic takes a different approach to class validation.
# Note: Pydantic is kind of huge and has a lot of features.
#       There are many different ways to perform validation
#       so just keep in mind this is one of many choices.
from pydantic import BaseModel, model_validator
from typing_extensions import Self

# Pydantic's BaseModel adds attribute validation to our class.
# It expects us to define the types of the attributes in the 
# outside of the init method (and indeed use of a custom __init__
# is lightly discouraged, though possible).
class ExampleModel(BaseModel):
    name: str
    age: int

    def report(self) -> str:
        return f"{self.name} is {self.age} years old."
    
    # You can use the validate call on instance methods
    @validate_call
    def update_information(self, name: str, age: int) -> None: # NOTE SELF HERE!
        self.name = name
        self.age = age
    
    
x = ExampleModel(name="Alice", age=30)
print(x.report())
# y = ExampleModel(name="Bob", age="thirty") # ValidationError
x.update_information(name="Alice", age="thirty") # ValidationError


# Micro-exercise: Attempt to bypass the type checking
# of the above classes and functions. Write as much code 
# as you would like, and if you succeed please save the 
# example to share with the class. 