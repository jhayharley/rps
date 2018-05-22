import time
import random
from getpass import getpass

print("               RULES: The  players must input their own choice and patiently wait for their turn!" )
print("                   DESCRIPTION: Paper Covers Rock, Rock Smashes Scissors, Scissors Cuts Paper\n")
print("                                 ***Welcome to Rock, Paper Scissors Game***")
print("                                     >>>Best out of 5 wins. Goodluck!<<< \n")

def getInput():
    choice = getpass("\nrock, paper, or scissors:\n")
    if validate(choice) == True:
        pass
    else:
        print("Invalid choice, please try again\n")
        choice = getInput()
    return choice

# def select(i):
#     list=['Rock','Paper','Scissor']
#     i=input("Select your object from Rock, Paper and Scissor:")
#     while i not in list:
#         i=input("Invalid selection.Select your object from Rock, Paper and Scissor:")
#     return i

#Validate user input is as expected
def validate(choice):
    if choice == "rock" or choice == "paper" or choice == "scissors":
        return True
    else:
        return False

#Put together gameplay flow
def gameplay():
    #Store choices of each user
    print(player1 + "\nmake your choice!")
    p1 = getInput()
    print(player2 + "\nmake your choice!")
    p2 = getInput()


    print(player1+' selected '+p1)
    print(player2+' selected '+p2)

    points = score(p1,p2)
    return points

time.sleep(1)
rounds = int(raw_input("How many rounds would you like to play?\n"))
counter = 0
while counter <= rounds-1:
    while rounds not in range(3,11):
        try:
            rounds = int(raw_input("Sorry! I can only play between 3 and 10 rounds. Try again:"))
        except:
            print ("ERROR invalid input. Out of range or wrong type of data.")
    if rounds in range(3,11):
        time.sleep(1)
        print ("Challenge accepted! I will play you for", rounds,"rounds! Let's begin!!!")
    options = ("rock","paper","scissors")
    userChoice = getpass("Rock, Paper or Scissors, peasant?")
    while userChoice not in options:
        try:
            userChoice = raw_input("Not an option lad. Rock, paper or scissors")
        except:
            print ("ERROR invalid input. Out of range or wrong type of data.")
    cpuoption1 = "rock"
    cpuoption2 = "paper"
    cpuoption3 = "scissors"
    cpuChoice = random.randint(1,3)
    answer = ""
    if cpuChoice == 1:
        answer = cpuoption1
    elif cpuChoice == 2:
        answer = cpuoption2
    elif cpuChoice == 3:
        answer = cpuoption3
    print ("I choose", answer,"!")
    user= 0
    cpu = 0
    if userChoice == "rock" and answer == cpuoption1:
        user += 1
        cpu += 1
        print ("Draw!")
        counter += 1
    elif userChoice == "paper" and answer == cpuoption2:
        user+=1
        cpu+=1
        print("Draw!")
        counter += 1
    elif userChoice == "scissors" and answer == cpuoption3:
        user+=1
        cpu+=1
        print ("Draw!")
        counter += 1
    elif userChoice == "rock" and answer == cpuoption2:
        cpu+=1
        print ("CPU wins the round!")
        counter += 1
    elif userChoice == "rock" and answer == cpuoption3:
        user+=1
        print ("Player wins the round!")
        counter += 1
    elif userChoice == "paper" and answer == cpuoption1:
        user+=1
        print ("Player wins the round!")
        counter += 1
    elif userChoice == "paper" and answer == cpuoption3:
        cpu+=1
        print ("CPU wins the round!")
        counter += 1
    elif userChoice == "scissors" and answer == cpuoption1:
        cpu+=1
        print ("CPU wins the round!")
        counter += 1
    elif userChoice == "scissors" and answer == cpuoption2:
        user+=1
        print ("Player wins the round!")
        counter += 1
    if cpu==rounds:
        print("CPU beat the player!")
    elif user==rounds:
        print("Player beat the CPU!")
        counter += 1
    elif cpu==rounds and user==rounds:
        print("Looks like that was a draw! Good game!")
        counter += 1

