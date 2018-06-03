__author__ = 'twlhgs'

Math_Pass = {'Tom', 'John', 'Mary', 'Jimmy', 'Sunny', 'Amy'}
EN_Pass= {'John', 'Mary', 'Tony', 'Bob', 'Pony', 'Tom', 'Alice'}

print('數學及格但英⽂文不及格: {}'.format(Math_Pass - EN_Pass))

print('數學不及格但英⽂文及格: {}'.format(EN_Pass - Math_Pass))

print('兩科都及格: {}'.format(Math_Pass & EN_Pass))

total = Math_Pass | EN_Pass
print('全班總共{}位同學'.format(len(total)))
