import re

m = "My name is Alikhan, I'm 18 years old. There will be three ':'- ,.}"

m = re.sub(r"\s|,|[.]", ":", m)

print(m)