import random

# Exercise: Guess the secret number
secret_number = random.randint(1, 10)
guess = int(input("Guess the secret number between 1 and 10: "))
# The loop continues until the user guesses the secret number.
while secret_number != guess:
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess the secret number between 1 and 10: "))
print("\n Congratulations! You guessed the secret number.", "\n ------------------------- \n")