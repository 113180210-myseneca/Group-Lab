#!/usr/bin/env python3
import random

def get_user_choice():
    while True:
        # Request the user's selection, then change it to lowercase.
        user_choice = input("Enter your choice (Rock/Paper/Scissors): ").lower()

        # Verify that the user's input is one of the acceptable alternatives by validating it.
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        print("Invalid input. Please choose again from the following choices: Rock/Paper/Scissors.")

def get_computer_choice():
    # Create a random selection for the computer to choose from the available possibilities.
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    # In accordance with the game's regulations, compare the user's selection with the computer's selection to determine the winner.
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        return "You win!" if computer_choice == 'scissors' else "Computer wins!"
    elif user_choice == 'paper':
        return "You win!" if computer_choice == 'rock' else "Computer wins!"
    elif user_choice == 'scissors':
        return "You win!" if computer_choice == 'paper' else "Computer wins!"

def play_game():
    while True:
        # Obtain the option made by the user and the computer.
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Show the decisions that both the user and the machine have made.
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        # Choose a winner and present the outcome.
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Inquire if the player wants to play once more.
        play_again = input("One more round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
