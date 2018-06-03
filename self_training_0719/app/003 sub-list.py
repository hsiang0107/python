__author__ = 'twlhgs'
movies = ["movie 1",  "movie 2", "movie 3",
          ["sub-movie 1",
          ["dsub-movie 1",
          "dsub-movie 2",
          "dsub-movie 3"
          ]]]
# print(movies[0])
# print(movies[3])
# print(movies[3][1])

for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)