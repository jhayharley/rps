def ppt():

	a= [ 'paper', 'rock', 'scissors']

	n = raw_input('Enter rock, paper or scissors : ')

	import random

	pc= random.choice(a)

	print pc

	if n == 'paper' :

		if pc == 'paper':

			print 'Draw'

	elif pc == 'rock':

			print 'You win!'

	else:

			print 'You lose'

	elif n == 'rock' :

	if pc == 'paper':

			print 'You lose'

	elif pc == 'rock':

			print 'Draw'

	else:

			print 'You win!'

	elif n == 'scissors':

	if pc== 'rock':

			print 'You lose'

		elif pc == 'paper':

			print 'You win'

	else:

			print 'Draw'

	else:

			print 'Invalid input! You have not entered rock, paper or scissors, try again'