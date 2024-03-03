import os

if os.path.exists(r"C:\Users\Asus\Desktop\pp2\lab6\folder\2.txt") == False:
    print("File doesn't exist")

else:
    with open(r"C:\Users\Asus\Desktop\pp2\lab6\folder\2.txt", "w") as fw:
        fw.write("Added to 2.txt")
    with open(r"C:\Users\Asus\Desktop\pp2\lab6\folder\2.txt", "r") as fr:
        file_info = fr.read()
        print(file_info)
