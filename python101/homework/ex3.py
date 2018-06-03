__author__ = 'twlhgs'

n = input('Input N: ')
char_lst = list(n)
for i in char_lst[::-1]:
    if i == '0':
        char_lst.pop()
        continue
    else:
        break

if char_lst[0] == '-':
    dash, *char_lst = char_lst
    char_lst.reverse()
    char_lst.insert(0, dash)
else:
    char_lst.reverse()

print(''.join(char_lst))

