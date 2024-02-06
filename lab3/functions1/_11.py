def palindrome(string):
    check = ""
    i = len(string) - 1
    
    while(i >= 0):
        check += string[i]
        i-=1

    if string == check:
        return "YES, it is paindrome"
    else:
        return "NO("
    
word = input()

print(palindrome(word))
