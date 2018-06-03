__author__ = 'twlhgs'

class FindMaxCount:

    def __init__(self):
        pass

    def find_match_by_max_count(self, num):
        dic = self._make_dic(num)
        max_count = self._find_max_value(dic)
        match_lst = []
        for key in dic.keys():
            if dic[key] == max_count:
                match_lst.append(key)
        match_lst.sort()
        return list(map(int, match_lst)), max_count

    def _find_max_value(self, dic):
        max_cun = max(dic.values())
        return max_cun

    def _make_dic(self, num):
        count_dict = {}
        full_lst = list(str(num))
        set1 = set(full_lst)
        for i in set1:
            count_dict.update({i: full_lst.count(i)})
        return count_dict

input_num = input('Input N: ')
find_max = FindMaxCount()
match_list = list(map(str, find_max.find_match_by_max_count(input_num)[0]))
max_count = find_max.find_match_by_max_count(input_num)[1]
print(','.join(match_list), ' ({})'.format(max_count))

