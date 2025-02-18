class A:
    def __init__(self):
        print('Class A init')
        self.a = 'A'
        super().__init__()

class B:    
    def __init__(self):
        print('Class B init')
        self.b = 'B'
        super().__init__()


class C(A, B):
    def __init__(self):
        super().__init__()
        self.c = 'C'

# Run this code once, then again after making the following changes:
# 1. Change the order of A and B in the class definition for C.
# 2. Comment out the call to super().__init__() in class A.
# 3. Comment out the call to super().__init__() in class B.

c = C()

# For more details:
# https://realpython.com/python-super/
# 