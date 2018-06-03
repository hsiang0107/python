# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime


class CountAge:
    def __init__(self):
        pass

    def turn_100_years_old(self, age):
        if(age >= 0):
            now = datetime.datetime.now(tz=None)
            current_year = now.year
            return current_year + (100-age)
        else:
            print('Age cannot be minus')
            return None

    def test(self):
        now = datetime.datetime.now(tz=None)
        print(now.year, type(now.year))


your_name = input('Enter your name')
try:
    age_string = input('Enter your age')
    your_age = int(age_string)
except ValueError:
    print('Please input integer !')

my_age = CountAge()
when = my_age.turn_100_years_old(your_age)
if(when is None):
    pass
else:
    print('{0}, you will turn into 100 in year {1}'.format(your_name, when))

# Testing
# my_age = CountAge()
# my_age.test()