# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C, D):
    # write your code in Python 3.6
    max = 0
    LST = [A, B, C, D]
    for x in LST:
        n = LST.index(x)
        for y in LST[n+1:]:
            m = LST[n+1:].index(y)
            lst_tmp = LST[n+1:]
            lstA= [x,y]
            if m == 0:
                lstB= lst_tmp[m+1:]
            elif m == 1:
                lstB[0] = lst_tmp[(m - 1)]
                lstB[1] = lst_tmp[(m + 1)]
            elif m == 2:
                lstB = lst_tmp[0:m]
            #print(lstA, y, LST[n+1:], m, lstB)
            sqr = (lstA[0] - lstB[0]) ** 2 + (lstA[1] - lstB[1]) ** 2

            if sqr > max:
                max = sqr

    return max


result = solution(1,1,2,3)