import sys

def sum(a,b,c):
    total=a+b+c

    return total


number=(1,3,5)
print(sum(*number))

def sumdict(a,b,c):
    total=a+b+c
    return total

dict1={'a':1, 'b':3, 'c':5}
print(sumdict(**dict1))