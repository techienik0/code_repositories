# Episode 8: File Handling
# Reading and writing real files - this is where it gets real!

# ===== READING FILES =====
# Reading files is how you work with real data

# The WRONG way - don't do this!
# file = open("data.txt", "r")
# content = file.read()
# file.close()  # Easy to forget!

# The RIGHT way - use 'with' statement (automatically closes file)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# File automatically closes here - even if there's an error!

# Reading line by line - perfect for large files
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character

# Read all lines into a list
with open("data.txt", "r") as file:
    lines = file.readlines()  # Returns list of all lines
    print(lines)

# ===== WRITING FILES =====
# Writing files creates actual files on your computer

# Write mode ('w') - OVERWRITES existing files!
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
# Creates new file or overwrites existing one

# Append mode ('a') - adds to end of file (safer!)
with open("output.txt", "a") as file:
    file.write("This line is added, not overwritten\n")

# Write multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
# Note: You need to include \n yourself!

# ===== WORKING WITH CSV FILES =====
# CSV files are everywhere - spreadsheets, data exports, etc.

# The WRONG way - don't parse CSV manually!
# with open("data.csv", "r") as file:
#     for line in file:
#         values = line.split(",")  # This breaks with commas in data!

# The RIGHT way - use csv module
import csv

# Reading CSV with csv.reader
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list

# Reading CSV with csv.DictReader (better - access by column name!)
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])  # Access by column name!
        print(row["age"])

# Writing CSV files
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])  # Header row
    writer.writerow(["Alex", 25, "New York"])
    writer.writerow(["Sarah", 30, "Boston"])

# Writing CSV with csv.DictWriter
with open("output.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write header row
    writer.writerow({"name": "Alex", "age": 25, "city": "New York"})
    writer.writerow({"name": "Sarah", "age": 30, "city": "Boston"})

# ===== WORKING WITH JSON FILES =====
# JSON is everywhere - APIs, config files, data storage

import json

# Reading JSON files
with open("data.json", "r") as file:
    data = json.load(file)  # Converts JSON to Python dictionary
    print(data["name"])
    print(data["age"])

# Writing JSON files
data = {
    "name": "Alex",
    "age": 25,
    "city": "New York",
    "hobbies": ["coding", "reading", "gaming"]
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)  # indent=4 makes it readable!

# ===== COMMON MISTAKES TO AVOID =====

# Mistake 1: Forgetting to close files
# file = open("data.txt", "r")
# content = file.read()
# # Forgot to close! Bad!
# Solution: Always use 'with' statement

# Mistake 2: Using wrong file path
# open("data.txt", "r")  # Looks in current directory
# open("/path/to/data.txt", "r")  # Absolute path
# Know where your file is!

# Mistake 3: Not handling file not found errors
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File doesn't exist!")

# Mistake 4: Opening file in wrong mode
# open("data.txt", "w")  # Write mode - overwrites!
# open("data.txt", "a")  # Append mode - adds to end
# Know the difference!

# Mistake 5: Not including newline characters
# file.write("Line 1")  # No newline - next write continues on same line!
# file.write("Line 2")
# Result: "Line 1Line 2" (all on one line!)
# Solution: file.write("Line 1\n")

# ===== PRACTICAL EXAMPLES =====

# Example 1: Reading a config file
try:
    with open("config.json", "r") as file:
        config = json.load(file)
        print(f"App name: {config.get('app_name', 'Unknown')}")
except FileNotFoundError:
    print("Config file not found, using defaults")

# Example 2: Logging to a file
def log_message(message):
    with open("log.txt", "a") as file:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")

log_message("Application started")
log_message("User logged in")

# Example 3: Processing CSV data
def process_sales_data(filename):
    total_sales = 0
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["amount"])
    return total_sales

# Example 4: Saving user data
def save_user_data(user_data):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    users.append(user_data)
    
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)
