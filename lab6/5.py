import os
import json
l = ["Naruto", "Sasuke", "Minato", "Namikaze"]

#by json
with open("5.txt", "w") as f:
    f.write(json.dumps(l))

#deleting
# os.remove("5.txt")

#second method
# with open("5.txt", "w") as f:
#     f.writelines("\n".join(l))

