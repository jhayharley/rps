import os,random

def playerChoice():
    while True: #infinite loop that will keep repeating until we pick an option
        os.system("clear")
        choice = input("Pick one: (r)ock (p)aper (s)cissors")
        if choice.lower() in ["rock","r"]:
            return "rock"
        elif choice.lower() in ["paper","p"]:
            return "paper"
        elif choice.lower() in ["scissors","s"]:
            return "scissors"

def computerChoice():
    l = ["rock","scissors","paper"]
    return random.choice(l)


def playARound(currentRound,playerScore):
    print("RPS Game")
    print(" ")
    print(" ")
    print("Round :",currentRound)
    print(" ")
    print("Score - You: ",playerScore, "Computer: ",(currentRound - playerScore) - 1)
    input("Press enter to choose")
    pc =  playerChoice()
    cc = computerChoice()
    print("You:", pc,"       Computer:", cc)
    print(" ")
    if pc == cc:
        print("draw")
        roundScore = playARound(currentRound,playerScore)
    elif pc == "rock" and cc == "scissors":
        print("you win!")
        roundScore = 1
    elif pc == "paper" and cc == "rock":
        print("you win!")
        roundScore = 1
    elif pc == "scissors" and cc == "paper":
        print("you win!")
        roundScore = 1
    else:
        print("You lose!")
        roundScore = 0
    print(" ")
    print(" ")
    input("Press enter for the next round")
    return roundScore

def main():
    score = 0
    roundNo = 1
    for i in range(5):
        score = score + playARound(roundNo,score)
        roundNo += 1

    os.system("clear")
    print("Game Over       ")
    print("")
    print("")
    print("The final score is: ")
    print("Player: ",score, "out of 5")
    print("")
    if score > 2:
        print("You win, well done!")
    else:
        print("You lose! Loser!")
    print("")
    input("Press enter to play again")
    main()

main()