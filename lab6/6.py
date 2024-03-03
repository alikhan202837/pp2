import os
l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in range(len(l)):
    with open(f"{l[i]}.txt", "w") as f:
        f.write(f"Hello from {l[i]}.txt!")

# for i in l:
#     os.remove(f"{i}.txt")
        
        