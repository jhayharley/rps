import random
from getpass import getpass
import pickle

#I'll use class for easy load, easy dump.
class GameStatus():
    def __init__(self, name):
        self.tie = 0
        self.playerWon = 0
        self.pcWon = 0
        self.name = name

    def get_round(self):
        return self.tie + self.playerWon + self.pcWon + 1

# Displays program information, starts main play loop
def main():
    print "Welcome to a game of Rock, Paper, Scissors!"
    print "What would you like to do?" 
    print  "" 
    game_status  = welcomemenu()
    while True:
        play(game_status)
        endGameSelect(game_status)

#prompt user's choice and return GameStatus instance
def welcomemenu():
    #changed a logic to handle unexpected user input.
    while True:
        print "[1]: Start New Game"
        print "[2]: Load Game"
        print "[3]: Quit"
        print ""
        menuselect = input("Enter choice: ")
        if menuselect in [1, 2, 3]:
            break
        else:
            print "Wrong choice. select again."

    if menuselect == 1:
        name = raw_input("What is your name?: ") # raw_input for string
        print "Hello %s." % name
        print "Let's play!"
        game_status = GameStatus(name) #make a new game status
    elif menuselect == 2:
        while True:
            name = raw_input("What is your name?: ")
            try:
                player_file = open('%s.rsp' % name, 'r')
            except IOError:
                print "There's no saved file with name %s" % name
                continue
            break
        print "Welcome back %s." % name
        print "Let's play!" 
        game_status = pickle.load(player_file) #load game status. not dump.
        displayScoreBoard(game_status)
        player_file.close()
    elif menuselect == 3:
        print "Bye~!"
        exit()
        return

    return game_status


# displays the menu for user, if input == 4, playGame in the calling function (main()) is False, terminating the program.
# Generate a random int 1-3, evaluate the user input with the computer input, update globals accordingly, returning True
# to playGame, resulting in the loop in the calling function (main()) to continue.
def play(game_status):
    playerChoice = int(playerMenu())
    #this if statement is unnecessary. playerMenu() already checked this.
    #if playerChoice == 4:
    #    return 0
    pcChoice = pcGenerate()
    outcome = evaluateGame(playerChoice, pcChoice)
    updateScoreBoard(outcome, game_status)


# prints the menu, the player selects a menu item, the input is validated, if the input is valid, returned the input, if
# the input is not valid, continue to prompt for a valid input
# 1 - rock
# 2 - paper
# 3 - scissors

def playerMenu():
    print "Select a choice: \n [1]: Rock \n [2]: Paper \n [3]: Scissors\n" 
    menuSelect = getpass("What will it be? ")
    while not validateInput(menuSelect):
        invalidChoice(menuSelect) #I think this function is un necessary. just use print.
        menuSelect = getpass("Enter a correct value: ")
    return menuSelect


# if the user doesn't input a 1-3 then return false, resulting in prompting the user for another value. If the value
# is valid, return True
# takes 1 argument
# menuSelection - value user entered prior
def validateInput(menuSelection):
    if menuSelection in [1, 2, 3]: # more readable.
        return True
    else:
        return False


# return a random integer 1-3 to determine pc selection
# 1 - rock
# 2 - paper
# 3 - scissors
def pcGenerate():
    pcChoice = random.randint(1,2,3)
    return pcChoice


# evaluate if the winner is pc or player or tie, return value accordingly
# 0 - tie
# 1 - player won
# 2 - pc won
def evaluateGame(playerChoice, pcChoice):
    #more readable.
    rsp = ['rock', 'paper', 'scissors']
    win_statement  = ['Rock breaks scissors', 'Paper covers rock', 'Scissors cut paper']
    # if player win, win_status = 1 (ex. rock vs scissors -> (1 - 3 == -2) -> (-2 % 3 == 1))
    # if pc win, win_status = 2
    # if tie, win_status = 0
    win_status = (playerChoice - pcChoice) % 3
    print "You have chosen %s" % rsp[playerChoice - 1]
    what_to_say = "Computer has chose %s" % rsp[pcChoice - 1] 
    if win_status == 0:
        what_to_say += " as Well. TIE!"
    elif win_status == 1:
        what_to_say += ". %s. You WIN!" % win_statement[playerChoice - 1]
    else:
        what_to_say += ". %s. You LOSE!" % win_statement[pcChoice - 1]
    print what_to_say
    return win_status



# Update track of ties, player wins, and computer wins
def updateScoreBoard(outcome, game_status):
    if outcome == 0:
        game_status.tie += 1
    elif outcome == 1:
        game_status.playerWon += 1
    else:
        game_status.pcWon += 1

# If user input is invalid, let them know.
def invalidChoice(menuSelect):
    print menuSelect, "is not a valid option. Please use 1-3"


# Print the scores before terminating the program.
def displayScoreBoard(game_status):
    print ""
    print "Statistics:"
    print "Ties: %d" % game_status.tie
    print "Player Wins: %d" % game_status.playerWon
    print "Computer Wins: %d" % game_status.pcWon 
    if game_status.pcWon > 0:
        #if you don't use float, '10 / 4' will be '2', not '2.5'.
        print "Win/Loss Ratio: %f" % (float(game_status.playerWon) / game_status.pcWon) 
    else:
        print "Win/Loss Ratio: Always Win."
    print "Rounds: %d" % game_status.get_round()

def endGameSelect(game_status):
    print ""
    print "[1]: Play again"
    print "[2]: Show Statistics"
    print "[3]: Save Game"
    print "[4]: Quit"
    print ""
    while True:
        menuselect = input("Enter choice: ")
        if menuselect in [1, 2, 3, 4]:
            break
        else:
            print "Wrong input."

    if menuselect == 2:
        displayScoreBoard(game_status)
        endGameSelect(game_status)
    elif menuselect == 3:
        f = open("%s.rsp" % game_status.name, 'w')
        pickle.dump(game_status, f)
        f.close()
        print "Saved."
        endGameSelect(game_status)
    elif menuselect == 4:
        print "Bye~!"
        exit()
main()