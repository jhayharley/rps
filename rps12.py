# from tkinter import *
# import tkinter
#for clearing the unneccesary fields
import os 
#for security purposes
from getpass import getpass

print("               RULES: The  players must input their own choice and patiently wait for their turn!" )
print("                   DESCRIPTION: Paper Covers Rock, Rock Smashes Scissors, Scissors Cuts Paper\n")
print("                                 ***Welcome to Rock, Paper Scissors Game***\n")


#for the user to input their choice
def getInput():
    choice = getpass("What are you picking - [rock, paper, or scissors?]\n")
    if validate(choice) == True:
        pass
    else:
        print("Invalid choice, please try again\n")
        choice = getInput()
    return choice

#Validate user input is as expected
def validate(choice):
    if choice == "rock" or choice == "paper" or choice == "scissors":
        return True
    else:
        return False

#Put together gameplay flow
def gameplay():
#Store choices of each user
    print(player1 + "")
    p1 = getInput()
    print(player2 + "")
    p2 = getInput()
    os.system('clear')
#displays the selected choice
    print(player1.upper()+' selected '+p1.upper())
    print(player2.upper()+' selected '+p2.upper())

    points = score(p1,p2)
    return points

#Takes each player's choice as an argument
#Determines the winner and awards a point
#per round
def score(p1,p2):

#if p1 is equal to p2 generate TIE
    if p1 == p2:
        print("Tie! Try Next Round!\n")
        points = (0,0)

#This code will generate p1 wins because paper covers rock
    elif p1 == "paper" and p2 == "rock":
        print(player1.upper() + "\nWin This Round!\n")
        points = (1,0)

#This code will generate p2 wins because rock smashes scissors
    elif p1 == "scissors" and p2 == "rock":
        print(player2.upper() + " Win This Round!\n")
        points = (0,1)


#This code will generate p2 wins because paper covers rock
    elif p1 == "rock" and p2 == "paper":
        print(player2 + " Win This Round!\n")
        points = (0,1)


#This code will generate p1 wins because scissors cuts paper
    elif p1 == "scissors" and p2 == "paper":
        print(player1 + " Win This Round!\n")
        points = (1,0)


#This code will generate p1 wins because rock smashes scissors
    elif p1 == "rock" and p2 == "scissors":
        print(player1 + " Win This Round!\n")
        points = (1,0)


#This code will generate p2 wins because scissors cuts paper
    elif p1 == "paper" and p2 == "scissors":
        print(player2 + " Win This Round!\n")
        points = (0,1)

    return points


#Before executing the code, it will define a few special variables. For example, if the python interpreter is running 
#that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__".
#If this file is being imported from another module, __name__ will be set to the module's name.
if __name__ == "__main__":

#determine how many rounds to play
    while True:
        try:
            num_rounds = int(raw_input("How many points does it takes to win? \n"))
            break
        except ValueError:
            print("input a integer")

#player's identity
    player1 = raw_input("Enter your name player 1: ")
    player2 = raw_input("Enter your name player 2: ")

#this part is responsible for summing-up the scores and declare the overall winner.
    gamescore = [0,0]
    while gamescore[0] < num_rounds and gamescore[1] < num_rounds:
        points = gameplay()
        gamescore[0] += points[0]
        gamescore[1] += points[1]
        print(player1.upper() + " has " + str(gamescore[0]) + " points")
        print(player2.upper() + " has " + str(gamescore[1]) + " points\n")
        if gamescore[0] == num_rounds:
            print(player1 + " has Won\nGAME OVER!")
        elif gamescore[1] == num_rounds:
            print(player2 + " has Won\nGAME OVER!")

#after the declaration of winner in every round it will ask the players if they want to play another round.
    # if (raw_input('Do you want to play another round, yes or no?\n')).lower().startswith('y'):
    # continue
    # print('GAME OVER')
    # break