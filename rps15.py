#rock paper scissors gmae with a computer
#Created by Cassidy Bliss
#game introduction and initial assignments
import random
computer_weapon = random.randint(1,3)
player_name = input ("What is your name?")

print()
print("Well, hello" , player_name +  ". Welcome to a game of turning common household items and naturally occuring sediments into weapons of great destruction.")
print ("This game is greatly versitile can be used to solve a simple argument like where to go eat dinner, or deciding whether to get a divorce. ")
print ("We call it...")
print ("ROCK. PAPER. SCISSORS")
print()
player_choice = input("Type rock, paper, or scissors to begin the game")
print()
player_choice = player_choice.lower()
rounds = 1
player_score = 0
computer_score = 0 


#Loop 
while rounds <10  :
  print("Round:" , rounds)
  print()
  #Most specific to least specific outcomes
  if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors" :
    player_choice = input("That is not an option. please try again")
    print()
    player_choice = player_choice.lower()
    rounds +=0

  if player_choice == "rock" :
    player_weapon = 1
  elif player_choice == "paper" :
    player_weapon = 2
  elif player_choice == "scissors" :
    player_weapon = 3
    
  if computer_weapon == player_weapon :
    print("This round is a tie.")
    computer_score += 0
    player_score += 0
  elif computer_weapon ==1 and player_weapon==2 :
    print(player_name ,"wins. Conradulations. Your paper has covered the computer's rock. and somehow the rock has been deemed useless by the rules of this game.")
    player_score += 1
  elif computer_weapon ==1 and player_weapon==3 :
    print ("Computer wins")
    computer_score += 1
  elif computer_weapon ==2 and player_weapon==1 :
    print("Computer wins")
    computer_score += 1 
  elif computer_weapon ==2 and player_weapon==3 :
    print(player_name ,"wins. Good choice. Mom was right about scirrors being dangerous." , player_name)
    player_score += 1
  elif computer_weapon ==3 and player_weapon==1 :
    print(player_name , "wins. Congradulations warrior of the rock" )
    player_score += 1
  elif computer_weapon ==3 and player_weapon==2 :
    print("Computer wins")
    computer_score += 1
  else :
    print ("something is wrong")
  print ("{:25}{:3}".format( player_name +"'s score is:" , player_score))
  print("{:25}{:3}".format("Computer's score is:" , computer_score))
  print()
  player_choice = input("Enter your weapon of choice to play again")
  print()
  player_choice = player_choice.lower()
  rounds += 1 
  computer_weapon = random.randint(1,3)
  
print()
print("You played" , rounds , "rounds")
print()
if player_score > computer_score :
  print ( player_name ,"won the most rounds" )
elif player_score < computer_score :
  print ("Computer won the most rounds")
elif player_score == computer_score :
  print ("Overall score is a tie between computer and" , player_name)
else :
  print ("debug end score")