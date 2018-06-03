InputStr = input('Please input an integer:')
num = int(InputStr)
if num <= 0:
    raise ValueError('must greater than 0 !')

for first in range(1, num+1):
    for second in range(1, num+1):
        result = first * second
        print('{0} * {1} = {2}'.format(first, second, result))
    print('')




