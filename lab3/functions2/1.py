from movies import fun

copy_dict = fun()

def imdb(a):
    if a >= 5.5:
        return True
    return False

# "Usual suspects"
single_movie = copy_dict[0]["imdb"]

print(imdb(single_movie))
