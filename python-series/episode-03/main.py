# Episode 3: Variables & Data Types
# Playing around with variables

# Variables are basically labeled boxes
# Put something in, give it a name, use it later
name = "Alex"
print(name)

# Cool thing - you can change what's inside
name = "Sarah"
print(name)  # Now it's Sarah!

# Different types of data Python can handle

# Text (strings) - use quotes
name = "Alex"
message = 'Hello, World!'  # Single or double quotes work
email = "alex@example.com"

# Whole numbers (integers) - no quotes!
age = 25
count = 100
temperature = -10  # Negative numbers work too

# Decimal numbers (floats)
price = 19.99
pi = 3.14159
height = 5.9

# True/False (booleans) - capital T and F!
is_student = True
has_license = False
is_raining = True

# Why types matter - this is important!

age = 25
age_text = "25"  # This looks like a number but it's actually text

print(age + 5)        # Works! 25 + 5 = 30
# print(age_text + 5)  # This will crash! Can't add number to text
# Uncomment the line above to see the error

# Converting between types
# Sometimes you need to change text to numbers or vice versa

age = "25"  # This is text (string)
age_number = int(age)  # Convert to actual number
print(age_number + 5)  # Now we can do math! 30

# Going the other way - number to text
price = 19.99
price_text = str(price)  # Convert number to text
print("The price is $" + price_text)

# Pro tip: input() always gives you text, so convert it!
user_age = input("Enter your age: ")  # This is text even if you type a number
age = int(user_age)  # Convert it so we can do math
print(f"You'll be {age + 10} in 10 years")

# F-strings - the modern way to combine text and variables
# This is SO much better than the old way

name = "Alex"
age = 25

# Old way - super messy, don't do this
message = "My name is " + name + " and I'm " + str(age) + " years old"
print(message)

# New way with f-strings - clean and easy!
message = f"My name is {name} and I'm {age} years old"
print(message)

# Just put 'f' before the quotes and use {variable} inside
# Python automatically converts everything - magic! ✨
