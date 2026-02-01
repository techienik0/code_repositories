# Episode 4: Mini Project - Grade Calculator
# This actually calculates real grades!

print("=== Grade Calculator ===")
print()

# Get the scores from user
math_score = float(input("Enter math score (0-100): "))
science_score = float(input("Enter science score (0-100): "))
english_score = float(input("Enter english score (0-100): "))

# Calculate the average
average = (math_score + science_score + english_score) / 3

# Determine grade
if average >= 90:
    grade = "A"
    message = "Excellent work!"
elif average >= 80:
    grade = "B"
    message = "Good job!"
elif average >= 70:
    grade = "C"
    message = "Not bad, but you can do better."
elif average >= 60:
    grade = "D"
    message = "You need to study more."
else:
    grade = "F"
    message = "You need serious help."

# Display results
print()
print(f"Average Score: {average:.1f}")
print(f"Grade: {grade}")
print(f"Message: {message}")

# Bonus: Subject feedback
print()
print("=== Subject Feedback ===")
if math_score >= 90:
    print("Math: Outstanding!")
elif math_score >= 70:
    print("Math: Good")
else:
    print("Math: Needs improvement")

if science_score >= 90:
    print("Science: Outstanding!")
elif science_score >= 70:
    print("Science: Good")
else:
    print("Science: Needs improvement")

if english_score >= 90:
    print("English: Outstanding!")
elif english_score >= 70:
    print("English: Good")
else:
    print("English: Needs improvement")
