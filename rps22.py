import random,os,time
score = {'human':0,'robot':0}
def game(): #Basic Game code.
    time.sleep(1)
    os.system('clear')
    print('IA: ' + str(score['robot']) + ' Human: ' + str(score['human']))
    print('1.Rock 2.Scissors 3.Paper')
    while True:
        try:
            choice = int(input("Input your choice:\n"))
            if choice < 1 or choice > 3: #Valid number but outside range, don't let through
                raise ValueError
            else: #Valid number within range, quit loop and the variable selection contains the input.
                break
        except ValueError: #Invalid input
            print("Enter a number from 1 to 3.")
    rchoice = random.randint(1,3)
    time.sleep(1)
    if rchoice == 1:
        print('IA choice is Rock.')
    elif rchoice == 2:
        print('IA choice is Scissors.')
    elif rchoice == 3:
        print('IA choice is Paper.')

    if (rchoice==1 and choice==2) or (rchoice==2 and choice==3) or (rchoice==3 and choice==1):
        print('IA wins!\n')
        score['robot'] += 1
        time.sleep(0.5)
    elif (rchoice == choice):
        print("Draw, let's repeat")
        time.sleep(0.5)
        game()
    else:
        print('You win!\n')
        time.sleep(0.5)
        score['human'] += 1

def startgame(): #The introduction of the game.
    os.system('clear')
    print('Rock-Paper-Scissors v.1')
    print('Developed by P.R.B.\n')
    ngames = int(input('How many games do you want to play?\n'))
    time.sleep(1)
    i = 0
    while i != ngames:
        game()
        i += 1
    print('Final Score:')
    print('IA: ' + str(score['robot']) + ' Human: ' + str(score['human']))
    if score['human'] > score['robot']:
        print('You win the game!\n')
    else:
        print('Game Over')
        print('IA wins the game!\n')

startgame()