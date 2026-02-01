# Episode 3: Mini Project - User Info Collector
# This is my first real program!

print("=== User Information Collector ===")
print()

# Ask the user for their info
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))  # Convert to number
email = input("Enter your email: ")
city = input("Enter your city: ")

# Show them what we collected
print()
print("=== Your Information ===")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Location: {city}")
print()
print(f"Welcome, {first_name}! You're {age} years old.")

# Try running this and entering your info!
