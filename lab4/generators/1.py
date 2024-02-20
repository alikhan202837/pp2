def sq_numbers(n):
    for i in range(1, n + 1): # от 1 до n включительно
        yield i * i

    
n = int(input("Input some number: "))

list_of_sq_num = sq_numbers(n)

for i in range(n):
    print(next(list_of_sq_num), end = " ")
