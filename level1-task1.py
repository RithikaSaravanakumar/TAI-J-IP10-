import random

def number_guessing_game():
    """Number guessing game."""

    print("Welcome to the Number Guessing Game!")

    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    if lower_bound >= upper_bound:
        print("Lower bound must be less than upper bound.")
        return

    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return

        if guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Sorry, you ran out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
