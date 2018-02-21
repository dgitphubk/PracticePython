# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

basenum = int(input('Enter a number: '))

if basenum % 4 == 0:
	print('That number is divisible by 4.')
elif basenum % 2 == 0:
		print('That is an even number.')
else:
		print('That is an odd number.')
		
firstnum = int(input('Enter a new number: '))
secnum = int(input('Enter a second number: '))
modnum = firstnum % secnum

if firstnum % secnum == 0:
	print(str(firstnum) + ' is divisible by ' + str(secnum))
else:
	print(str(firstnum) + ' is not divisible by ' + str(secnum) + '. It leaves a remainder of ' + str(modnum) + '.')