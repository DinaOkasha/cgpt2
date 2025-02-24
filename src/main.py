def add_numbers(a, b):
    return a - b  # Bug

print(add_numbers(5, "three"))  # TypeError: unsupported operand type(s)
