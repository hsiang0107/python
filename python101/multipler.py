__author__ = 'productiontwic'


while 1:
    try:
        n = input('Input N: ')
        if int(n) <= 0:
            print('N must great than 0')
            continue
        else:
            break
    except ValueError:
        print('N must be integer')

for outer in range(int(n)):
    outer += 1
    for inner in range(int(n)):
        inner += 1
        print('{} * {} = {}'.format(outer, inner, outer*inner))
    print(end='\n')
