#rock,paper,scissors
#inputs of player 1 and player 2
t = ["Rock","Paper","Scissors"]
p = ''
pp = ''
while p not in {"Rock", "Paper", "Scissors"}:
  p = raw_input("Player 1, please enter Rock,Paper, or Scissors!")
while pp not in {"Rock", "Paper", "Scissors"}:
  pp = raw_input("Player 2, please enter Rock,Paper or Scissors!")
#player 1 values of choice
if p == "Rock":
    p = 1
elif p == "Paper":
    p = 2
elif p == "Scissors":
    p = 3
else:
    print("You have entered a wrong hand")
#player 2 values of choice
if pp == "Rock":
    pp = 1
elif pp == "Paper":
    pp = 2
elif pp == "Scissors":
    pp = 3
#outcomes of the Game
if p > pp:
    print("Player 1 Wins")
elif p < pp:
    print("Player 2 Wins")
elif p == pp:
    print("Players Draw")