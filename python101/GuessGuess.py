import random
from util import do_guess

__author__ = 'productiontwic'

answer = random.sample(range(10), 4)

while 1:
    s = input('Input 4 digits number or input i for the answer: ')
    if (s == 'i') | (s == 'I'):
        ans_str = list(map(str, answer))
        print(''.join(ans_str))
        break
    slist = list(s)
    try:
        my_guess = list(map(int, slist))
    except ValueError:
        print('Number must be integer')
        continue

    if (len(my_guess) != len(set(my_guess))) | (len(my_guess) != 4):
        print('Must enter 4 numbers and each number should be unique')
        continue
    elif my_guess == answer:
        print('BINGO !')
        break
    else:
        do_guess(my_guess, answer)
        continue
