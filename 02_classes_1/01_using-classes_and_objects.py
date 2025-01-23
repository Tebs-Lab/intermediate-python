# It turns out we've been using classes this whole time!
# Classes are a template for a data type.
# Each instance of a class is called an object.
# Concrete example, lists are a datatype, their class is the "list" class and when we make one
# we're making an object of the "list" type, that objects "class" is the "list"
x = []
print(x.__class__, type(x), x.__class__ == list, "\n")

# Classes allow us to create datatypes that have both values and functions attached.
# functions that belong to a class are often called "methods" to distinguish them from 
# standalone functions. For example the "append" function is a "method" of the list class.
x.append("one")
x.append(2)
x.append(3.0)

# as you can see, methods can change the values inside a particular object!
print(x, "\n")

# The dir function lets us see what attributes an object has:
# (dir is designed to be used for humans to understand objects.)
print(dir(x), "\n")

# the vars function is similar, but it is designed to be used more programmatically
# (it also has some peculiarities, which is why we have to call it this strange 
# looking way for lists). Vars returns a dictionary mapping propertyName->propertyValue
for prop_name, prop_value in vars(x.__class__).items():
    print(prop_name, prop_value, type(prop_value))


# Micro-Exercise: "everything is an object" Choose any other built-in 
# datatype and examine the output of using dir and vars on it. 

