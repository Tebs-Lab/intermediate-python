def counter_factory():
    a = 0

    def counter(): 
        nonlocal a
        a += 1
        return a
    
    return counter

x = counter_factory()
print(type(x)) # <class> 'function'
print(x()) # 1
print(x()) # 2
print(x()) # 3

first = counter_factory() 
second = counter_factory()

print(first()) # 1
print(first()) # 2
print(first()) # 3

print(second()) # 1
print(second()) # 2
print(second()) # 3