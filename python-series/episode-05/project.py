# Episode 5: Mini Project - Number Guessing Game
# My first game! Pretty cool, right?

import random

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100.")
print("You have 7 guesses!")
print()

secret_number = random.randint(1, 100)  # Random number between 1-100
guesses = 0
max_guesses = 7

while guesses < max_guesses:
    guess = int(input(f"Guess {guesses + 1}: "))
    guesses += 1
    
    if guess == secret_number:
        print(f"🎉 You won! The number was {secret_number}.")
        print(f"You guessed it in {guesses} tries!")
        break  # Exit the loop
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    print(f"Guesses remaining: {max_guesses - guesses}")
    print()

# If they ran out of guesses
if guesses == max_guesses and guess != secret_number:
    print(f"Game over! The number was {secret_number}.")

print()
print("Thanks for playing!")
