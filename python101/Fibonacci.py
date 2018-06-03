__author__ = 'productiontwic'

while 1:
    try:
        n = input('Input Fib(N): ')
        if int(n) < 0:
            print('N must >= 0')
            continue
        else:
            break
    except ValueError:
        print('N must be integer')

fib_lit = [0, 1]
FibN = int(n)

for key in range(2, FibN + 1):
    fib_lit.append(fib_lit[key - 2] + fib_lit[key - 1])

print('Fib( {} ) = {}'.format(FibN, fib_lit[FibN]))

