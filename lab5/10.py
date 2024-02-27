import re

camelCase = "thisStringInCamelCase"

#this_string_in_camel_case
snake_word = ""

for i in range(len(camelCase)):
    if camelCase[i].isupper():
        p = re.sub("[A-Z]", f"_{camelCase[i].lower()}", camelCase[i])
        snake_word += p
    else:
        snake_word += camelCase[i]

print(snake_word)