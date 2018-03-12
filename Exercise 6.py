# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

maypal = input('Enter a string: ')
backwise = maypal[::-1]

if maypal == backwise:
	print('{} is a palindrome'.format(maypal))
else:
	print('{} is not a palindrome'.format(maypal))