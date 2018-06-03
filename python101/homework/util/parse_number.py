__author__ = 'twlhgs'

class ParseNumber:

    def __init__(self):
        pass

    def is_palindrome(self, num):
        palindrome = True
        forw_lst = list(str(num))
        backw_lst = forw_lst[::-1]
        for n in range(len(forw_lst)):
            if forw_lst[n] != forw_lst[-(n + 1)]:
                palindrome = False
        return palindrome

sample = 1357531
ex3 = ParseNumber()
result = ex3.is_palindrome(sample)
# print(result)