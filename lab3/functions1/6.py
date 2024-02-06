def fun(sentence):
    a = word.split(" ")
    i = len(a) - 1
    while i >= 0:
        print(a[i], end = " ")
        i-=1

word = str(input())
fun(word)


