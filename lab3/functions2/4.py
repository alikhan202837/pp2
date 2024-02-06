from movies import fun

copy_dict = fun()

def calculate():
    sum = 0
    for i in range(len(copy_dict)):
        sum += copy_dict[i]["imdb"]
    return sum/len(copy_dict)

print("Average IMDB score of all movies is", round(calculate(), 3))