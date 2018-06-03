# def remove_element(self, lst, rem):
# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.


# def list_common(self, list1, list2):
# write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.


class ParseIteration:
    def __init__(self):
        pass

    def remove_element(self, lst, rem):
        new_lst = []
        for item in lst:
            if(item < rem):
                new_lst.append(item)
            else:
                continue
        return new_lst

    def list_common(self, list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        new_set = set1 & set2
        com_list = list(new_set)
        return com_list

    def test(self):
        pass


list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

lstwork = ParseIteration()

post_list1 = lstwork.remove_element(list1, 5)
print(post_list1)

post_list2 = lstwork.list_common(list2, list3)
print(post_list2)