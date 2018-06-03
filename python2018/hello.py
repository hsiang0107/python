import sys
print('Hello', sys.argv[1], '!')

name = input('input name again:')
file1 = open('hello.txt', 'w')
print('hello', name, '!', file=file1)

