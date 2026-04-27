import random
emojis = {'r': '✊', 'p': '✋', 's': '✌️'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, Scissors (r/p/s): ").lower()
        if(user_choice in choices):
            return user_choice
        else:
            print("Invalid input. Please enter 'r', 'p', or 's'.")
            continue

def display_choices(user_choice, system_choice):
    print(f'You Chose: {user_choice}{emojis[user_choice]}')
    print(f"Computer chose: {system_choice}{emojis[system_choice]}")

def determine_winner(user_choice, system_choice):
    if user_choice == system_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and system_choice == 's') or (user_choice == 'p' and system_choice == 'r') or (user_choice == 's' and system_choice == 'p'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    while True:
        user_choice = get_user_choice()
        system_choice = random.choice(choices)

        display_choices(user_choice, system_choice)

        result = determine_winner(user_choice, system_choice)
        print(result)

        continue_game = input("Continue or not? y/n:: ").lower()
        if continue_game != 'y':
            break

play_game()