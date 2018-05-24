#for clearing the unneccesary fields
import os 
#for security purposes
from getpass import getpass

#constants

print("               RULES: The  players must input their own choice and patiently wait for their turn!" )
print("                   DESCRIPTION: Paper Covers Rock, Rock Smashes Scissors, Scissors Cuts Paper\n")
print("                                 ***Welcome to Rock, Paper Scissors Game***\n")


#for the user to input their choice
class Game(object):

    def getInput(self):
        choice = getpass("What are you picking - [(1)ROCK, (2)SCISSORS, (3)PAPER?]\n")
        if self.validate(choice) == True:
            pass
        else:
            print("Invalid choice, please try again\n")
            choice = self.getInput()
        return choice

    #Validate user input is as expected
    def validate(self,choice):
        if choice == "1" or choice == "2" or choice == "3":
            return True
        else:
            return False

    #Put together gameplay flow
    def gameplay(self):
    #Store choices of each user
        print(player1 + "")
        p1 = self.getInput()
        print(player2 + "")
        p2 = self.getInput()
        os.system('clear')
    #displays the selected choice
        print(player1.upper()+' selected '+p1.upper())
        print(player2.upper()+' selected '+p2.upper())

        points = self.score(p1,p2)
        return points

    #Takes each player's choice as an argument
    #Determines the winner and awards a point
    #per round
    def score(self,p1,p2):

    #if p1 is equal to p2 generate TIE
        if p1 == p2:
            print("Tie! Try Next Round!\n")
            points = (0,0)

    #This code will generate p1 wins because paper covers rock
        elif p1 == "3" and p2 == "1":
            print(player1.upper() + "\nWin This Round!\n")
            print('Paper covers Rock')
            print('[(1)ROCK, (2)SCISSORS, (3)PAPER]\n')
            points = (1,0)

    #This code will generate p2 wins because rock smashes scissors
        elif p1 == "2" and p2 == "1":
            print(player2.upper() + " Win This Round!\n")
            print('Rock smashes Scissors')
            print('[(1)ROCK, (2)SCISSORS, (3)PAPER]\n')
            points = (0,1)


    #This code will generate p2 wins because paper covers rock
        elif p1 == "1" and p2 == "3":
            print(player2 + " Win This Round!\n")
            print('Paper covers Rock')
            print('[(1)ROCK, (2)SCISSORS, (3)PAPER]\n')
            points = (0,1)


    #This code will generate p1 wins because scissors cuts paper
        elif p1 == "2" and p2 == "3":
            print(player1 + " Win This Round!\n")
            print('Scissors cuts Paper')
            print('[(1)ROCK, (2)SCISSORS, (3)PAPER]\n')
            points = (1,0)


    #This code will generate p1 wins because rock smashes scissors
        elif p1 == "1" and p2 == "2":
            print(player1 + " Win This Round!\n")
            print('Rock smashes Scissors')
            print('[(1)ROCK, (2)SCISSORS, (3)PAPER]\n')
            points = (1,0)


    #This code will generate p2 wins because scissors cuts paper
        elif p1 == "3" and p2 == "2":
            print(player2 + " Win This Round!\n")
            print('Scissors cuts Paper')
            print('[(1)ROCK, (2)SCISSORS, (3)PAPER]\n')
            points = (0,1)

        return points


#Before executing the code, it will define a few special variables. For example, if the python interpreter is running 
#that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__".
#If this file is being imported from another module, __name__ will be set to the module's name.
if __name__ == "__main__":
    game = Game()
#determine how many rounds to play
    while True:
        try:
            num_rounds = int(input("How many points does it take to win? \n"))
            break
        except ValueError:
            print("input a integer")

#player's identity
    player1 = input("Enter your name player 1: ")
    player2 = input("Enter your name player 2: ")

#this part is responsible for summing-up the scores and declare the overall winner.
    gamescore = [0,0]
    while gamescore[0] < num_rounds and gamescore[1] < num_rounds:
        points = game.gameplay()
        gamescore[0] += points[0]
        gamescore[1] += points[1]
        print(player1.upper() + " has " + str(gamescore[0]) + " points")
        print(player2.upper() + " has " + str(gamescore[1]) + " points\n")
        if gamescore[0] == num_rounds:
            print(player1.upper() + " has Won\nGAME OVER!\n")
        elif gamescore[1] == num_rounds:
            print(player2.upper() + " has Won\nGAME OVER!\n")

#after the declaration of winner in every round it will ask the players if they want to play another round.
    # if (raw_input('Do you want to play another round, yes or no?\n')).lower().startswith('y'):
    # continue
    # print('GAME OVER')
    # break