import sean_fnc.print_fnc

__author__ = 'twlhgs'
movies = ["movie 1",  "movie 2", "movie 3",
          ["sub-movie 1",
          ["dsub-movie 1",
          "dsub-movie 2",
          "dsub-movie 3"
          ]],
          "movie 4"]
cast = ["cast1","cast2","cast3","cast4"]
"""for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)"""

# def print_list(the_list):
#     for each_item in the_list:
#         if isinstance(each_item,list):
#             print_list(each_item)
#         else:
#             print(each_item)

sean_fnc.print_fnc.print_list(movies)
sean_fnc.print_fnc.print_list(movies,True,1)
sean_fnc.print_fnc.print_list(cast,True,1)
sean_fnc.print_fnc.show_list_num(movies)
