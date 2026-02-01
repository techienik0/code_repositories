# Episode 6: Mini Project - Calculator with Functions
# Using functions to organize code - much cleaner!

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"  # Don't crash!
    return a / b

def calculator():
    print("=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1-4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == "1":
        result = add(num1, num2)
        print(f"Result: {result}")
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"Result: {result}")
    elif choice == "3":
        result = multiply(num1, num2)
        print(f"Result: {result}")
    elif choice == "4":
        result = divide(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid choice!")

# Run the calculator
calculator()
