a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
y = []

for i in a:
	if i < 5:
		x.append(i)

print(x)

b = int(input('Pick a number: '))

for i in a:
	if i < b:
		y.append(i)

print('The following elements are less than ' + str(b) + ': ' + str(y))