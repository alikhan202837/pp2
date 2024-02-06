from movies import fun

#Write a function that returns a sublist of movies with an IMDB score above 5.5.

def movie5_5(a):
    if a >= 5.5:
        return True
    return False
    
copy_dict = fun()

list_of_movies = []


for i in range(len(copy_dict)):
    imdb = copy_dict[i]["imdb"]
    if movie5_5(imdb):
        list_of_movies.append(copy_dict[i]["name"])


print(list_of_movies)
