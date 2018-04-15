# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random
import string

a = 0
b = random.randint(1, 9)
guess = 0
again = 'Y'

print('I want to play a game.')
while again == 'Y':
	while guess != b and guess != 'exit':
		guess = input('Pick a number between 1 and 9, or exit: ')
		if guess == 'exit':
			break
		guess = int(guess)
		a += 1
		if guess < b:
			print('Too low.')
		elif guess > b:
			print('Too high.')
		else:
			print('You won the game in', a, 'attempts.')
	again = input('Play again Y/N? ').upper()
	if again == 'N':
		print('Bye.')
	else:
		guess = 0
		a = 0
		b = random.randint(1, 9)