import random

def game(choice):

    options = ["rock", "paper", "scissors"]
    bot = random.choice(choice)

    if choice == "rock" and bot == "scissors":
        print("you chose rock and i played scissors, YOU WIN!")

    elif choice == "rock" and bot == "paper":
        print (" you chose rock and i played paper, YOU LOSE!")

    elif choice == "rock" and bot == "rock":
        print ("we chose the same thing...")

    elif choice == "paper" and bot == "paper":
        print ("we chose the same thing.")

    elif choice == "paper" and bot == "scissors":
        print ("you chose paper and i chose scissors, you lose!")

    elif choice == "paper" and bot == "rock":
        print ("you chose paper and i chose rock, you win!")

    elif choice == "scissors" and bot == "scissors":
        print ("We chose the same thing")

    elif choice == "scissors" and bot == "paper":
        print ("you chose scissors and i chose paper, YOU WIN!")

    elif choice == "scissors" and bot == "rock":
        print ("you chose scissors and i chose rock, YOU LOSE!")

    def again(x):

        while True:
            if x == "y":
                game(raw_input("rock, paper or scissors? "))
                again(raw_input("play again? y / n. "))
            else:
                print "goodbye"
                break
                break

        game(raw_input("rock, paper or scissors? "))
        again(raw_input("play again? y / n" ))