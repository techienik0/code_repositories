# Episode 6: Functions
# Write code once, use it everywhere - this is huge!

# Basic function - no parameters
def greet():
    print("Hello, World!")

# Call it (use it)
greet()

# Functions with parameters - make them flexible!
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")
greet("Sarah")
greet("Python")  # Same function, different results!

# Multiple parameters - separate with commas
def introduce(name, age):
    print(f"Hi, I'm {name} and I'm {age} years old.")

introduce("Alex", 25)
introduce("Sarah", 30)

# Return values - functions can give you something back
def add(a, b):
    result = a + b
    return result  # Send the result back

sum = add(5, 3)
print(sum)  # Prints: 8

# Or use it directly
print(add(5, 3))  # Also prints: 8

# Real example - calculate total with tax
def calculate_total(price, tax_rate):
    tax = price * tax_rate
    total = price + tax
    return total

final_price = calculate_total(100, 0.08)
print(f"Total: ${final_price}")

# Function scope - variables inside functions are separate
# This confused me at first, but it's actually useful!

def my_function():
    x = 10  # This x only exists inside the function
    print(x)

x = 5  # This x is outside the function
my_function()  # Prints: 10 (the one inside)
print(x)  # Prints: 5 (the one outside)

# Functions can read variables from outside though
y = 20

def show_y():
    print(y)  # Can read y from outside

show_y()  # Prints: 20
