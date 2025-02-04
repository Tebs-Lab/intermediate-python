# Python has a robust built in logging package.
import logging

# Typically, you want to configure your logger to, at minimum, set the 
# "log level" that you want to see. debug is the most verbose level
# More on this in a moment...

# Additionally, it's common to set a format for the log messages
# We can also customize the format of the log message, and include several built in variables
# There are a LOT of built in variables that can be logged:
# https://docs.python.org/3/library/logging.html#logrecord-attributes
logging.basicConfig(level=logging.DEBUG, 
                    format="[{asctime}]{levelname}:{name}:{message}", 
                    style="{", 
                    datefmt="%Y-%m-%d %H:%M:%S"
)

# At it's most basic, you can use the "root logger" to log
# any kind of message you want. By default, this goes to 
# standard out / standard error (which will print to the terminal)
logging.info("This is some information")

# There are 5 log levels, and a special level called "notset". 
# We'll talk about notset later. The 5 levels are:
logging.debug("This is a debug message, generally we only use these during development")
logging.info("This is purely informational, nothing bad has happened, but we want to make a record of something occurring")
logging.warning("This is a warning, something bad might happen, but it's not critical")
logging.error("This is an error, something bad has happened and the software has failed to perform some function")
logging.critical("This is a critical error, something very bad has happened and the software has most likely crashed completely.")

# Micro-Exercise: Change the log level to warning and run the script up to this point
# again... What is the difference in the console output?

# Micro-Exercise 2: Go to the docs linked above and add a few more variables to the log 
# messages format section. Choose variables that are interesting to you.
