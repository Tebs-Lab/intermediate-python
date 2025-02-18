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

c = C()