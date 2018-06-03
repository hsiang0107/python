def sum(*numbers):
    total=0
    for num in numbers:
        total += num
    return total

def sum2(a, b, c):

    return a+b+c

#dic1=dict([('a', 1), ('b', 2), ('c', 3)])
dic1 = {'a':1, 'b':2, 'c':3}
print(sum2(**dic1))