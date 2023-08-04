# Group-Lab

### Table of Contents
1. [Part A - Algorithm for the project](#part-a)
2. [Part B - Instruction for the game of Rock, Paper, Scissors](#part-b)
3. [Part C - Role of each member](#part-c)
4. [Part D - Links for the files](#part-d)


## Part A

### Algorithm for the project

``` 
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
```

## Part B

### Instruction for the game of Rock, Paper, Scissors
As in how this works is the user inputs an option selected from rock, paper or scissors and on the other hand the computer randomly procees to select an option from the above mentioned list. As the both parties proceed with the inputs the script compares them. There is a total of 9 outcomes when comapred the inputs.

```
1) If the user chooses "Rock" and the computer chooses "Rock", it will be a tie. 
2) If the user chooses "Rock" and the computer chooses "Paper", the computer will win.
3) If the user chooses "Rock" and the computer chooses "Scissors", the user will win.
4) If the user chooses "Paper" and the computer chooses "Paper" it will be a tie.
5) If the user chooses "Paper" and the computer chooses "Scissors", the computer will win.
6) If the user chooses "Paper" and the computer chooses "Rock", the user will win.
7) If the user chooses "Scissors" and the computer chooses "Scissors", it will be a tie.
8) If the user chooses "Scissors" and the computer chooses "Rock", the computer will win.
9) If the user chooses "Scissors" and the computer chooses "Paper", the user will win.
```

The user will be only able to enter one option each turn, same as the auto generated option from the computer. After selecting the option, the user will be given the option between moving on or going back to selecting a different option. This is where the difference comes in as in a real time game of rock papper scissor you can't go back on the selected move. Then the program will comapre the inputs and provide the user with the final result and leaving the option for him or her to go back for another round of rock paper scissor.

## Part C

### Member's Role:

- Parkhi Sharma

Student ID: 113180210

Email: psharma178@myseneca.ca

Role: 
Worked on Iteration1 and Testing1

Created a new issue for resolving

Made the README.md file

Deployed the project

- Khushi Rathod 

Student ID: 121499214 

Email: kkrathod@myseneca.ca

Role:

Acknowleged the issue

Worked on Iteration2 and Testing2

- Arjun Vadakkekarayil Sojan

Student ID: 144828217

Email ID: avadakkekarayil-soja@myseneca.ca

Role:

Created the algorithm for the project

- Kinod Lakdinu

Student ID: 130349210

Email: klmelewa-thanthrige@myseneca.ca

Role:

Created the flowchart for the project

Created the intructions for how the the game of rock/paper/scissors works.

## Part D

### Links for the files 

- Flowchart: https://github.com/113180210-myseneca/Group-Lab/blob/main/OPS445.drawio.pdf  

- Iteration 1: https://github.com/113180210-myseneca/Group-Lab/blob/Iteration1/Iteration1.py

- Iteration 2: https://github.com/113180210-myseneca/Group-Lab/blob/main/Iteration2.py
