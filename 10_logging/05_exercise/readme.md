# Practice With Logging

In this exercise you'll practice using the logging package, as well as refresh your memory about making  decorators.

## Setup

This folder contains a few files that you'll be modifying.

* `main.py` a simple script that imports and executes some functions and other code. 
* `functions.py` some functions from a previous exercise.

## The Tasks

Additionally you'll be required to make at least one new file (the solution uses 2 new files) to build an enable the following:

1. Create a decorator that can:
    * Use `logging` to log the arguments and return value from the decorated function.
    * Accept as input a `logger` instance and a `log_level` which will be used for the logging in the decorator.
2. A log configuration file that specifies:
    * A file where you will write the logs.
    * An explicit format that at minimum includes the timestamp of each log line.
    * A log level to be used (we suggest debug, but it's really up to you)
    * Two logger configurations -- one for the root logger and another for the `functions.py` file
        * Because our decorator accepts a logger as input, we need to define that logger in the file where we apply the decorators!

Once you've built such a decorator and logging configuration, test your decorator by adding it to the two functions in `functions.py` and running `main.py`. Check that your logs match your expectations.