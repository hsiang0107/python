import sys

__author__ = 'twlhgs'

def print_list(the_list,tab=False,level=0,fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_list(each_item,tab,level+1,fh)
        else:
            if tab:
                for tap_num in range(level):
                    print("\t",end='',file=fh)
            print(each_item,file=fh)

def show_list_num(the_list):
    print(len(the_list))