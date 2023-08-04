# Group-Lab

## Algorithm for the project

1.	Create a function called get_user_choice():
-	Get the input from the user (Rock/Paper/Scissors)
-	Check if the input is valid through a while loop and iterate until a valid input is provided.
-	Convert the user’s choice into lowercase and return the result.
2.	Create a function called get_computer_choice():
-	Generate a random response by the computer (Rock/Paper/Scissors).
-	Create a list of options [Rock,paper,scissors]
-	Use the random.choice() function to randomly select an element from the list.
3.	Create a function called determine_winner():
-	Pass the user choice and the computer choice as its arguments to determine the winner between the user and the computer.
-	Compare the user’s choice with the computer’s choice to determine the winner based on the Rock, Paper Scissors rules. 
-	Return the following output based on conditions: “You win” – if the user wins, “Computer wins!” – if the computer wins, and “it is a tie!” – if it is a tie.
4.	Create another function play_game():
-	Start the game loop.
-	Use the while loop condition to keep the game going until the user decides to quit. 
-	Inside the while loop, call the get_user_choice() and the get_computer_choice() to get the user’s choice and the computer’s choice respectively.
-	Print the choices
-	Call the determine_winner() function to play the game and determine the winner and print the result of the game.
-	Ask if the user wants to continue playing the game, if not, break out of the loop and end the game.
5.	In the main () function:
-	Print a welcome message to the user and call the play_game() function to start the Rock,Paper,Scissors game.

