import os # For clearing the output from the terminal

class Calculator:
    VALID_OPERATORS = ('+', '-', '/', '*')
    EXIT_DISPLAY_VALUE = 'e'
    CLEAR_VALUE = 'c'

    def __init__(self):
        self.additional_display = None
        self.pending_operator = None
        self.current_val = 0

    def run_display(self):
        # If there is a pending operator we'll do that calculation with whatever is input.
        # Otherwise we'll set the current value to the input
        self.pending_operator = None
        while True:
            os.system('clear') # Clears the text output so we always have just the most recent line
            # os.system('cls') # For Windows Users!!
            if self.additional_display: print(self.additional_display)
            print(f'{self.current_val} {self.pending_operator or ""}')
            user_in = input(": ")

            if user_in == Calculator.EXIT_DISPLAY_VALUE:
                print("Exiting calculator display")
                break

            if user_in == Calculator.CLEAR_VALUE:
                self.clear()
                continue

            # If it's an operator just overwrite whatever operator is currently there and start over
            if user_in in Calculator.VALID_OPERATORS:
                self.pending_operator = user_in
                self.additional_display = None
                continue
            # If it's not an operator, make sure it's a number and cast it as such.
            else:
                try:
                    user_in = float(user_in)
                except Exception as e:
                    self.additional_display = f"\x1b[31mError, invalid input {user_in}. Enter a number of one of +, -, /, *, c, e\x1b[0m"
                    continue
            
            # Now the input must be a number.
            if self.pending_operator is None:
                self.set_current_val(user_in)
            elif self.pending_operator == '+':
                self.add(user_in)
            elif self.pending_operator == '-':
                self.subtract(user_in)
            elif self.pending_operator == '/':
                self.divide(user_in)
            elif self.pending_operator == '*':
                self.multiply(user_in)
            else:
                # This shouldn't ever happen
                raise ValueError(f"Pending operator is an illegal value {self.pending_operator}")

            self.pending_operator = None
            self.additional_display = None


    def clear(self):
        self.current_val = 0
        self.pending_operator = None
        self.additional_display = None

    def set_current_val(self, num):
        self.current_val = num

    def add(self, num):
        self.current_val += num

    def subtract(self, num):
        self.current_val -= num

    def divide(self, num):
        self.current_val /= num

    def multiply(self, num):
        self.current_val *= num


def main():
    calc = Calculator()
    calc.run_display()

if __name__ == '__main__':
    main()