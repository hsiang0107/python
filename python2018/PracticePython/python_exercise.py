import unittest
import csv

class Python_exercise(unittest.TestCase):
    def setup(self):
        None

    def teardown(self):
        None

    def test_get_birthday(self):
        bday_file = 'D:\\python\\pycharm\\python2018\\test_data\\birthday.csv'
        bday_dict = {}
        with open(bday_file, newline='') as csvfile:
            readcsv = csv.reader(csvfile, delimiter=',')
            for row in readcsv:
                bday_dict[row[0]] = row[1]
        name = input('Give me the name: ')
        if name in bday_dict:
            print(name + '\'' + 'birthday is ' + bday_dict[name])
        else:
            print(name + 'does not exist')


if __name__ == '__main__':
    unittest.main()