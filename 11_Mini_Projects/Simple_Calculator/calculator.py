def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(add(5, 3))
print(subtract(5, 3))
print(multiply(5, 3))
print(divide(5, 3))
