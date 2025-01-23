# Making custom classes is easy in Python.
# You may not do this very often (especially when you're just writing scripts)
# But seeing class implementations makes understanding 3rd party libraries much easier.

# Lets start very simple to see the components of a class
class User:

    # Every class has a "constructor" function, which has this very special name
    # The constructor is called when we create a new object of this class
    # methods ALWAYS take a first parameter called "self" in Python which will
    # refer to a particular object of the class's type, in the constructor that's
    # the object that will be created.
    def __init__(self, email, name, age):
        self.email = email
        self.name = name
        self.age = age

    # Classes often have methods, which we define like normal functions
    def generate_report(self):
        report = f"{self.name} is {self.age} years old and their email address is {self.email}"
        return report
    
    def birthday(self):
        print(f'{self.name} got older!')
        self.age += 1


# To make a new object of any classes type, you use the name of the class
user_tyler = User('teb@tebs-lab.com', 'Tyler Bettilyon', 58)
print(user_tyler, type(user_tyler), type(user_tyler) == User)
print(dir(user_tyler))
print()
print(vars(user_tyler))

# We can call methods using the dot notation.
print(user_tyler.generate_report()) 

# We can create as many instances of this type as we want.
user_sara = User('sara@fakemail.com', 'Sara Middelton', 32)

# Objects of the same class have the same type
print(type(user_tyler) == type(user_sara))

# But they won't have the same properties!
print(user_sara.name, user_tyler.name)

# Properties can be accessed and changed using dot notation
# This is often a bad idea, but you should be aware it can be done.
user_tyler.name = 'Frank Fredrickson'
print(user_tyler.name)
print()

# The preferred way to change an object's value is by using a method
print(user_sara.age)
user_sara.birthday()
print(user_sara.age)

# Micro-exercise: add a method to the User class that allows us to change the user's name
# Then execute that method on an User objects and prove to yourself that it works.