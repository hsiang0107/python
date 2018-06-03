import traceback

__author__ = 'productiontwic'

try:
    n = int(input('enter INT'))
    assert n < 100, 'n is too big'
    print(n)

except ValueError as valerr:
    print('you must enter INT\n')
    # traceback.print_exc()
    print(type(valerr))
    # print(valerr)
    print(valerr.args)
except (EOFError, KeyboardInterrupt):
    print('user interrupt')
else:
    print('no exception')
finally:
    print('must execute')

