# Episode 7: Lists & Dictionaries
# Storing multiple values - this changes everything!

# ===== LISTS =====
# Lists are like shopping lists, but for your code

# Creating a list - one variable, multiple values
fruits = ["apple", "banana", "orange"]
print(fruits)  # See? All three in one variable!

# Accessing items - remember, starts at 0, not 1!
print(fruits[0])  # First item (apple)
print(fruits[1])  # Second item (banana)
print(fruits[2])  # Third item (orange)

# Adding items to a list
fruits.append("grape")  # Add one item to the end
print(fruits)  # Now has grape too!

# Adding multiple items - use extend(), not append()!
fruits.extend(["mango", "pineapple"])  # Add multiple items
print(fruits)

# Common mistake: trying to append multiple items
# fruits.append("kiwi", "berry")  # This would break! append() takes ONE item

# Slicing lists - get parts of a list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])    # Items 2, 3, 4 (not including 5!)
print(numbers[:3])     # First 3 items
print(numbers[3:])     # Everything from index 3 onwards
print(numbers[-3:])    # Last 3 items (negative indexing!)

# Negative indexing - count from the end
print(numbers[-1])     # Last item
print(numbers[-2])    # Second to last

# Sorting lists
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()  # Sorts in place (changes original)
print(numbers)

# Or use sorted() to keep original unchanged
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)  # Creates new sorted list
print(f"Original: {numbers}")  # Still unsorted
print(f"Sorted: {sorted_numbers}")  # New sorted list

# Looping through lists
for fruit in fruits:
    print(f"I like {fruit}!")

# List length
print(f"There are {len(fruits)} fruits in the list")

# ===== DICTIONARIES =====
# Dictionaries use key-value pairs - like a contact list!

# Creating a dictionary
person = {
    "name": "Alex",
    "age": 25,
    "email": "alex@example.com"
}

print(person["name"])   # Get value by key
print(person["age"])

# Adding/updating values
person["city"] = "New York"  # Add new key-value
person["age"] = 26  # Update existing value
print(person)

# Safe access with get() - won't crash if key doesn't exist
phone = person.get("phone", "Not provided")  # Returns default if missing
print(phone)

# Common mistake: accessing non-existent key
# print(person["phone"])  # This would crash! Use get() instead

# Looping through dictionaries
for key, value in person.items():
    print(f"{key}: {value}")

# Just keys
for key in person.keys():
    print(key)

# Just values
for value in person.values():
    print(value)

# Checking if key exists
if "email" in person:
    print("Email found!")

# Nested dictionaries - dictionaries inside dictionaries
students = {
    "student1": {
        "name": "Alex",
        "age": 20,
        "grade": "A"
    },
    "student2": {
        "name": "Sarah",
        "age": 21,
        "grade": "B"
    }
}

print(students["student1"]["name"])  # Access nested values

# Lists of dictionaries - very common pattern!
people = [
    {"name": "Alex", "age": 25},
    {"name": "Sarah", "age": 30},
    {"name": "John", "age": 28}
]

for person in people:
    print(f"{person['name']} is {person['age']} years old")

# Dictionary length
print(f"Person has {len(person)} pieces of information")

# ===== PRACTICAL EXAMPLES =====

# Shopping list with quantities
shopping = {
    "apples": 5,
    "bananas": 3,
    "milk": 2,
    "bread": 1
}

# Add item
shopping["eggs"] = 12

# Update quantity
shopping["apples"] = 6

# Check what we need
for item, quantity in shopping.items():
    print(f"Buy {quantity} {item}")

# List of tasks with status
tasks = [
    {"task": "Learn Python", "done": True},
    {"task": "Build project", "done": False},
    {"task": "Write code", "done": True}
]

# Show incomplete tasks
for task in tasks:
    if not task["done"]:
        print(f"TODO: {task['task']}")
