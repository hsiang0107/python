__author__ = 'twlhgs'
from homework.util.FindMaxCount import FindMaxCount
n = input('Input N: ')
key_dict = {}
max_lst = []
lst1 = list(n)
set1 = set(lst1)

for i in set1:
    key_dict.update({i: lst1.count(i)})

max_cun = max(key_dict.values())
for key in key_dict.keys():
    if key_dict[key] == max_cun:
        max_lst.append(key)
max_lst.sort()
print(','.join(max_lst), '({})'.format(max_cun))


