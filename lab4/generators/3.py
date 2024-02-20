def squares(a, b):
    for i in range(a, b + 1):
        yield pow(i, 2)

a, b = map(int, input("Two numbers with space: ").split())

list_of_sq = squares(a, b)

for i in list_of_sq:
    print(i, end = " ")