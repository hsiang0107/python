__author__ = 'twlhgs'
movies = ["movie 1", "movie 2", "movie 3"]
#print(movies[0])
movies.append("movie 4")
print(movies)
#movies.pop()
movies.extend(["movies 5","movie 6"])
print(movies)
movies.insert(3,"tmp movie")
print(movies)
movies.remove("tmp movie")
print(movies)
print(len(movies))