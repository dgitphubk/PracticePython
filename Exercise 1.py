from datetime import date, datetime, timedelta

name = input('Enter your name: ')
age = input('What\'s your age, ' + name + '? ')
intage = int(age)
diffage = 100 - intage
# year = timedelta(days=365)
# diffyear = year * diffage
now = datetime.now()
# centyear = now.year + diffyear
centyear = now.year + diffage - 1
message = ('Hi ' + name + ', you will turn 100 years old in ' + str(diffage) + ' years. That\'ll be the year ' + str(centyear) + '.\n')
print(message * 100)