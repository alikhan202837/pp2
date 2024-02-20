def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
            


n = int(input("Input number: "))

list_of_even_numbers = even_numbers(n)



for i in list_of_even_numbers:
    print(i, end = " ")