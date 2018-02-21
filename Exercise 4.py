# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

numerator = int(input('Enter a number: '))
x = []
i = 1
while i <= numerator:
	if numerator % i == 0:
		print(str(numerator) + ' / ' + str(i) + ' = ' + str(int(numerator / i)))
		x.append(i)
	i = i + 1
	
print(x)