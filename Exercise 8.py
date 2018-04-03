# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

import string

while True:
	a = input('Player 1: Rock, Paper, Scissors, Quit? ')
	a = a.lower()
	if a == 'quit':
		print('Player 1 Quit')
		break
	else:
		b = input('Player 2: Rock, Paper, Scissors? ')
		b = b.lower()
		if a == 'rock':
			if b == 'paper':
				print('Player 2 Wins')
			elif b == 'scissors':
				print('Player 1 Wins')
			else:
				print('Tie game')
		elif a == 'paper':
			if b == 'paper':
				print('Tie game')
			elif b == 'scissors':
				print('Player 2 Wins')
			else:
				print('Player 1 Wins')
		else:
			if b == 'scissors':
				print('Tie Game')
			elif b == 'paper':
				print('Player 1 Wins')
			else:
				print('Player 2 Wins')