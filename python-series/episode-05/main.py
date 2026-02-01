# Episode 5: Loops
# Finally! No more copy-pasting code

# For loops - the easiest way to repeat code
# Print "Hello" 5 times without typing it 5 times!
for i in range(5):
    print("Hello!")

# Loop through numbers
for i in range(5):
    print(i)  # This prints 0, 1, 2, 3, 4

# range() function - generates numbers for loops
# Super useful, you'll use this all the time

# range(5) gives you 0, 1, 2, 3, 4
for i in range(5):
    print(i)

# range(1, 6) gives you 1, 2, 3, 4, 5 (starts at 1, stops before 6)
for i in range(1, 6):
    print(i)

# range(0, 10, 2) - start at 0, go to 10, step by 2
for i in range(0, 10, 2):
    print(i)  # Prints 0, 2, 4, 6, 8

# While loops - keep going until condition is false
# Be careful - can create infinite loops if you're not careful!

count = 0
while count < 5:
    print(count)
    count += 1  # Don't forget this! Otherwise infinite loop!

# break and continue - control your loops

# break - exit the loop completely
for i in range(10):
    if i == 5:
        break  # Stop the loop here
    print(i)  # Only prints 0, 1, 2, 3, 4

# continue - skip this iteration, keep going
for i in range(10):
    if i == 5:
        continue  # Skip 5, but keep looping
    print(i)  # Prints 0, 1, 2, 3, 4, 6, 7, 8, 9 (no 5!)

# Nested loops - loops inside loops
# Can get slow with big numbers, but useful for some things

# Simple multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line after each row
