#Rock Paper Scissor
#Two-player (Player Vs PC) Rock-Paper-Scissor game.
#Rock beats scissors,Scissors beats paper,Paper beats rock

import random
    
def select(i):
    list=['Rock','Paper','Scissor']
    i=input("Select your object from Rock, Paper and Scissor:")
    while i not in list:
        i=input("Invalid selection.Select your object from Rock, Paper and Scissor:")
    return i          

def random_selection(i):
    i=random.choice(['Rock','Paper','Scissor'])
    return i
 
input_1=select(1)
input_2=random_selection(2)
print('Player 1 selected '+input_1)
print('Player 2 selected '+input_2)

while input_1=='Rock':
    if input_2=='Scissor':
        print('Player 1 wins')
    elif input_2=='Rock':
        print ('Tie')
    else: 
        print ('Player 2 wins')
    break

while input_1=='Paper':
    if input_2=='Rock':
        print('Player 1 wins')
    elif input_2=='Paper':
        print ('Tie')
    else: 
        print ('Player 2 wins')
    break

while input_1=='Scissor':
    if input_2=='Paper':
        print('Player 1 wins')
    elif input_2=='Scissor':
        print ('Tie')
    else: 
        print ('Player 2 wins')
    break