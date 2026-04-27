import random

random_number = random.randint(1, 100)
guess_number = 0

while random_number != guess_number:
    try:
        guess_number = int(input("Guess the number (1-100) "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if guess_number < random_number:
        print("Too low! Try again..")
    elif guess_number > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
