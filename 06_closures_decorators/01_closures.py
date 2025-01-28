# Closures are a general concept in computer programming, especially
# in functional programming paradigms. A closure is created when a function
# is defined within another function (the enclosing function). 

# Here's an example of a closure in Python:
def counter_factory():
    a = 0

    def counter(): 
        nonlocal a
        a += 1
        return a
    
    return counter

# This is an example of "first class functions" -- a feature of programming
# languages that treat functions like other kinds of data, that can be passed
# to functions, stored to variables, and returned from functions. 

# x is an instance of the function called "counter" defined on line 10.
x = counter_factory()
print(type(x)) # <class> 'function'
print(x()) # 1
print(x()) # 2
print(x()) # 3

# However, there can be multiple, separate instances, of that function "counter"
# and each instance will have it's own state. Specifically, a separate copy of 
# the variable "a" which will be tracked independently for each instance. 
first = counter_factory() 
second = counter_factory()

print(first()) # 1
print(first()) # 2
print(first()) # 3

print(second()) # 1
print(second()) # 2
print(second()) # 3

# In many ways closures are the functional programming equivalent of classes.
# the variables that are "closed over" (a in this example) are like instance
# variables, and the functions themselves are like methods. They are also "safer"
# in some ways, for example the variable "a" is not accessible from outside the
# returned function instance, making it truly private data in a way that is not 
# true for instance variables in classes.

# Micro-exercise: Create a closure a takes starting point and an "increment by"
# value as arguments, and returns a function that iteratively returns the sequence
# starting at the starting point, and incrementing by the increment by value each time.