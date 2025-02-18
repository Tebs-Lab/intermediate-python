# Object Oriented Programming Exercise: 4 Function Calculator

This exercise is designed to help you practice:

* Writing classes with properties (state) and methods (behavior).
* Thinking about and designing systems with many possible states.
* Gracefully handling expected errors.
* Writing larger programs with more user input.

# The Exercise:

Make a 4 function calculator interface. Your program should:

* Create a class called Calculator, which must:
    * Have a way to store the current value of the computation.
    * Have separate methods for performing addition, subtraction, multiplication, and division
    * Have a display function which uses the terminal to:
        * Display the current value of the computation.
        * Accepts input from the user.
        * Displays any relevant error messages.
        * Allows the user to exit the display, but loops until then.
    * Take inputs like an old-school calculator: one at a time.
        * Enter a number while no operation is pending: that becomes the value.
        * Enter an operation: that becomes the pending operation
        * Enter a number while an operation is pending: perform the operation with the new number and the currently displayed value. 
        * Have a method that clears the current value and pending operation.

## Some tips:

* Design a little first, but be flexible to change as you learn more.
    * Decide what properties and methods you think will be needed. 


* Build, test, repeat, on short loops.
    * Make a method, prove it works, then implement the next method.

* The display function will most likely be the most difficult part.

* The following code snippet will clear the terminal output. My solution uses this repeatedly to make the interface easier to read and follow.

```
import os

os.system('clear') # *nix
os.system('cls') # windowsa
```