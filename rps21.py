#Programmer: 
import random as ran
import shelve

class Score(object):
    """Place where all scores are stored for save document"""

    def __init__(self):
        """Makes all variables set to 0"""
        self.rounds = 0
        self.losses = 0
        self.wins = 0
        self.draws = 0
        self.game_wins = 0
        self.game_losses = 0
        self.total_rounds = 0
        self.total_games = 0
        self.round_wins = 0
        self.round_losses = 0
        self.round_draws = 0

    def reset(self):
        """Resets the scores for next game"""
        self.wins = 0
        self.draws = 0
        self.losses = 0

    def tally(self):
        """Adds the score to stats"""
        self.total_rounds += self.rounds
        self.total_games += 1
        self.round_wins += self.wins
        self.round_losses += self.losses
        self.round_draws += self.draws

    def stats(self):
        """Prints the stats"""
        print ('\n\n+++++++++++++++++++++-=Stats=-+++++++++++++++++++')
        print ('=================================================')
        print ('|--           --|--   Rounds  --|--   Games   --|')
        print ('|--   Wins    --|--     %s     --|--     %s     --|')    %(self.round_wins, self.game_wins)
        print ('|--   Losses  --|--     %s     --|--     %s     --|')    %(self.round_losses, self.game_losses)
        print ('|--   Draws   --|--     %s     --|--    N/A    --|')    %(self.round_draws)
        print ('|--   Played  --|--     %s     --|--     %s     --|\n\n')%(self.total_rounds, self.total_games)

    def final(self):
        """Prints final score of the game just played"""
        print ('\n\n+++++++++++Final Score++++++++++')
        print ('================================')
        print ('|--   Wins    --|--    %s     --|')    %(self.wins)
        print ('|--   Losses  --|--    %s     --|')    %(self.losses)
        print ('|--   Draws   --|--    %s     --|')    %(self.draws)
        print ('|--   Rounds  --|--    %s     --|\n\n')    %(self.rounds)


def custom_input(question, choices):
    """A custom loop that checks to see if choices is valid"""
    response = raw_input(question).lower()
    while response not in choices:
        print ("Correct inputs: ")
        for c in choices:
            print(c)
        response = raw_input(question).lower()
    return response


class Game(object):
    """Main game"""
    def __init__(self):
        """Starts the program here."""
        try:                                    
            f = shelve.open("RPS_save.dat")     
            statistics = f["statistics"]        
            self.score = statistics[0]          
            f.close()
        except:
            self.score = Score()
            f = shelve.open("RPS_save.dat")
            statistics = [self.score]
            f["statistics"] = statistics
            f.sync()
            f.close()
        self.Continue = None
        self.game = None
        self.plays = ['rock', 'paper', 'scissors']
        self.games = ['1', '3', '5']
        self.modes = ['pvc', 'cvc']
        self.p1win = [('rock' + 'scissors'), ('paper' + 'rock'), ('scissors' + 'paper')]
        self.menu = [('stats'), ('play'), ('quit')]
        while self.Continue is None:
            self.Continue = raw_input("Welcome to the greatest, mind blowing, challenge of all "
                    "time.\n   - Rock, Paper, Scissors! \nMany have tried and many have"
                    " FAILED... \nThis will be a test between the human mind and"
                    " my AI.\nPress \"enter\" when you believe your ready for this "
                    "challenge.\n")
        print "Good Luck... Human."
        while True:
            self.game = custom_input("Would you like to play, look at stats, or quit?\n", self.menu)
            if self.game == "play":
                self.rounds = custom_input("How many rounds would you like? \n", self.games)
                self.play_game()
                self.score.tally()
                self.score.final()
                self.score.reset()
                f = shelve.open("RPS_save.dat")
                statistics = [self.score]
                f["statistics"] = statistics
                f.sync()
                f.close()
            elif self.game == "stats":
                self.score.stats()
            if self.game == "quit":
                break


    def play_game(self):
        """This is where most of the game takes place"""
        while self.score.rounds != int(self.rounds):
            self.score.rounds += 1
            self.user_choice = custom_input("What is your choice, human! \n  ",self.plays)
            self.computer_choice = self.computer_choice_gen()
            print "\nComputer choice is %s"    %(self.computer_choice)
            result = self.evaluate()
            if result == "win":
                print "%s beats %s! The human wins this round.\n\n"   %(self.user_choice.capitalize(), self.computer_choice)
                self.score.wins += 1
            elif result == "loss":
                print "%s beats %s! Hahaha! You lost this round!\n\n" %(self.computer_choice.capitalize(), self.user_choice)
                self.score.losses += 1
            else:
                print "I knew you were going to pick %s!\n\n"        %(self.user_choice.capitalize())
                self.score.draws += 1
        self.finals()

    def finals(self):
        """Adds win /losses to scores"""
        if self.score.wins > self.score.losses:
            self.score.game_wins += 1
            print "Looks like humans are still dominant in this time. You won the Game!"
        else:
            self.score.game_losses += 1
            print "Humans are no match for my AI."

    def computer_choice_gen(self):
        """Generates computer choice"""
        return ran.choice(self.plays)

    ##def computer_choice():
    ##    chance = ran.randint(0, 99)
    ##    if chance > 66:
    ##        return "rock"
    ##    elif chance < 33:
    ##        return "paper"
    ##    else:
    ##        return "scissors"

    def evaluate(self):
        """Determines whether game is a win loss or draw"""
        if self.user_choice + self.computer_choice in self.p1win:
            return "win"
        elif self.user_choice == self.computer_choice:
            return "draw"
        else:
            return "loss"


Game()