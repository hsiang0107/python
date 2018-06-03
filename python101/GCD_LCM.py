__author__ = 'productiontwic'

while 1:
    try:
        value1, value2 = input('Input 2 values separated by space: ').split()
        m = int(value1)
        n = int(value2)
        break
    except ValueError:
        print('Invalid iput ! Values must be integer and separated by space')

base = 1

while 1:
    min_mn = min(m, n)
    for key in range(2, min_mn+1):
        if (m % key == 0) & (n % key == 0):
            m = int(m / key)
            n = int(n / key)
            base *= key
            break
        else:
            continue
    else:
        break

GCD = base
LCM = GCD * m * n
print('GCD = {}, LCM = {}'.format(GCD, LCM))
