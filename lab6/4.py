# with open("4.txt", "r") as file:
#     x = file.readlines()

# print("Number of lines:",len(x))  


cnt = 0
with open("4.txt", "r") as file:
    line = file.readline()
    while line != "":
        cnt+=1
        line = file.readline()
print(cnt)

