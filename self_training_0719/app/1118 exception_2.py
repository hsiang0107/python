__author__ = 'twlhgs'

try:
    lst = ["a", "b"]
    int(lst[1])

except (ValueError, IndexError) as e:
    print()


