from movies import fun

copy_dict = fun()


my_list = []


def that_category(a):
    for i in range(len(copy_dict)):
        if copy_dict[i]["category"] == a:
            my_list.append(copy_dict[i]["name"])

category = input()

that_category(category)

print(my_list)

