__author__ = 'twlhgs'

init = 2
value1, value2 = input('Input start and end separated by space: ').split()
start = int(value1)
end = int(value2)

def is_prime(i, target):
    if target == 2:
        return True
    elif target % i == 0:
        return False
    elif i == (target - 1):
        return True
    else:
        try:
            i += 1
            return is_prime(i, target)
        except RuntimeError:
            print('Value out of range')

for num in range(start, end + 1):
    if (num == 0) | (num == 1):
        continue
    elif not is_prime(init, num):
        continue
    else:
        print(num, ' ', end='')
        continue
