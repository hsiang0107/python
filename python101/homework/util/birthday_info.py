import time

__author__ = 'twlhgs'

class BirthdayInfo:

    def __init__(self):
        self.calendar = {1: ('January', []), 2: ('February', []), 3: ('March', []), 4: ('April', []),
                         5: ('May', []), 6: ('June', []), 7: ('July', []), 8: ('August', []),
                         9: ('September', []), 10: ('October', []), 11: ('November', []), 12: ('December', [])}

    def monthly_view(self, bdic):
        month_dic = self.format_birthday(bdic)
        for person, mon in month_dic.items():
            self.calendar[mon][1].append(person)
            self.calendar[mon][1].sort()
        return self.calendar

    def format_birthday(self, bdic):
        format_dic = {}
        for person in bdic.keys():
            try:
                struct_time = time.strptime(bdic[person], '%Y.%m.%d')
            except ValueError:
                struct_time = time.strptime(bdic[person], '%Y/%m/%d')
            format_dic.update({person.title(): struct_time.tm_mon})
        return format_dic


people_birthday = {"alex": "1982.04.30", "andrew": "2008.8.19", "diego": "2010/02/20", "fanny": "1978/11/29",
                   "peggy": "1985/4/10"}
bday = BirthdayInfo()
bir_dic = bday.monthly_view(people_birthday)

out = open('ex4_result.txt', 'w', encoding='UTF-8')
for item in bir_dic.values():
    print(item[0], '({})'.format(len(item[1])), ', '.join(item[1]), file=out)
out.close()
