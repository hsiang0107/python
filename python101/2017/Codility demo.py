
def solution(A):
    # write your code in Python 3.6
    setA = set(A)
    CleanA = list(setA)
    print(setA, CleanA)
    start = CleanA[0]
    while True:
        if (start in CleanA) is False:
            break
        else:
            start += 1
    return start



A = [-1, 3, 6, 4, 1, 2]
# solution(A)
result = solution(A)
print(result)