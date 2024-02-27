"""
snake case string - lower case letters and separated by "_"

camel case = " the first word is written in lowercase, 
and subsequent words are capitalized without any spaces or punctuation

myCamelCase
"""
import re
    
snake_word = "this_is_snake_case_string"

camelCase = ""

snake_word = re.split("_", snake_word)

for i in range(1, len(snake_word)):
        snake_word[i] = snake_word[i][0].upper() + snake_word[i][1:]
camelCase = "".join(snake_word)
print(camelCase)