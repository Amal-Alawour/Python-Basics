# Guess_Number Game
# A simple Python beginner project

import random

print("=== Guess The Number Game ===")

# Computer chooses a random number
secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = input("Guess a number between 1 and 100 (or type 'exit'): ")

    if guess.lower() == "exit":
        print("Game ended. The number was:", secret_number)
        break

    # Check if the input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("🎉 Correct!")
        print("You guessed the number in", attempts, "attempts.")
        break
