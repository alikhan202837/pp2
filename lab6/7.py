import os
#creating
with open("7.txt", "w") as file:
    file.write("""Information that in 7.txt will copy
in 7_1.txt""")

#copy
with open("7_1.txt", "w") as file1, open("7.txt", "r") as file:
    file1.write(file.read())

with open("7_1.txt", "r") as file1:
    print(file1.read())

#checking for closed
print(file.closed)
print(file1.closed)
# os.remove("7.txt")
# os.remove("7_1.txt")