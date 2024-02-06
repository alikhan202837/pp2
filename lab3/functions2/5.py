from movies import fun

copy_dict = fun()

def calculate(a):
    global sum
    sum += a
    return sum


category = input()

sum = 0
cnt = 0
for i in range(len(copy_dict)):
    if copy_dict[i]["category"] == category:
        cnt += 1
        calculate(copy_dict[i]["imdb"])

print(f"Average IMDB score of the category {category} is", sum/cnt)