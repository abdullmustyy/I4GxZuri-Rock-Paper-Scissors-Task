import random

options = {
    'R': 'Rock 🤜🏻',
    'P': 'Paper 🖐🏻',
    'S': 'Scissors ✌',
}

options_list = ['R', 'P', 'S']


def check_game():
    if player_choice == computer_choice.lower():
        print('It is a tie.')
    elif player_choice == 'r' and computer_choice.lower() == 'p':
        print("Paper beats Rock. Computer wins.")
    elif player_choice == 'r' and computer_choice.lower() == 's':
        print("Rock beat Scissors. Player wins.")
    elif player_choice == 'p' and computer_choice.lower() == 'r':
        print("Paper beat Rock. Player wins.")
    elif player_choice == 'p' and computer_choice.lower() == 's':
        print("Scissors beats Paper. Computer wins.")
    elif player_choice == 's' and computer_choice.lower() == 'r':
        print("Rock beats Scissors. Computer wins.")
    elif player_choice == 's' and computer_choice.lower() == 'p':
        print("Scissors beat Paper. Player wins.")


print("ROCK 🤜🏻 - PARER 🖐🏻 - SCISSORS ✌\n    Welcome to the game of Rock, Paper, Scissors.\n    Input 'r' for Rock,"
      " 'p' for Paper and 's' for Scissors.\nEnjoy...\n")

game_on = True
while game_on:

    computer_choice = random.choice(options_list)
    prompt = input("Input 'y' to start the game and 'n' to stop it: ").lower()
    print("")

    if prompt == "y":
        player_choice = input("Rock(r), Paper(p) or Scissors(s)? ").lower()
        if player_choice == "r" or player_choice == "p" or player_choice == "s":
            print(f"\nPlayer ({options[player_choice.upper()]}) : CPU ({options[computer_choice]})\n")
            check_game()
        else:
            print("\nThat is not part of the options, please pick the correct option.")
    elif prompt == "n":
        game_on = False
    else:
        print('Invalid input, Please pass in the correct the input. \n')
