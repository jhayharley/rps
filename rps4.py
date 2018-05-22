##Rules
##Rock beats scissors
##Scissors beats paper
##Paper beats rock

def rockPaperSci(p1, opt1, p2, opt2):
	if options.index(opt1) - options.index(opt2) == 1:
		print('\n' + p1 + ' wins')

	elif options.index(opt1) - options.index(opt2) == -1:
		print('\n' + p2 + ' wins')

	elif options.index(opt1) - options.index(opt2) == -2:
		print('\n' + p1 + ' wins')

	elif options.index(opt1) - options.index(opt2) == 2:
		print('\n' + p2 + ' wins')

	else:
		print('\nTie')

	options = ['scissors', 'rock', 'paper']
	player1Name = input('player 1 name: ')
	player2Name = input('player 2 name: ')

	while True:
	player1Option = input('\n'+ player1Name + ' choose from rock, paper or scissors: ')
	if player1Option not in options:
		print(player1Option + ' is an invalid option. Try again')
	continue

	else:
	break

	while True:
	player2Option = input('\n' + player2Name + ' choose from rock, paper or scissors: ')
	if player2Option not in options:
		print(player2Option + ' is an invalid option. Try again')
	continue

	else:
	break

	rockPaperSci(player1Name, player1Option, player2Name, player2Option)

	while True:
	tryAgain = int(input('\nEnter 0 to exit and 1 to try again: '))

	if tryAgain == 1 or tryAgain == 0:
	break
	else:
		print(str(tryAgain) + ' is invalid option')
	continue

	if tryAgain == 1:
	continue
	else:
	break