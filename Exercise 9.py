# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random
import string

a = 0
b = random.randint(1, 9)
guess = 0

print('I want to play a game.')
# while True:
	# guess = input('Guess a number between 1 and 9 or exit: ')
	# if guess.lower() == 'exit':
		# print('Goodbye.')
		# break
	# elif int(guess) != b:
		# guess = int(guess)
		# while guess != b:
			# if guess < b:
				# a = a + 1
				# guess = input('Too low. Guess again or exit: ')
				# if guess.lower() != 'exit':
					# guess = int(guess)
			# else:
				# a = a + 1
				# guess = input('Too high. Guess again or exit: ')
				# if guess.lower() != 'exit':
					# guess = int(guess)
	# else:
		# guess = int(guess)

# print('You win! It took you {} guesses.').format(a)