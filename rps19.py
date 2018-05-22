import random

def rock_paper_scissors():
    playerscore = 0
    computerscore = 0
    rounds = input('\nHow many points does it take to win?: ')
    count = 1
    while playerscore or computerscore != int(rounds):
        print('\n********************* ROUND #',count,'*********************')
        player = input('\nPick your throw: [r]ock, [p]aper, or [s]cissors?: ')
        computerthrow = random.randint(0,2)
        if (computerthrow == 0):
            computer = "rock"
            computer = 'r'
        elif (computerthrow == 1):
            computer = "paper"
            computer = 'p'
        elif (computerthrow == 2):
            computer = "scissors"
            computer = 's'
        if (player == computer):
            print('Tie!')
            while (player == computer):
                player = input('\nPick your throw: [r]ock, [p]aper, or [s]cissors?: ')
                computerthrow = random.randint(0,2)
                if (computerthrow == 0):
                    computer = "rock"
                    computer = 'r'
                elif (computerthrow == 1):
                    computer = "paper"
                    computer = 'p'
                elif (computerthrow == 2):
                    computer = "scissors"
                    computer = 's'      
                print(computer)
        elif (player == 'r'):
            if (computer == "p"):
                print('Computer threw paper, you lose!')
                computerscore=computerscore+1
            else:
                print('Computer threw scissors, you win!')
                playerscore = playerscore+1
            #count = count + 1
        elif (player == 'p'):
            if (computer == "r"):
                print('Computer threw rock, you win!')
                playerscore = playerscore+1
            else:
                print('Computer threw scissors, you lose!')
                computerscore=computerscore+1
            #count = count + 1
        elif (player == 's'):
            if (computer == "p"):
                print('Computer threw paper, you win!')
                playerscore = playerscore+1
            else:
                print('Computer threw rock, you lose!')
                computerscore=computerscore+1
    count = count = +1
    print('Your score: ',playerscore)
    print('Computer''s score: ',computerscore,'\n')
    print('********************* GAME OVER ********************')

def main(): 
    print('ROCK PAPER SCISSORS in Python')
    print()
    print('Rules: 1) Rock wins over Scissors.')
    print('       2) Scissors wins over Paper.')
    print('       3) Paper wins over Rock.')

    rock_paper_scissors()

main()