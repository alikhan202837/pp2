def fun(n):
    i = n
    while i >= 0:
        yield i
        i -= 1


n = int(input("Input number: "))

reversed_list = fun(n)

for i in reversed_list:
    print(i, end = " ")


# def fun(n):
#     for i in range(n, -1, -1):
#         yield i

# n = int(input())
# a = fun(n)

# for i in a:
#     print(i, end = " ")