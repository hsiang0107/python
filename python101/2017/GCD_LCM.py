value1, value2 = input('enter two integer separated by space:').split()
try:
    n1 = int(value1)
    n2 = int(value2)
except ValueError:
    print('Invalid iput ! Values must be integer and separated by space')


if n1 >= n2:
    m, n = n2, n1
else:
    m, n = n1, n2

lst1 = []
GCD = 1
while True:
    for count in range(2, m+1):
        if (m % count ==0) & (n % count ==0):
            lst1.append(count)
            m //= count
            n //= count
            break
    else:
        p1 = m
        p2 = n
        break

print(lst1, p1, p2)

for elem in lst1:
    GCD *= elem

LCM = GCD * p1 * p2

print('GCD = {0}, LCM = {1}'.format(GCD, LCM))
