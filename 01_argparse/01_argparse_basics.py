#!python
# The above is called a "shebang" or "hashbang" and it lets your terminal know what 
# program to use if this file is called as an executable. In this case "python"

# Argparse is a library for building CLI tools.
# It's an excellent and simple way to enable more complex scripts
# Docs: https://docs.python.org/3/library/argparse.html
import argparse

# When you make a parser, you should give it some helpful details that can
# be displayed to the user automatically when they call your program with
# -h or --help
# Details: https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
parser = argparse.ArgumentParser(
    prog='ProgramName',
    description='What the program does',
    epilog='Text at the bottom of help'
)

# add_argument allows us to add options to our program.
# There are LOTS of options and parameters, making argparse very flexible.
# Details: https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument

# All positional arguments are strings that your user will type into the CLI.
# Positional arguments that start with a "-" are optional, ones that do not are required.

# This (uninformative) line adds a required positional argument called 'pos_one'
# using default options for everything else. 
parser.add_argument("pos_one")

# You may use a value that is not a valid python variable or identifier name.
# But it will make your life harder for little gain...
parser.add_argument("2pos-two")


# Here's a more typical example that includes some of the common options
# Remember: this one is optional because it's positional args start with a "-"
# Note: if multiple names are specified argparse uses the first one that starts with '--' 
# as the "normalized" name, or if none start with -- it uses the first name.
parser.add_argument(
    "-n", "--num", 
    help="This must be an integer between 1 and 10. Defaults to 1.", 
    type=int, 
    default=1,
    choices=range(1,11)
)

# Note, specifying a range for floating points with "choices" possible but kind of a hassle.
# You can test the value after it's been parsed and raise an error or you can see this SO answer:
# https://stackoverflow.com/questions/12116685/how-can-i-require-my-python-scripts-argument-to-be-a-float-in-a-range-using-arg
parser.add_argument(
    "-f", 
    help="This should be a float", 
    type=float, 
    default=1.0,
)

args = parser.parse_args()
print(args.pos_one, type(args.pos_one))

# This throws a Syntax error before the program even runs.
# print(args.2pos-two)
# this works, but is it really worth it?
print(args.__dict__['2pos-two'], type(args.__dict__['2pos-two'])) 

# Because we used a '--' form, that's the name for the arg we called -n --num
print(args.num, type(args.num))

# Because we did not use a '--' form, the arg we called f is just called f
print(args.f, type(args.f))

# Micro-Exercise: Add any one argument to this example then print its value and type.
# Call the program from your terminal to ensure it still works.