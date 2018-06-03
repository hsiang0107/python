__author__ = 'twlhgs'

class ParseSentence:

    def __init__(self):
        pass

    def list_hot_word(self, stnc):
        hot_word = []
        full_dic = self._make_dic(stnc)
        count_list = self._hot_count_list(full_dic)
        for count in count_list:
            words = self._find_match_word(full_dic, count)
            hot_word.extend(words)
        return hot_word
        # for word in full_dic.keys():
        #     if full_dic[word] == hot_list[-1]:
        #         match_list.append((word, full_dic[word]))
        # for word in full_dic.keys():
        #     if full_dic[word] == hot_list[-2]:
        #         match_list.append((word, full_dic[word]))
        # return match_list

    def reverse_sentence(self, stnc):
        # return ' '.join(stnc.split()[::-1])
        stnc_list = stnc.split()
        stnc_list.reverse()
        rev_stnc = ' '.join(stnc_list)
        return rev_stnc

    def _make_dic(self, stnc):
        mkdic = {}
        stnc = stnc.replace(',', '')
        stnc = stnc.replace('.', '')
        unify_stnc = stnc.lower()
        stnc_lst = unify_stnc.split(' ')
        for word in stnc_lst:
            mkdic.update({word: stnc_lst.count(word)})
        return mkdic

    def _hot_count_list(self, dic):
        set1 = set(dic.values())
        list1 = list(set1)
        hot_count_list = sorted(list1, reverse=True)
        return hot_count_list[0:2]

    def _find_match_word(self, dic, count):
        word_list = []
        for word in dic.keys():
            if dic[word] == count:
                word_list.append((word, count))
        return word_list



sample1 = 'I am a boy,and I love Job. But I want a good job.'
sample2 = 'Open  a book'
empty_sample = ''
# Exercise 1
# ex1 = ParseSentence()
# hot_word = ex1.list_hot_word(sample1)
# print(hot_word)
# for item in hot_word:
#     print(item[0], ' ({})'.format(item[1]))

# Exercise 2
ex2 = ParseSentence()
pars_sample2 = ex2.reverse_sentence(sample2)
print(pars_sample2)
pars_empty_sample = ex2.reverse_sentence(empty_sample)
print(pars_empty_sample)