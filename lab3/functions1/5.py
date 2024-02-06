from itertools import permutations

def permutations_print(word):
    perms = permutations(word)
    for i in perms:
        print(i)

word = str(input())
permutations_print(word)