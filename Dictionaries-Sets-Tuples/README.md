🐍 Day 5: Python Functions
📚 Topics Covered
✅ 1. Defining Functions
Functions are reusable blocks of code.
def greet():
    print("Hello, World!")


✅ 2. Parameters and Arguments
Functions can take inputs (parameters) and work with them.

def greet(name):
    print(f"Hello, {name}!")

greet("Ismail")  # Output: Hello, Ismail!


✅ 3. Return Statement
Functions can return values using return.
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5


✅ 4. Scope
Local Scope: Variables inside a function.

Global Scope: Variables outside all functions.
x = 10  # global

def example():
    x = 5  # local
    print("Inside:", x)

example()
print("Outside:", x)