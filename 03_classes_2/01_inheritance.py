# Inheritance is an important OOP concept. In short
# it allows one class (the child class) to automatically
# have all the properties of another class (the parent class)

# A class that does not explicitly inherit from anything 
# will automatically inherit the properties of Python's 
# base class. This Person class is such an example:
class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


p = Person('Tyler')
p.print_name()


# When a class inherits from another class, we specify it using parentheses.
# In this class, Student inherits from Person. 
class Student(Person):
    def __init__(self, name, grade):
        # The parent class has it's own __init__ function which must be 
        # invoked. Unfortunately, 'self' in this context is a Student, so self.__init__ 
        # would refer to THIS __init__ function. Python's built in super() function
        # allows us to explicitly access such "shadowed" or "overloaded" functions.
        super().__init__(name)
        self.grade = grade

        # FYI: super() is complex. Docs: https://docs.python.org/3/library/functions.html#super

    def print_grade(self):
        print(self.grade)

    # Instances (objects) of child types have access to all the properties
    # and methods created in the parent class
    def print_report(self):
        print(f'{self.name} currently has the grade: {self.grade}')

s = Student('Molly', 'A+')

# Note that we can invoke parent methods directly:
s.print_name()

# We can also invoke child methods:
s.print_grade()
s.print_report()

# But the relationship is one way, Person instances do NOT have a
# print_grade method:
# p.print_grade() # Error!

# All children are instances of the parent class and the child class:
print(isinstance(s, Person))
print(isinstance(s, Student))

# Micro-exercise: read the following code and predict the output.
class SeventhGrader(Student):
    def __init__(self, name, grade):
        super().__init__(name, grade)

    def print_report(self):
        print(f'{self.name} is a seventh grader who doesn\'t care about their grade of: {self.grade}')

sven = SeventhGrader('Sven', 'B-')
sven.print_report()

# Micro-Exercise Part 2: Add a method to SeventhGrader that allows us to invoke 
# the print_report from Student using the following line of code:
sven.print_student_report() # This should print "Sven currently has a B-" when you're done