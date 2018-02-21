# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

from datetime import date, datetime, timedelta

name = input('Enter your name: ')
age = input('What\'s your age, ' + name + '? ')
intage = int(age)
diffage = 100 - intage
now = datetime.now()
centyear = now.year + diffage - 1
message = ('Hi ' + name + ', you will turn 100 years old in ' + str(diffage) + ' years. That\'ll be the year ' + str(centyear) + '.\n')
print(message * 100)