# from player import Player
import random


class Rps(object):

    def __init__(self, human=True):
        self.human = human
        self.player = self.create_player()
        self.computer = 'Alfred'
        self.winner = None
        self.loser = None


    def create_player(self):   # Captures the name of the human player.
        if self.human:
            name = raw_input("Please enter your name: ")
            return name

    def play_game(self):
        while self.winner is None:
            self.pause()                        # Insert a pause so that the player has time to brace himself before the action starts.
            player = Player()
            hand_p = plyr.player_hand()       # Call player_hand method to get the player's hand.
            hand_c = plyr.computer_hand()     # Call computer_hand method to get the computer's hand.
            self.display_play(hand_p, hand_c)

            if hand_p == hand_c:
                print "Tie! Ugh..."
                self.play_game()
            elif hand_p == 'rock' and hand_c == 'scissor':
                self.winner = self.player
                self.loser = self.computer
                self.display_winner(self.winner, self.loser)
            elif hand_p == 'paper' and hand_c == 'scissor':
                self.winner = self.computer
                self.loser = self.player
                self.display_winner(self.winner, self.loser)
            elif hand_p == 'rock' and hand_c == 'paper':
                self.winner = self.computer
                self.loser = self.player
                self.display_winner(self.winner, self.loser)
            elif hand_p == 'scissor' and hand_c == 'paper':
                self.winner = self.player
                self.loser = self.computer
                self.display_winner(self.winner, self.loser)
            elif hand_p == 'paper' and hand_c == 'rock':
                self.winner = self.player
                self.loser = self.computer
                self.display_winner(self.winner, self.loser)
            elif hand_p == 'scissor' and hand_c == 'rock':
                self.winner = self.computer
                self.loser = self.player
                self.display_winner(self.winner, self.loser)

    def display_play(self, hand_p, hand_c):
        print "{} plays {}.".format(self.player, hand_p)
        print "{} plays {}.".format(self.computer, hand_c)


    def display_winner(self, winner, loser):
        print "{} has lost. {} has won. Long live {}!".format(self.loser, self.winner, self.winner)


    def pause(self):    # Requires the human to hit enter before continuing.
        if self.human:
            raw_input("Press 'enter' when you're ready to play against Alfred (the computer).")


if __name__ == "__main__":
    game = Rps()
    game.play_game()