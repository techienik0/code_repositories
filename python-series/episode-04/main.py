# Episode 4: If/Else Logic
# Making my code make decisions!

# Basic if statement

age = 20

if age >= 18:
    print("You can vote!")

# Try changing age to 15 - nothing will print
age = 15

if age >= 18:
    print("You can vote!")  # This won't run because age is 15

# Adding else and elif for more options

age = 15

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")

# Multiple conditions with elif
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Comparison operators - how to compare things

# Greater than
print(5 > 3)   # True

# Less than
print(3 < 5)   # True

# Greater than or equal
print(5 >= 5)  # True

# Less than or equal
print(3 <= 5)  # True

# Equal to (double equals!)
print(5 == 5)  # True (note: == not =)

# Not equal
print(5 != 3)  # True

# Logical operators - combining conditions

age = 25
has_license = True

# AND - both must be true
if age >= 18 and has_license:
    print("You can drive!")

# OR - at least one must be true
if age < 18 or age > 65:
    print("Special pricing applies")

# NOT - reverses the condition
if not has_license:
    print("You need a license")

# Nested conditions - if inside if
# Can get messy, but sometimes you need it

age = 25
has_license = True
has_car = True

if age >= 18:
    if has_license:
        if has_car:
            print("You can drive to work!")
        else:
            print("You need a car")
    else:
        print("You need a license")
else:
    print("You're too young")

# Simplified version with 'and'
if age >= 18 and has_license and has_car:
    print("You can drive to work!")
elif age >= 18 and has_license:
    print("You need a car")
elif age >= 18:
    print("You need a license")
else:
    print("You're too young")
