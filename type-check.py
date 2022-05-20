def only_ints(a, b):
    if type(a) == int and type(b) == int:
        return True
    return False

print(only_ints(25, 5))
print(only_ints('sun', 5))
print(only_ints("x", 22))
print(only_ints(33,-5))
print(only_ints(-5, "plus"))