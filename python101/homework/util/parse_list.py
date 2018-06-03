__author__ = 'twlhgs'

class ParseList:

    def __init__(self):
        pass

    def list_plus_one(self, lst_in):
        str_in = ''.join(str(e) for e in lst_in)
        num_in = int(str_in)
        num_in += 1
        str_out = list(str(num_in))
        lst_out = list(map(int, str_out))
        return lst_out

    def get_max_product(self, lst_in):
        product = None
        # lst_out = []

        lst_len = len(lst_in)
        for start_elem, value in enumerate(lst_in):
            for end_elem in range(start_elem + 1, lst_len + 1):
                mul = self.get_multiple(lst_in[start_elem: end_elem])
                if product is None:
                    product = mul
                    # lst_out = lst_in[start_elem: end_elem]
                if mul > product:
                    product = mul
                    # lst_out = lst_in[start_elem: end_elem]
        # return product, lst_out
        return product

    def get_permutation(self, lst_in):
        lst_out = []
        if len(lst_in) <= 1:
            # yield lst_in
            lst_out.append(lst_in)
        else:
            for lst_perm in self.get_permutation(lst_in[1:]):
                for i in range(len(lst_in)):
                    # yield lst_perm[:i] + lst_in[0:1] + lst_perm[i:]
                    lst_out.append(lst_perm[:i] + lst_in[0:1] + lst_perm[i:])
        return lst_out

    def get_multiple(self, lst):
        multiple = 1
        for elem in lst:
            multiple = multiple * elem
        return multiple

lst_sample1 = [9, 9, 9, 9]
# lst_sample2 = [0, 1, 2, 3]
lst_sample2 = [1,-5,6,-5,2,-4,-5,0,3,2,-4,0,-5,-3,-1,-4,-1,4,1,-1,-3,-1,1,3,-4,-6,-2,5,1,-5,0,-1,-5,0,1,2,6,1,2,-6,5,5,0,1,0,1,1,-1,-1,3,1,0,4,-3,0,4,-4,-1,6,5,5,6,-6,1,1,3,4,3,-1,-3,0,-5,-4,1,5,-2,3,-1,2,1,1,6,0,5,-5,6,-6,3,0,4,-1,3,6,0,-2,0,-1,6,4,1,-5,1,0,1,-1,-1,3,5,5,4,2,5,0,-1,5,2,2,-3,-1,-1,0,-6,-2,-5,1,-2,2,0,0,2,-3,-2,-4,1,1,-4,-3,-1,0,0,1,-3,-2,3,-4,5,2,-1,4,1,5,6,0,1,1,-2,-1,0,-1,-5,5,6,6,-1,-1,0,-4,2,1,3,-5,6,-5,-1,-1,-3,-1,-4,-2,-1,-1,1,-3,-4,0,1,-3,4,3,2,-2,6,-3,-6,-6,-2,-5,1,2,0,-1,0,0,-2,3,-4,2,4,3,-1,3,1,0,2,1,-1,0,5,-1,-3,-6,-5,0,6,6,-6,-5,4,-2,-1,0,4,6,-3,1,-1,0,1,-5,5,-3,-3,-3,-1,-1,4,0,-2,-4,3,5,5,-1,-1,-5,-2,-4,-4,6,0,-3,-1,-5,-3,-1,6,1,-5,-1,0,1,-4,-5,0,0,0,-3,-5,-1,-4,-1,5,5,-4,4,-1,6,-1,1,-1,2,-2,-3,0,1,0,0,-3,0,2,5,-6,-3,-3,3,-4,-2,-6,-1,1,4,4,0,-6,-5,-6,-3,5,-3,1,-4,6,-2,0,-4,-1,0,-1,0,6,-6,0,5,0,1,-3,6,1,-1,1,0,-1,1,-1,-6,-3,4,-1,-4,6,4,-1,-3,2,-6,5,0,4,-2,1,0,4,-2,2,0,0,5,5,-3,4,3,-5,2,2,6,-1,-2,1,-3,1,-1,6,-4,0,0,0,2,-5,-4,2,6,-3,-6,-1,-6,0,0,2,-1,6,-4,-5,-1,0,-3,-3,-1,0,-4,3,1,5,0,2,5,0,4,-5,-1,3,1,-1,-1,1,1,-2,3,5,4,6,2,6,-6,5,2,-3,0,-1,-1,3,1,1,1,-2,-5,3,-1,3,0,-1,3,1,1,-2,6,3,-6,5,-5,-5,0,-2,-3,-3,-4,6,-1,-6,6,-3,-5,1,-1,0,0,1,4,-5,0,1,-2,6,1,-3,-5,0,4,-2,1,-5,-4,0,0,-1,-2,0,2,-2,5,6]
lst_sample3 = [1, 2, 3]
prs_lst = ParseList()

# EX1
# parsed_sample = prs_lst.list_plus_one(lst_sample1)
# print(parsed_sample)

# EX2
# max_product = prs_lst.get_max_product(lst_sample2)
# print(max_product[1], max_product[0])
# print(max_product)

# EX3
# for p in prs_lst.get_permutation(lst_sample3):
#     print(p)
parsed_sample = prs_lst.get_permutation(lst_sample3)
print(parsed_sample)

