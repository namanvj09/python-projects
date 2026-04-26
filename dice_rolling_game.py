import random

while True:
    input_again = input("Roll dice (y/n): ").lower()
    if input_again == 'y':
        dice_roll = random.randint(1, 6)
        print(f"You rolled a {dice_roll}!")
        continue
    elif input_again == 'n':
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue
