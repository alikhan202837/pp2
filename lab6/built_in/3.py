s = input("String to chech palindrome: ")

print(list(reversed(s)))
if "".join(reversed(s)) == s:
    print("Yes it is palindrome")
else:
    print("No")